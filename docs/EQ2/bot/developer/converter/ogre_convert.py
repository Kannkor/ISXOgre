#!/usr/bin/env python
"""ogre_convert.py - convert OgreBot Classic script lines to the new OgreBot, from conversion-map.json alone.

    python ogre_convert.py lookup <old name> [...]          what happened to a name, and what to write
    python ogre_convert.py fix <file.iss> [-o out.iss]      the MECHANICAL pass (safe rewrites only) + a to-do list
    python ogre_convert.py fix <file.iss> --in-place        same, but keep the file's name: the original is copied to
                                                            <file>.classic.iss first, then <file>.iss is converted
    python ogre_convert.py sweep <file|folder> [...]        is a converted file clean?  exit 0 = clean
    python ogre_convert.py coverage <file|folder> [...]     does the map know every Classic name these files use?
    python ogre_convert.py sites <file|folder> [...]        lines to KEEP and LIST: game-server name lookups (R10),
                                                            actor scans (R12), unbounded index reads (INDEX)

Needs only Python 3 and conversion-map.json (same folder, or --map <path>). It reads no bot source, so it
runs anywhere the map has been copied to. Open source, like the map.

WHAT `fix` REWRITES - and nothing else:
  * an old call whose map row says `moved` / `renamed` with the same arguments: the call is swapped,
    the arguments are left exactly as they were;
  * an old call whose ONLY change is "the for-who is now argument 0" on an object that acted on its own
    session (every Ogre_CampSpot / Obj_* / OgreBotAPI method that had no for-who): `all` is inserted
    first - a script's own call only ever runs on the session running it, so that is what the old call did;
  * a console verb that was renamed with the same arguments;
  * a Classic framework variable renamed to a plain member: `${OgreRelayGroup}` (and `${OgreRelayGroup.Length}`
    etc.) becomes `${ISXOgreEQ2.Auth.RelayGroup}` - the same text under its new name.
Everything else - argument reorders, changed arguments, data-file moves, not-ported names - is left in
place and listed as a TO-DO with the map's how-to-fix line. A person (or Claude, following the
"Converting your scripts" page of the OgreBot docs) does those.

WHAT `sweep` CALLS UNRESOLVED (any of these -> exit 1):
  OLD      a line still uses a Classic spelling whose row is not `unchanged`
  UNKNOWN  a Classic-style call the map has no row for
  UNKNOWN  a console verb that is neither in the map nor in the new console
  BROKEN   a new-bot call (OgreBotAPI.<Group>...) that does not exist, or a console line with the command
           in quotes
  and it WARNS (does not fail) on a console verb whose arguments changed order or meaning - the sweep
  cannot see whether you already fixed them.
Commented-out lines (first character `;`) are ignored, so `; TODO(Classic): ...` notes are fine.
"""
import io, os, re, sys, json, argparse, shutil

HERE = os.path.dirname(os.path.abspath(__file__))

# ------------------------------------------------------------------ the map
class Map:
    def __init__(self, path):
        self.m = json.load(io.open(path, encoding='utf-8'))
        self.rows = self.m['rows']
        self.by_call = {}            # (surface lower, name lower) -> row
        self.by_verb = {}            # console verb lower -> row
        self.by_any = {}             # bare name lower -> [rows]
        for r in self.rows:
            if r['surface'] == 'console':
                self.by_verb[r['oldName'].lower()] = r
            elif r.get('oldKinds') != ['event'] and '|' not in r['id']:
                self.by_call[(r['surface'].lower(), r['oldName'].lower())] = r
            elif '|' in r['id']:
                mm = re.match(r'^(?:\$\{)?([A-Za-z0-9_]+)[.:]([A-Za-z0-9_]+)', r['oldName'])
                if mm: self.by_call.setdefault((mm.group(1).lower(), mm.group(2).lower()), r)
            self.by_any.setdefault(r['oldName'].lower(), []).append(r)
            self.by_any.setdefault(r['oldCall'].lower(), []).append(r)
        self.surfaces = sorted({k[0] for k in self.by_call}, key=len, reverse=True)
        self.surface_set = set(self.surfaces) | {r['surface'].lower() for r in self.rows}
        self.new_api = {k.lower(): (k, v) for k, v in self.m.get('newApi', {}).items()}
        self.new_groups = {k.split('.', 1)[1].lower() for k in self.m.get('newApi', {})
                           if k.count('.') == 1 and ':' not in k}
        self.new_console = {v.lower() for v in self.m.get('newConsole', [])}
        oi = self.m.get('optionIds') or {}
        self.opt_new = set(oi.get('new', []))
        self.opt_renamed = oi.get('renamed', {})
        self.opt_old = set(oi.get('oldNotInNew', []))
        self.opt_removed = oi.get('removed', {})
        names = '|'.join(re.escape(s) for s in self.surfaces)
        self.OLD = re.compile(r'(?<![A-Za-z0-9_.])(call\s+)?(%s)([.:])([A-Za-z0-9_]+)' % names, re.I)
        self.NEW = re.compile(r'(?<![A-Za-z0-9_])OgreBotAPI\.([A-Za-z0-9_]+)(?:([.:])([A-Za-z0-9_]+))?')
        # a console line: `oc !c …`, `irc !c …`, or a bare `!c …` (an MCP console-route button)
        self.OC = re.compile(r'(?:\b(?:oc|irc)\s+|^\s*)!(?:ci?|command)\b\s*(.*)$', re.I)
        self.con_params = {k: v for k, v in self.m.get('newConsoleParams', {}).items()}
        self.new_ogre = set(self.m.get('newOgre', []))
        self.idioms = [(re.compile(e['pattern']), e) for e in self.m.get('idioms', [])]
        # Classic globals NO surface covers (framework objects, objectdefs, global functions/atoms): any use
        # is UNKNOWN - the map cannot convert what it does not know, and must never call such a file CLEAN
        self.unmapped = dict(self.m.get('oldBotUnmapped', {}))
        # ruled Classic framework names (IC helpers, top-level functions ...): found like an unmapped global,
        # answered by their row. 'OldBot framework' is the map's surface KEY for them (a key, not display text).
        self.by_fw = {r['oldName']: r for r in self.rows if r['surface'] == 'OldBot framework'}
        for k in self.by_fw:
            if not k.startswith('ogre '): self.unmapped.setdefault(k, 'Classic framework')   # `ogre <word>`: raw_commands
        self.UNM = re.compile(r'(?<![A-Za-z0-9_.:$-])(%s)(?![A-Za-z0-9_])' % '|'.join(
            re.escape(n) for n in sorted(self.unmapped, key=len, reverse=True))) if self.unmapped else None

def find_map(p):
    for c in ([p] if p else []) + [os.path.join(HERE, 'conversion-map.json'), 'conversion-map.json']:
        if c and os.path.exists(c): return c
    sys.exit('conversion-map.json not found - pass --map <path>')

# ------------------------------------------------------------------ scanning one line
def new_spans(M, line):
    """-> [(start, end, text, ok)] for every OgreBotAPI.<Group>... call (a NEW-style call)."""
    out = []
    for m in M.NEW.finditer(line):
        grp = m.group(1)
        if grp.lower() not in M.new_groups:
            continue                      # OgreBotAPI.<member> on the flat object - judged as an old call
        full = 'OgreBotAPI.%s%s%s' % (grp, m.group(2) or '', m.group(3) or '')
        ok = full.lower() in M.new_api
        out.append((m.start(), m.end(), full, ok))
    return out

def old_hits(M, line, skip):
    out = []
    for m in M.OLD.finditer(line):
        if any(a <= m.start() < b for a, b, _, _ in skip): continue
        surf, sep, name = m.group(2), m.group(3), m.group(4)
        if surf.lower() == 'ogrebotapi' and name.lower() in M.new_groups and sep == '.':
            continue                      # a new group handle, handled by new_spans
        row = M.by_call.get((surf.lower(), name.lower()))
        out.append((m, surf, sep, name, row))
    return out

META = ('-tab', '-rg', '-endargs')

def console_hits(M, line):
    """-> [(verb, quoted, pos)] EVERY command on a console line, walked the way the new console parses it:
    a known command takes its parameters - a forwho the next non-dash
    token, a rest everything up to the next known command (or -endargs when allParams), anything else the next
    token that is not a known command - and the next token starts over. So `-nc` inside a -RunScriptOB line is
    an argument, while a chain `-letsgo all -RODMIR a b` is two commands. A dash token no command takes is
    reported (a Classic verb, or unknown)."""
    first = console_hit(M, line)
    if not first: return []
    if first[1]: return [first]                         # the whole command in quotes - nothing in it parses
    m = M.OC.search(line)
    toks = [(t.group(0), m.start(1) + t.start()) for t in re.finditer(r'"[^"]*"?|\S+', m.group(1))]
    known = lambda t: t.lower() in M.new_console
    bound = lambda t: t.lower() in META or known(t)
    out, i, n = [], 0, len(toks)
    while i < n and toks[i][0].lower() in ('-cfw', '-tab', '-rg'):
        i += 2                                           # the line's leading routing flags
    while i < n:
        t, pos = toks[i]
        tl = t.lower()
        if tl in META:
            i += 2 if tl in ('-tab', '-rg') else 1; continue
        if known(t):
            out.append((t, False, pos)); i += 1
            for typ, allp in M.con_params.get(tl, []):
                if typ == 'rest':
                    while i < n and not (toks[i][0].lower() == '-endargs' if allp else bound(toks[i][0])): i += 1
                    if i < n and toks[i][0].lower() == '-endargs': i += 1
                elif typ == 'forwho':
                    if i < n and not toks[i][0].startswith('-'): i += 1
                elif i < n and not bound(toks[i][0]):
                    i += 1
            continue
        if re.match(r'^-[A-Za-z]', t):
            out.append((t, False, pos)); i += 1      # a Classic verb or an unknown one; its own words follow
            while i < n and not toks[i][0].startswith('-'): i += 1
            continue
        i += 1                                           # a stray word (e.g. `irc !c <dest>`) - not a command
    return out or [first]

def console_hit(M, line):
    m = M.OC.search(line)
    if not m: return None
    rest = m.group(1)
    # Leading -tab/-rg/-cfw <value> are the new console's per-line routing flags, not verbs:
    # `oc !ci -cfw igw:${Me.Name} -letsgo` = -letsgo for igw:<me>. Skip them.
    off = 0
    while True:
        f = re.match(r'(-(?:tab|rg|cfw))\s+("[^"]*"|\S+)\s*', rest[off:], re.I)
        if not f: break
        off += f.end()
    body = rest[off:]
    quoted = bool(re.match(r'^(?:\S+\s+)*?"\s*-[A-Za-z]', body)) and not re.match(r'^-[A-Za-z]', body)
    v = re.search(r'(?:^|\s|")(-[A-Za-z][A-Za-z0-9_\-]*)', body)
    if not v: return None
    return v.group(1), quoted, m.start(1) + off + v.start(1)

# an OgreBot OPTION id: -ChangeOgreBotUIOption <fw> <id> ..., ChangeOgreBotUIOption[<fw>,<id>,...],
# OgreBot.Value["<id>"], TabConfig.<Tab>.<id>. Only ids that look like control ids are checked.
OPT_RX = [re.compile(r'-ChangeOgreBotUIOption\s+\S+\s+"?([A-Za-z][A-Za-z0-9_]+)', re.I),
          re.compile(r'ChangeOgreBotUIOption\[\s*"?[^,\]]*"?\s*,\s*"?([A-Za-z][A-Za-z0-9_]+)', re.I),
          re.compile(r'OgreBot\.Value\[\s*"?([A-Za-z][A-Za-z0-9_]+)'),
          re.compile(r'Options:Set\[\s*"?[^,\]]*"?\s*,\s*"?([A-Za-z][A-Za-z0-9_]+)'),     # the new setter, for-who first
          re.compile(r'Options\.Value\[\s*"?([A-Za-z][A-Za-z0-9_]+)'),
          re.compile(r'TabConfig\.[A-Za-z0-9_]+\.([a-z][A-Za-z0-9_]+)')]
OPT_PREFIX = re.compile(r'^(?:checkbox|combobox|textentry|slider|listbox|button|radio)_', re.I)

def option_hits(M, line):
    """-> [(id, verdict, text)] verdict: ok | renamed | unknown"""
    if not M.opt_new: return []
    out = []
    for rx in OPT_RX:
        for m in rx.finditer(line):
            i = m.group(1)
            if not OPT_PREFIX.match(i) or i.endswith('_'): continue      # not a control id (or built at runtime)
            if i in M.opt_new: continue
            if i in M.opt_renamed: out.append((i, 'renamed', 'option id renamed -> %s' % M.opt_renamed[i]['to'])); continue
            if i in M.opt_removed:
                out.append((i, 'removed', 'option id that never did anything (not even in Classic) - delete the line')); continue
            out.append((i, 'unknown', 'option id the new bot does not have%s - stop and ask (renames exist; never guess one from a similar name)'
                        % ('' if i in M.opt_old else ' (not a Classic id either - check the spelling)')))
    return out

# names a file defines ITSELF are its own code, never an unknown Classic global - many instance files carry
# their own copy of move_to_next_waypoint / kill_trash
LOCAL_DEF = re.compile(r'^\s*(?:function(?::\w+)?|atom(?:\(\w+\))?|objectdef|method|member(?::\w+)?)\s+([A-Za-z_]\w*)'
                       r'|^\s*(?:variable(?:\(\w+\))?\s+[\w:]+|declarevariable)\s+([A-Za-z_]\w*)'
                       r'|^\s*#define\s+([A-Za-z_]\w*)', re.M | re.I)

def local_defs(text):
    return {next(g for g in m.groups() if g) for m in LOCAL_DEF.finditer(text)}

# Classic names its objects Ogre* / Obj_* / Object_* / Ob_*; the new bot's only such top-level objects are OgreBotAPI and,
# in the uplink, OgreConsoleHub (the session watch - `OgreConsoleHub.Sessions...`, what the ogreping idioms write).
NEW_TOP_OBJECTS = ('OgreBotAPI', 'OgreConsoleHub')
# An object of that shape the map has never heard of (and the file does not define) is an UNKNOWN - otherwise
# `Ogre_Instance_Controller:ZoneSet` or a typo such as `OgreIH:Set_Debug_Mode` would pass every check.
OLDOBJ = re.compile(r'(?<![A-Za-z0-9_.$])((?:Ogre|Obj_|Object_|Ob_)[A-Za-z0-9_]*)(?=\s*[.:][A-Za-z_])')
INCL = re.compile(r'^\s*#include(?:optional)?\s+"?([^"\r\n]+)', re.I)
CLASSIC_TREES = re.compile(r'(?:^|[\\/])(?:EQ2OgreBot|EQ2OgreCommon|OgreCommon|EQ2OgreCraft|EQ2OgreHarvest)[\\/]', re.I)

# `ogre <word>` in COMMAND position only (a line start, after `relay <group>` / `timedcommand <n>` / execute, or a
# quoted command) and lowercase - `echo "Ogre will ..."` is prose
OGRECMD = re.compile(r'(?:^\s*|relay\s+\S+\s+|timedcommand\s+\d+\s+|execute\s+|")ogre(?:\s+end)?\s+([a-z][a-z0-9_]*)')
OLDEXT = re.compile(r'\bext\s+(?:-unload\s+)?isxogre(?![A-Za-z0-9])', re.I)

def raw_commands(M, line):
    """-> [(text, why)] raw bot commands a button or script types: `ogre <word>` the new bot has no such
    word for, and loading / unloading the OLD extension."""
    out = []
    if M.OC.search(line): return out
    for m in OGRECMD.finditer(line):
        w = m.group(1).lower()
        if not M.new_ogre or w in M.new_ogre: continue
        fw = M.by_fw.get('ogre ' + w)
        if fw:                                   # ruled: answered by its row (OLD), not a question
            out.append(('ogre ' + w, '[%s] -> %s' % (fw['status'], fw.get('howToFix') or ''), fw)); continue
        out.append(('ogre ' + w, 'the new bot has no `ogre %s` command - stop and ask (`ogre ?` lists them)' % w, None))
    if OLDEXT.search(line):
        out.append(('ext isxogre', 'loads or unloads the OLD extension (ISXOgre) - the new bot is ISXOgreX; stop and ask', None))
    return out

def idiom_hits(M, line):
    """-> [(start, end, text, entry)] Classic IDIOMS on the line (map `idioms`, first entry wins a span) - e.g.
    `${Script["Buffer:OgreBot"](exists)}` reads NULL under the new bot."""
    out, taken = [], []
    for rx, e in M.idioms:
        for m in rx.finditer(line):
            if any(a < m.end() and m.start() < b for a, b in taken): continue
            taken.append((m.start(), m.end())); out.append((m.start(), m.end(), m.group(0), e))
    return sorted(out)

def unknown_objects(M, line, own=frozenset()):
    """-> [(name, why)] Classic-shaped objects nothing knows, and #includes of Classic's own files."""
    out = []
    mi = INCL.match(line)
    if mi and CLASSIC_TREES.search(mi.group(1)):
        out.append((mi.group(1).strip(), 'includes a Classic file - the new bot does not load Classic; remove the #include once '
                                         'nothing in this file uses what it brought in', None))
        return out
    if mi:
        return out          # the user's own #include - a FILE name (`.../Object_Trash.iss`), not an object
    s = re.sub(r'"[^"]*"', lambda m: re.sub(r'[^$]', ' ', m.group(0)) if '${' not in m.group(0) else m.group(0), line)
    for m in OLDOBJ.finditer(s):
        n = m.group(1)
        if n in NEW_TOP_OBJECTS or n in own or n.lower() in M.surface_set or n in M.unmapped: continue
        if any(k in line for k in M.by_fw if k.startswith((n + ':', n + '.'))): continue   # a ruled member of it
        out.append((n, 'a Classic-style object the map does not know (and this file does not define) - stop and ask', None))
    return out

def unmapped_hits(M, line, own=frozenset()):
    if not M.UNM: return []
    # plain text inside quotes is not a use - but a ${...} inside quotes IS (`press -hold "${OgreForwardKey}"`)
    def _blank(m):
        t = m.group(0)
        keep = [(x.start(), x.end()) for x in re.finditer(r'\$\{[^}]*\}', t)]
        return ''.join(ch if any(a <= i < b for a, b in keep) else ' ' for i, ch in enumerate(t))
    s = re.sub(r'"[^"]*"', _blank, line)
    if M.OC.search(line):        # `-CastAbilityOnNPC auto Intercept`: an ability NAME, not the Intercept helper
        s = ' '.join(re.findall(r'\$\{[^}]*\}', line))
    def by_old_hits(u):            # `Obj_X.Name` with a row is reported by old_hits already - never twice
        mm = re.match(r'^([A-Za-z0-9_]+)[.:]([A-Za-z0-9_]+)$', u)
        return bool(mm and (mm.group(1).lower(), mm.group(2).lower()) in M.by_call)
    return [m.group(1) for m in M.UNM.finditer(s) if m.group(1) not in own and not by_old_hits(m.group(1))]

def live(line):
    s = line.strip()
    return s and not s.startswith(';')

def live_lines(text):
    # (line number, line, is_live) - `;` lines and /* ... */ blocks are not live (a comment is not a call)
    inblock = False
    for i, l in enumerate(text.split('\n'), 1):
        st = l.strip()
        if inblock:
            if '*/' in st: inblock = False
            yield i, l, False; continue
        if st.startswith('/*'):
            inblock = '*/' not in st
            yield i, l, False; continue
        yield i, l, live(l)

# ------------------------------------------------------------------ lookup
# names lookup answers 'not Classic - unchanged' instead of 'NOT IN THE MAP' (`lookup oc` / `Script` must not
# say 'stop and ask'). Only names the bot's own docs use - add when one is missed.
CONSOLE_PREFIX = {'oc', 'irc', '!c', '!ci', '!command'}
CORE_NAMES = {'script', 'session', 'lavishscript', 'math', 'if', 'echo', 'wait', 'waitframe', 'call', 'return',
              'timedcommand', 'relay', 'runscript', 'endscript', 'squelch', 'execute', 'me', 'target', 'actor',
              'zone', 'eq2', 'eq2execute', 'eq2echo', 'eq2uipage', 'isxeq2'}

def cmd_lookup(M, names):
    for n in names:
        k = n.lower().strip()
        if k in M.new_api:
            # a NEW-bot name: say that it exists, and which old names lead to it
            name = M.new_api[k][0]
            frm = sorted({r['oldCall'] for r in M.rows if (r.get('newForm') or '').lower() == k})
            print('%s: a new-bot name - it exists.%s\n' % (name, ('  Old names that become it: ' + ', '.join(frm)) if frm else ''))
            continue
        hits = M.by_any.get(k) or []
        if not hits:
            mm = re.match(r'^(?:\$\{)?(?:call\s+)?([A-Za-z0-9_]+)[.:]([A-Za-z0-9_]+)', n)
            if mm:
                r = M.by_call.get((mm.group(1).lower(), mm.group(2).lower()))
                hits = [r] if r else []
        if not hits and k in M.new_console:
            print('%s: a new-console command - it exists. Parameters: %s\n' % (n, ' '.join(
                '<%s%s>' % (t, '' if not a else ' to -endargs') for t, a in M.con_params.get(k, [])) or '(none)'))
            continue
        if not hits and k in M.surface_set:
            print('%s: a Classic object - look up its members by name, e.g. `lookup %s:<Method>` or `lookup %s.<Member>`\n' % (n, n, n))
            continue
        if not hits:
            idm = [e for rx, e in M.idioms if rx.search(n) or rx.search('Script["%s"](exists)' % n.strip('"'))]
            if idm:
                e = idm[0]
                print('%s: a Classic IDIOM [%s] (%s)\n   howToFix         %s\n%s' % (
                    n, e['status'], e['id'], e.get('howToFix'),
                    ('   why              %s\n' % e['why']) if e.get('why') else '')); continue
        if not hits and k in CONSOLE_PREFIX:
            print('%s: a console prefix, not Classic - unchanged. `oc !c <line>` sends a command to the sessions; '
                  '`oc !ci` is the same but the console window does not show it; `irc !c` goes over IRC; '
                  '`oc <text>` with no !c is chat.\n' % n); continue
        if not hits and k in CORE_NAMES:
            print('%s: a LavishScript / InnerSpace / ISXEQ2 name, not Classic - the switch to the new bot does not change it'
                  '%s\n' % (n, ' (but `Script["Ogre..."](exists)` checks ARE caught - run coverage)' if k == 'script' else '')); continue
        if not hits and re.match(r'^(?:event:)?EQ2_', n):
            print('%s: an ISXEQ2 (game) name, not Classic - the switch to the new bot does not change it\n' % n); continue
        if not hits:
            print('%s: NOT IN THE MAP - stop and ask (or it is new-bot syntax already)\n' % n); continue
        seen = set()
        for r in hits:
            if r['id'] in seen: continue      # a console row is indexed under oldName AND oldCall (the same text)
            seen.add(r['id'])
            print('%s  [%s]  %s' % (r['oldCall'], r['status'], r['id']))
            for f in ('oldSignature', 'newForm', 'newSignature', 'oldSpellingToday', 'howToFix', 'note', 'why'):
                if r.get(f): print('   %-16s %s' % (f, r[f]))
            if r['surface'] == 'console' and r.get('v2Row'):
                print('   %-16s %s %s' % ('newParams', r['v2Row'], ' '.join('<%s>' % x for x in (r.get('v2Params') or []))))
            ex = r.get('example') or {}
            if ex.get('after'):
                print('   example' + ((' (%s)' % ex['beforeAt']) if ex.get('beforeAt') else ''))
                print('     before: %s' % ex['before'])
                print('     after : %s' % ex['after'])
            print()

# ------------------------------------------------------------------ fix (mechanical pass)
FW_NOTE = 'The for-who is now argument 0'

def fix_line(M, line, n, todo, own=frozenset()):
    if not live(line): return line
    skip = new_spans(M, line)
    out, pos = [], 0
    for m, surf, sep, name, row in old_hits(M, line, skip):
        old = m.group(0)
        if row is None:
            todo.append((n, old, 'UNKNOWN', 'not in the map - stop and ask')); continue
        st, nf = row['status'], row.get('newForm') or ''
        if st == 'unchanged':
            continue
        nsep = ':' if ':' in nf.split('OgreBotAPI', 1)[-1] else '.'
        safe = nf.startswith('OgreBotAPI') and not m.group(1) and sep == nsep
        has_args = line[m.end():m.end() + 1] == '['
        args_ok = (not has_args) or row.get('argsCheck') == 'same-count'
        if st in ('moved', 'renamed') and safe and args_ok and not row.get('argsDropped'):
            out.append(line[pos:m.start()]); out.append(nf); pos = m.end()
            todo.append((n, old, 'DONE', '-> %s' % nf)); continue
        if st == 'signature' and safe and (row.get('note') or '').startswith(FW_NOTE) and not row.get('argsDropped')                 and row.get('argsCheck') == 'same-count':
            after = line[m.end():]
            out.append(line[pos:m.start()]); out.append(nf)
            if after.startswith('['):
                out.append('[all,' if not after.startswith('[]') else '[all')
                pos = m.end() + 1
            else:
                out.append('[all]'); pos = m.end()
            todo.append((n, old, 'DONE', '-> %s with `all` as the for-who (the old call acted on its own session; so does this one)' % nf)); continue
        why = row.get('howToFix') or ''
        if st in ('moved', 'renamed', 'signature') and not args_ok:
            why = 'check the arguments first - the map cannot prove they line up. ' + why
        todo.append((n, old, st, why))
    out.append(line[pos:])
    new = ''.join(out)
    for a, b, text, e in reversed(idiom_hits(M, new)):
        if e.get('replace'):
            new = new[:a] + e['replace'] + new[b:]
            todo.append((n, text, 'DONE', '-> %s (%s)' % (e['replace'], e['id'])))
        else:
            todo.append((n, text, 'UNKNOWN' if e['status'] == 'unknown' else e['status'], e.get('howToFix') or ''))
    for r in {e['replace'] for _, _, _, e in idiom_hits(M, line) if e.get('replace')}:
        # `${Script["Buffer:OgreBot"](exists)} || ${Script["OgreBotDev"](exists)}` became the same read twice - keep one
        rr = re.escape('${%s}' % r)
        new = re.sub(r'(!?)%s(?:\s*\|\|\s*\1%s)+' % (rr, rr), lambda m: m.group(1) + '${%s}' % r, new)
    for i, verdict, why in option_hits(M, new):
        if verdict == 'renamed':
            new = re.sub(r'(?<![A-Za-z0-9_])%s(?![A-Za-z0-9_])' % re.escape(i), M.opt_renamed[i]['to'], new)
            todo.append((n, i, 'DONE', '-> %s (option id renamed)' % M.opt_renamed[i]['to']))
        elif verdict == 'removed':
            todo.append((n, i, 'removed', why))
        else:
            todo.append((n, i, 'UNKNOWN', why))
    for u, why, row in unknown_objects(M, new, own) + raw_commands(M, new):
        todo.append((n, u, row['status'] if row else 'UNKNOWN', (row.get('howToFix') or '') if row else why))
    # A Classic framework VARIABLE whose row says `renamed` to a plain member path - OgreRelayGroup ->
    # ISXOgreEQ2.Auth.RelayGroup, which relay-heavy Classic scripts use on almost every relay line. `${Old}` and
    # `${Old.Member}` read the same text under the new name, so the swap is mechanical. Only inside ${ }, and never
    # `${Old[...]}` (a call with arguments is not a variable).
    for name, fw in M.by_fw.items():
        nf = fw.get('newForm') or ''
        if fw['status'] != 'renamed' or not re.match(r'^[A-Za-z0-9_]+(?:\.[A-Za-z0-9_]+)+$', nf):
            continue
        pat = re.compile(r'\$\{%s(?=[}.])' % re.escape(name))
        if pat.search(new):
            new = pat.sub(lambda _m: '${' + nf, new)
            todo.append((n, name, 'DONE', '-> ${%s}' % nf))
    for u in unmapped_hits(M, new, own):
        fw = M.by_fw.get(u)
        if fw:
            if fw['status'] != 'unchanged': todo.append((n, u, fw['status'], fw.get('howToFix') or ''))
            continue
        todo.append((n, u, 'UNKNOWN', 'a Classic global the map has no row for (%s) - stop and ask' % M.unmapped[u]))
    for verb, quoted, at in reversed(console_hits(M, new)):
        row = M.by_verb.get(verb.lower())
        if quoted: todo.append((n, verb, 'QUOTED', 'remove the quotes around the console command and its arguments'))
        if row is None and verb.lower() not in M.new_console:
            todo.append((n, verb, 'UNKNOWN', 'console verb not in the map or the new console'))
        elif row and row['status'] == 'renamed' and row.get('newForm') and not row.get('note'):
            new = new[:at] + row['newForm'] + new[at + len(verb):]
            todo.append((n, verb, 'DONE', '-> %s' % row['newForm']))
        elif row and row['status'] != 'unchanged':
            todo.append((n, verb, row['status'], row.get('howToFix') or ''))
    return new

def backup_name(path):
    stem, ext = os.path.splitext(path)
    return stem + '.classic' + (ext or '.iss')

def cmd_fix(M, path, outp, in_place=False):
    if in_place:
        # Keep the name people type (`run cleanX` keeps working on the new bot) and keep the Classic
        # original beside it. An existing backup is never overwritten: a second run would back up a
        # file that is already converted and lose the real original.
        if outp:
            print('fix: use -o OR --in-place, not both'); return 2
        bak = backup_name(path)
        if os.path.exists(bak):
            print('fix: %s already exists - this file may already be converted. Nothing written.' % bak); return 2
        shutil.copy2(path, bak)
        print('backed up the original to %s' % bak)
        outp = path
    src = io.open(path, encoding='utf-8', errors='replace', newline='').read()
    todo = []
    own = local_defs(src)
    res = [fix_line(M, l, i, todo, own) if ok else l for i, l, ok in live_lines(src)]
    text = '\n'.join(res)
    if outp: io.open(outp, 'w', encoding='utf-8', newline='').write(text)
    done = [t for t in todo if t[2] == 'DONE']
    rest = [t for t in todo if t[2] != 'DONE']
    print('%s: %d rewritten mechanically, %d left to do%s' % (path, len(done), len(rest),
                                                              (' -> wrote %s' % outp) if outp else ' (dry run: pass -o to write)'))
    for n, old, st, how in done: print('  line %-5d DONE      %-40s %s' % (n, old, how))
    for n, old, st, how in rest: print('  line %-5d %-9s %-40s %s' % (n, st, old, how))
    return 0

# ------------------------------------------------------------------ sweep / coverage
def files_of(paths):
    for p in paths:
        if os.path.isdir(p):
            for root, _, fs in os.walk(p):
                for f in fs:
                    if f.lower().endswith(('.iss', '.inc', '.json')): yield os.path.join(root, f)
        else:
            yield p

BUILT = {}     # button command text -> the commands its migration form names (lowercase)
EMPTY = []     # buttons with a label and no command - clicking them does nothing

def units(f, text):
    """(where, text, is_live) for every scannable unit. A .json file (an MCP button file is ONE minified line)
    is walked value by value - every string is its own unit, located by its JSON path - so the second
    `oc !c` on a line is never hidden behind the first. Anything else: line by line."""
    if f.lower().endswith('.json'):
        try:
            doc = json.loads(text)
        except ValueError:
            doc = None
        if doc is not None:
            out = []
            # a button file: only `command` values are code - labels (`name`) and the saved form (`build`) are not
            only_cmd = '"command"' in text
            def walk(v, at):
                if isinstance(v, dict):
                    if isinstance(v.get('name'), str) and at: at = '%s{%s}' % (at, v['name'])
                    for k, x in v.items():
                        if only_cmd and k in ('build', 'name'): continue
                        walk(x, '%s.%s' % (at, k) if at else k)
                elif isinstance(v, list):
                    for n, x in enumerate(v): walk(x, '%s[%d]' % (at, n))
                elif isinstance(v, str) and v.strip() and (not only_cmd or at.endswith('.command')):
                    out.append((at, v, True))
            # the migration wrote a form (`build`) for the commands it rewrote - their argument order is the
            # new one already, so a WARN on them is noise; a button with no form was not rewritten
            def forms(v):
                if isinstance(v, dict):
                    if isinstance(v.get('build'), list) and isinstance(v.get('command'), str):
                        BUILT[v['command']] = {str(b.get('cmd', '')).lower() for b in v['build'] if isinstance(b, dict)}
                    for x in v.values(): forms(x)
                elif isinstance(v, list):
                    for x in v: forms(x)
            forms(doc)
            def empties(v, at):
                if isinstance(v, dict):
                    if isinstance(v.get('name'), str) and 'id' in v and not str(v.get('command') or '').strip():
                        EMPTY.append('%s{%s}' % (at, v['name']))
                    for k, x in v.items():
                        nm = v['name'] if isinstance(v.get('name'), str) and at else None
                        empties(x, '%s%s.%s' % (at, '{%s}' % nm if nm else '', k) if at else k)
                elif isinstance(v, list):
                    for n, x in enumerate(v): empties(x, '%s[%d]' % (at, n))
            if only_cmd: empties(doc, '')
            walk(doc, '')
            return out
    return list(live_lines(text))

def cmd_sweep(M, paths, coverage=False):
    bad = warn = n_files = n_hits = 0
    for f in files_of(paths):
        n_files += 1
        text = io.open(f, encoding='utf-8', errors='replace').read()
        own = local_defs(text)
        for i, line, ok in units(f, text):
            if not ok: continue
            spans = new_spans(M, line)
            if not coverage:
                for a, b, full, ok in spans:
                    n_hits += 1
                    if not ok:
                        bad += 1; print('%s:%s: BROKEN  %s does not exist in the new bot' % (f, i, full))
            for m, surf, sep, name, row in old_hits(M, line, spans):
                n_hits += 1
                if row is None:
                    bad += 1; print('%s:%s: UNKNOWN %s - the map has no row for it' % (f, i, m.group(0)))
                elif not coverage and row['status'] != 'unchanged':
                    bad += 1; print('%s:%s: OLD     %s [%s] -> %s' % (f, i, m.group(0), row['status'], row.get('howToFix')))
            for a, b, text, e in idiom_hits(M, line):
                n_hits += 1
                if e['status'] == 'unknown':
                    bad += 1; print('%s:%s: UNKNOWN %s - %s' % (f, i, text, e.get('howToFix'))); continue
                if coverage or e['status'] == 'unchanged': continue
                bad += 1; print('%s:%s: OLD     %s [%s] -> %s' % (f, i, text, e['status'], e.get('howToFix')))
            for oid, verdict, why in option_hits(M, line):
                n_hits += 1
                if coverage and verdict != 'unknown': continue    # coverage lists only what the map does not know
                bad += 1
                print('%s:%s: %s %s - %s' % (f, i, 'UNKNOWN' if verdict == 'unknown' else 'OLD    ', oid, why))
            for u, why, row in unknown_objects(M, line, own) + raw_commands(M, line):
                n_hits += 1
                if row and (coverage or row['status'] == 'unchanged'): continue
                bad += 1
                print('%s:%s: %s %s - %s' % (f, i, 'OLD    ' if row else 'UNKNOWN', u, why))
            for u in unmapped_hits(M, line, own):
                n_hits += 1
                fw = M.by_fw.get(u)
                if fw:
                    if not coverage and fw['status'] != 'unchanged':
                        bad += 1; print('%s:%s: OLD     %s [%s] -> %s' % (f, i, u, fw['status'], fw.get('howToFix')))
                    continue
                bad += 1
                print('%s:%s: UNKNOWN %s - a Classic global the map has no row for (%s)' % (f, i, u, M.unmapped[u]))
            for verb, quoted, _ in console_hits(M, line):
                n_hits += 1
                row = M.by_verb.get(verb.lower())
                if coverage:
                    if row is None and verb.lower() not in M.new_console:
                        bad += 1; print('%s:%s: UNKNOWN console %s' % (f, i, verb))
                    continue
                if quoted:
                    bad += 1; print('%s:%s: BROKEN  console command in quotes - the new console ignores the line' % (f, i))
                if verb.lower() not in M.new_console:
                    bad += 1; print('%s:%s: %s %s%s' % (f, i, 'OLD    ' if row else 'UNKNOWN', verb,
                                                         (' [%s] -> %s' % (row['status'], row.get('howToFix'))) if row else
                                                         ' - console verb not in the map or the new console (stop and ask)'))
                elif row and row['status'] in ('argOrder', 'signature') and \
                        not ({verb.lower(), (row.get('v2Row') or '').lower()} & BUILT.get(line, set())):
                    warn += 1; print('%s:%s: WARN    %s - its arguments changed; check them: %s' % (f, i, verb, row.get('note') or row.get('howToFix')))
                elif row and row['status'] == 'stub':
                    bad += 1; print('%s:%s: OLD     %s - accepted by the new console but does nothing yet' % (f, i, verb))
    if coverage:
        # coverage only asks "does the map know every name?" - never call an unconverted file CLEAN
        # counts Classic spellings only - a converted line drops out; quote the SWEEP's count in the report
        print('coverage: %d file(s), %d Classic name use(s) checked, %d unknown name(s)%s' % (
            n_files, n_hits, bad, ' - none unknown' if not bad else ' - each is a question'))
        return 1 if bad else 0
    for e in EMPTY:
        print('%s: NOTE    a button with a label and no command - clicking it does nothing (list it for the person)' % e)
    print('sweep: %d file(s), %d call(s) checked, %d unresolved, %d warning(s) -> %s' % (
        n_files, n_hits, bad, warn, 'CLEAN' if not bad else 'NOT CLEAN'))
    return 1 if bad else 0

# ------------------------------------------------------------------ sites (keep + list, never rewrite)
SITE_RULES = [
    ('R10  ', re.compile(r'\bMe\.Ability\[(?!\s*id\s*,)|\.To[A-Za-z]*Info\b', re.I),
     'an ISXEQ2 name lookup / .To*Info (asks the game server)'),
    ('R12  ', re.compile(r'\bEQ2:(?:QueryActors|GetActors)\b|\bCustomActorArray\b', re.I),
     'an actor scan'),
    # Actor[...] by anything but an id: an id is a number, `id,`, or a ${...ID}-style value
    ('R12  ', re.compile(r'\bActor\[(?!\s*(?:id\s*,|\d|\$\{[^}\]]*\bID\}\s*\]|\$\{[^}\]]*\bID\}\s*,|\$\{[^}\]]*(?:ID|Id|id)\}\s*\]))', re.I),
     'an actor search by name / query'),
    # ${X[${i}](exists)} as a loop guard: an out-of-range index on an ISXEQ2 array crashes the client
    ('INDEX', re.compile(r'[A-Za-z_][A-Za-z0-9_.]*\[\s*\$\{[A-Za-z_][A-Za-z0-9_]*\}\s*\]\(exists\)'),
     'an index tested with (exists) - out of range CRASHES the client; it needs a bound by the Count member'),
]

def cmd_sites(paths):
    n = 0
    for f in files_of(paths):
        for i, line, ok in units(f, io.open(f, encoding='utf-8', errors='replace').read()):
            if not ok: continue
            for tag, rx, what in SITE_RULES:
                if rx.search(line):
                    n += 1; print('%s:%s: %s %s | %s' % (f, i, tag, what, line.strip())); break
    print('sites: %d line(s) to keep as they are and list in the report' % n)
    return 0

def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0], epilog=__doc__.split('\n', 1)[1],
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('cmd', choices=['lookup', 'fix', 'sweep', 'coverage', 'sites'])
    ap.add_argument('args', nargs='*', help='lookup: names; fix: one file; sweep / coverage / sites: files or folders')
    ap.add_argument('-o', '--out', help='fix: write the converted file here (without -o or --in-place, fix only prints)')
    ap.add_argument('--map', help='conversion-map.json to use (default: beside this tool)')
    ap.add_argument('--in-place', action='store_true',
                    help='fix: keep the name - copy the original to <file>.classic.iss, convert <file>.iss')
    if any(x in ('-h', '--help') for x in sys.argv[1:3]):
        ap.print_help(); return 0           # `lookup --help` / `fix --help` too, not just the bare tool
    if len(sys.argv) > 2 and sys.argv[1] == 'lookup':
        # every word after `lookup` is a NAME - `-ofol-++` is a console verb, not the -o option
        names, mp, rest = [], None, sys.argv[2:]
        while rest:
            x = rest.pop(0)
            if x == '--map' and rest: mp = rest.pop(0)
            elif x != '--': names.append(x)
        cmd_lookup(Map(find_map(mp)), names); return 0
    a, extra = ap.parse_known_args()        # console verbs start with '-' (lookup -RunWalk)
    a.args = a.args + [x for x in extra if x not in ('-o', '--out', '--map', '--in-place')]
    M = Map(find_map(a.map))
    if a.cmd == 'lookup': cmd_lookup(M, a.args); return 0
    if a.cmd == 'fix': return cmd_fix(M, a.args[0], a.out, a.in_place)
    if a.cmd == 'sites': return cmd_sites(a.args)
    return cmd_sweep(M, a.args, coverage=(a.cmd == 'coverage'))

if __name__ == '__main__':
    sys.exit(main())

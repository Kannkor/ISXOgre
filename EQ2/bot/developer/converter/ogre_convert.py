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

#INCLUDE FILES - the script's own include files come along:
    fix (dry run), sweep, coverage, sites   FOLLOW them by default (--no-follow-includes to stop)
    fix -o / fix --in-place                 only with --follow-includes - they WRITE, so you ask for it:
        fix main.iss --in-place --follow-includes   every file gets its own <file>.classic.iss backup
        fix main.iss -o <folder> --follow-includes  -o is a FOLDER: each file is written there at its place
                                                    under the Scripts folder (or under main.iss's folder)
  How a path is read (LavishScript): `#include "x.iss"` - a plain name - is in the MAIN file's folder (the
  script that was run), even when the line is inside another include; ${Script.CurrentDirectory} is that
  same folder; ${LavishScript.HomeDirectory} is the folder that holds Scripts. NOT followed, and said so:
  Classic's own files (EQ2OgreBot, OgreCommon, ... - sweep tells you to remove those #includes), anything
  outside the Scripts folder, a file that is not there, and a ${...} the tool cannot work out.

Needs only Python 3 and conversion-map.json (same folder, or --map <path>). It reads no bot source, so it
runs anywhere the map has been copied to. Open source, like the map.

WHAT `fix` REWRITES - and nothing else:
  * an old call whose map row says `moved` / `renamed` with the same arguments: the call is swapped,
    the arguments are left exactly as they were;
  * an old call whose ONLY change is "the for-who is now argument 0" on an object that acted on its own
    session (every Ogre_CampSpot / Obj_* / OgreBotAPI method that had no for-who): `all` is inserted
    first - a script's own call only ever runs on the session running it, so that is what the old call did;
  * THE FOR-WHO: every rewritten call whose new form takes a for-who gets one (the map row's `forWhoInsert`):
    a call that passed no arguments at all leaned on the old default, which is written out
    (`OgreBotAPI:Jump` -> `OgreBotAPI.Movement:Jump[all]`); a call that passed arguments already passed its
    for-who first, and keeps it;
    (all of the above only when the call passes every argument the new form requires - a call that leaves
    one off or blank is a TO-DO instead: the new verb refuses it);
  * a console verb that was renamed with the same arguments; and one renamed whose only change is the for-who
    the new verb takes first: `auto` is written after it (`-Door 2` -> `-ZoneDoor auto 2` - the line's -cfw or
    the For Who window decides). A verb that kept its name gains `auto` only when its first argument cannot be a
    for-who (a plain number, or quoted text with a space: `-ZoneDoor 1` -> `-ZoneDoor auto 1`); any other first
    argument stays a to-do (it may already be the for-who), and a line it converted is not touched again;
  * a console row that kept its name but lost arguments off its end: the words it no longer reads are dropped
    (`-AutoCurse <fw> <toon> AutoRemove 20` -> `-AutoCurse <fw> <toon>`); -Invite with TRUE becomes -RaidInvite and
    -RaidInvite with FALSE becomes -Invite; `-LogToonIn auto <character>` becomes `-LogToonIn <character> <character>`,
    and so does `-LoginAtCharacterSelect <fw> <character>`;
  * a Classic framework variable renamed to a plain member: `${OgreRelayGroup}` (and `${OgreRelayGroup.Length}`
    etc.) becomes `${ISXOgreEQ2.Auth.RelayGroup}` - the same text under its new name.
Everything else - argument reorders, changed arguments, data-file moves, not-ported names - is left in
place and listed as a TO-DO with the map's how-to-fix line. So is a FUNCTION-FORM call
(`call OgreBotAPI.DestroyItem "Rusty Key" 3`): the new bot has no function to call, so its to-do says to write
the new form with the call's arguments inside its brackets. A person (or Claude, following the
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
        self.OC = CONSOLE_LINE
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
            params = list(M.con_params.get(tl, []))
            row = M.by_verb.get(tl)
            if row and i < n and console_kept_forwho(M, row, t, toks[i][0]) == 'insert':
                # a kept-name verb still in its Classic shape (no for-who yet): walk it as Classic - without the
                # for-who - or its Classic argument count would swallow the next command (`-ZoneDoor 1 -OptNum 3`)
                params = [p for k, p in enumerate(params) if k != next((j for j, q in enumerate(params) if q[0] == 'forwho'), -1)]
            for typ, allp in params:
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

# ------------------------------------------------------------------ the commands a line RUNS (one parser)
# A Classic line often runs its command through a WRAPPER, and wrappers nest (`timedcommand 5 relay all ogre console`).
# Each wrapper the Classic scripts really use is peeled to the command it carries, and that command is read exactly
# like a line of its own - `relay all ogre bookcase` says what `ogre bookcase` says. The wrapper stays as written.
#   relay <target> <command>                           relay all ogre dev / relay ${OgreRelayGroup} ogre reloadbot
#   timedcommand [<delay>] <command>                   timedcommand 5 relay all ogre console (a delay: a number or ${...})
#   squelch <command> / execute <command>
#   oc|irc !c|!ci -OgreCommandOB_AP <who> <words>      runs `ogre <words>` for <who>: oc !ci -OgreCommandOB_AP igw:${Me.Name} end qh
#   oc|irc !c|!ci -RawCommandOB_AP <who> <command>     runs <command> for <who> (so does -RawCommandRequiresOgreBot_AllParams,
#                                                      and the new console's -RawCommand, the same shape)
# A carried command that is ONE quoted string is that string unquoted, an escaped quote (`\"`) inside it read as a
# quote: `relay all "ogre bookcase"`, `relay all "oc !c -RawCommandOB_AP all \"ogre bookcase\""`.
# On a line that is not a console line, a "quoted string" that is itself a command counts too, peeled the same way
# (`_TempCode:Set["ogre ..."]`, `TimedCommand 10 "ogre end im"`). A console line's quoted text is a verb's argument.
CONSOLE_LINE = re.compile(r'(?:\b(?:oc|irc)\s+|^\s*)!(?:ci?|command)\b\s*(.*)$', re.I)
CONSOLE_BANG = re.compile(r'^!(?:ci?|command)$', re.I)
CONSOLE_ROUTE = ('-cfw', '-tab', '-rg')
WRAP_PLAIN = ('squelch', 'execute', 'run', 'runscript')
CARRY_OGRE = ('-ogrecommandob_ap',)
CARRY_RAW = ('-rawcommandob_ap', '-rawcommandrequiresogrebot_allparams', '-rawcommand')
QUOTED = re.compile(r'"((?:[^"\\]|\\.)*)"')
DELAY = re.compile(r'^(?:\d+(?:\.\d+)?|\$\{.*\})$')

def tokens(text):
    """-> [(word, start)] a command line's words: whitespace splits them, except inside "quoted text" (an escaped `\\"`
    does not end it) or a [...] / {...} (a ${...} with spaces in it is one word)."""
    out, i, n = [], 0, len(text)
    while i < n:
        if text[i].isspace():
            i += 1; continue
        s, depth, quoted = i, 0, False
        while i < n:
            c = text[i]
            if quoted:
                if c == '\\' and i + 1 < n:
                    i += 2; continue
                quoted = c != '"'
            elif c == '"':
                quoted = True
            elif c in '[{':
                depth += 1
            elif c in ']}':
                depth = max(0, depth - 1)
            elif c.isspace() and depth == 0:
                break
            i += 1
        out.append((text[s:i], s))
    return out

def unquote(text):
    """The text, or - when the whole text is ONE quoted string - its inside, `\\"` read as `"`."""
    t = text.strip()
    if len(t) >= 2 and t[0] == '"' and t[-1] == '"' and len(tokens(t)) == 1:
        return t[1:-1].replace('\\"', '"')
    return t

def carried(cmd):
    """The command a wrapper line carries (see above), or None when `cmd` is not a wrapper."""
    tk = tokens(cmd)
    if not tk: return None
    w, k = tk[0][0].lower(), None
    if w == 'relay':
        k = 2
    elif w == 'timedcommand':
        k = 2 if len(tk) > 1 and DELAY.match(tk[1][0]) else 1
    elif w in WRAP_PLAIN:
        k = 1
    elif w in ('oc', 'irc') or CONSOLE_BANG.match(w):
        i = 0 if CONSOLE_BANG.match(w) else 1
        if i >= len(tk) or not CONSOLE_BANG.match(tk[i][0]): return None
        i += 1
        while i < len(tk) and tk[i][0].lower() in CONSOLE_ROUTE: i += 2          # the new console's routing flags
        while i < len(tk) and not tk[i][0].startswith('-'): i += 1             # a stray word (`irc !c <dest>`)
        if i + 2 >= len(tk) or tk[i][0].lower() not in CARRY_OGRE + CARRY_RAW: return None
        inner = unquote(cmd[tk[i + 2][1]:])                                      # after the verb and its <who>
        return ('ogre ' + inner) if tk[i][0].lower() in CARRY_OGRE else inner
    if k is None or k >= len(tk): return None
    return unquote(cmd[tk[k][1]:])

def commands_run(line, depth=0):
    """-> every command `line` runs, outermost first: the line itself, then what each wrapper carries, then (not on a
    console line) each quoted string's commands. Bounded: a wrapper carries one command, and 8 levels is far past
    anything written."""
    out, cmd = [], line.strip()
    for _ in range(8):
        if not cmd or cmd in out: break
        out.append(cmd)
        cmd = carried(cmd)
        if cmd is None: break
    if depth < 3 and not any(c.split(None, 1)[0].lower() == 'echo' for c in out):      # echo only prints its quotes
        for c in list(out):
            if CONSOLE_LINE.search(c): continue
            for q in QUOTED.finditer(c):
                for x in commands_run(q.group(1).replace('\\"', '"'), depth + 1):
                    if x not in out: out.append(x)
    return out

# `ogre <word>` at the START of a command the line runs (commands_run). The `ogre` keyword is lowercase - `echo "Ogre
# will ..."` is prose. The WORD (and `end`) is any case, read folded: Classic's `ogre` command lowercased its first two
# words before matching them (ISXOgre CMD_EQ2OgreLoader), so `ogre TransmuteSalvageExtractIt` ran `transmutesalvageextractit`.
OGREWORD = re.compile(r'^ogre(\s+(?i:end))?\s+([A-Za-z][A-Za-z0-9_]*)')
OLDEXT = re.compile(r'\bext\s+(?:-unload\s+)?isxogre(?![A-Za-z0-9])', re.I)

def same_word_changed(row, args):
    """Did this line of a word the new bot kept change? `row` is its map row (None: nothing changed), `args` what follows
    the word. Read case-blind: Classic's `ogre` lowercased the word, and flags are written both ways."""
    if row is None: return False
    return not row.get('changedArgs') or bool(re.search(row['changedArgs'], args.strip(), re.I))

def raw_commands(M, line):
    """-> [(text, why)] raw bot commands a button or script types: `ogre <word>` the new bot has no such
    word for, a word the new bot kept whose arguments or job changed, and loading / unloading the OLD extension. Every
    command the line runs is read (commands_run), so a word inside `relay all ...`, `timedcommand ...` or
    `oc !c -RawCommandOB_AP <who> ...` is seen; each word once."""
    out, seen = [], set()
    for c in commands_run(line):
        m = OGREWORD.match(c)
        if not m: continue
        w = m.group(2).lower()
        if w in seen or not M.new_ogre: continue
        fw = M.by_fw.get('ogre ' + w)
        # A word the new bot kept is answered only by a row of its own, and `ogre end <word>` still ends it. The row's
        # `changedArgs`, when it has one, says which lines changed (`ogre craftingmats -sig` is fine, a bare one is not).
        if w in M.new_ogre and (m.group(1) or not same_word_changed(fw, c[m.end():])): continue
        seen.add(w)
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

# ------------------------------------------------------------------ #include (the script's own include files)
# Follow a script's own #include files and convert them in the same run. How LavishScript reads an
# include path: a plain `#include "x.iss"` is in the MAIN file's folder - the script that was run - even
# when the line sits inside another include file. ${Script.CurrentDirectory} is that same folder.
HOME_TOKEN   = re.compile(r'\$\{LavishScript\.HomeDirectory\}', re.I)
CURDIR_TOKEN = re.compile(r'\$\{Script\.CurrentDirectory\}', re.I)

def scripts_home(path):
    """The LavishScript home: the folder that holds the `Scripts` folder `path` sits in. None when it is in none."""
    p = os.path.dirname(os.path.abspath(path))
    while True:
        d, base = os.path.split(p)
        if base.lower() == 'scripts': return d
        if not base or d == p: return None
        p = d

def same_file_key(path):
    return os.path.normcase(os.path.abspath(path))

def resolve_include(spec, main_file):
    """-> (path, None) for an include to follow, or (None, why) for one that is not followed."""
    s = spec.strip().strip('"').strip()
    main_dir = os.path.dirname(os.path.abspath(main_file))
    home = scripts_home(main_file)
    if HOME_TOKEN.search(s):
        if not home: return None, 'uses ${LavishScript.HomeDirectory}, but %s is not inside a Scripts folder' % main_file
        s = HOME_TOKEN.sub(lambda m: home.replace('\\', '/'), s)
    s = CURDIR_TOKEN.sub(lambda m: main_dir.replace('\\', '/'), s)
    if '${' in s: return None, 'a ${...} in the path the tool cannot work out'
    if not os.path.isabs(s): s = os.path.join(main_dir, s)      # a plain name: the MAIN file's folder
    s = os.path.normpath(s)
    if CLASSIC_TREES.search(s): return None, 'a Classic file - not yours to convert (sweep says to remove this #include)'
    if home:
        root = os.path.join(home, 'Scripts')
        if not same_file_key(s).startswith(same_file_key(root) + os.sep): return None, 'outside the Scripts folder'
    if not os.path.isfile(s): return None, 'not found: %s' % s
    return s, None

def include_tree(main_file, seen=None):
    """-> (files, skipped): main_file first, then every include it reaches, each ONCE (a file two others include, or
    two that include each other); skipped = [(file, line, spec, why)] for the includes not followed."""
    seen = set() if seen is None else seen
    files, skipped = [], []
    if same_file_key(main_file) in seen: return files, skipped
    seen.add(same_file_key(main_file)); files.append(main_file)
    i = 0
    while i < len(files):
        f = files[i]; i += 1
        try:
            text = io.open(f, encoding='utf-8', errors='replace').read()
        except (IOError, OSError):
            continue
        for n, l, ok in live_lines(text):
            if not ok: continue
            m = INCL.match(l)
            if not m: continue
            got, why = resolve_include(m.group(1), main_file)
            if got is None:
                skipped.append((f, n, m.group(1).strip().strip('"'), why)); continue
            if same_file_key(got) not in seen:
                seen.add(same_file_key(got)); files.append(got)
    return files, skipped

def say_skipped(skipped):
    for f, n, spec, why in skipped:
        print('%s:%s: INCLUDE %s - not followed: %s' % (f, n, spec, why))

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
FW_DONE = ' with `%s` as the for-who'

def function_form_todo(nf, shape):
    """The to-do's first words for a FUNCTION-FORM call - `call OgreBotAPI.DestroyItem "Rusty Key" 3`.
    `fix` never rewrites one: the new bot has no function to `call`, and the arguments after the name are the Classic
    FUNCTION's, space-separated (a Classic function's parameters are not always its method's: DestroyItem's function
    has no for-who, OpenAndBuyFromMerchant's does), so the new form's argument count proves nothing about the call. The
    writer moves them into the new form's brackets. A method is written as a call, a member as a `${...}` read; a new
    form that takes a for-who first (`[fw, ...]`) gets one unless the call already passes it."""
    lead = 'a function-form call (`call ...`) is never rewritten - the new bot has no function to call. '
    if not re.match(r'^[A-Za-z_][A-Za-z0-9_]*(?:[.:][A-Za-z0-9_]+)+$', nf or ''): return lead
    form = ('`%s[...]`' if ':' in nf else '`${%s[...]}`') % nf
    fw = bool(re.match(r'^\[\s*(?:fw|forwho)\b', shape or '', re.I))
    return lead + 'Write %s in its place, with this call\'s arguments inside the brackets, comma-separated%s. ' % (
        form, ' - the for-who first (`all` unless the call already passes one)' if fw else '')

def with_forwho(fwi, after):
    """THE for-who rule of a rewrite: the map row's `forWhoInsert` says what a converted call must gain - the map's
    generator decides it once, from the two signatures. `after` is the line just past the old name.
    -> (text to write after the new name, characters of `after` it replaces).
      when `always`  the old call had no for-who: the value goes in front of whatever it passes (`[all,` / `[all]`)
      when `noArgs`  the old for-who was already argument 0: only a call passing NOTHING gains it (`X` / `X[]` -> `X[all]`);
                     a call passing anything passes its for-who already
    A script call gains `all` (it only ever runs on the session running it) or the old declared default; a console line
    gains `auto` (console_forwho)."""
    v = (fwi or {}).get('value')
    if not v: return '', 0
    if after.startswith('[]'): return '[%s]' % v, 2
    if after.startswith('['): return ('[%s,' % v, 1) if fwi['when'] == 'always' else ('', 0)
    return '[%s]' % v, 0

def console_forwho(M, row, verb):
    """The console half: a Classic verb whose only change is the for-who the new console puts first (forWhoInsert, value `auto`) is rewritten
    to the new spelling with `auto` after it - ONLY when the spelling changes (`-Door 2` -> `-ZoneDoor auto 2`). A verb
    that keeps its name is console_kept_forwho's."""
    fwi = row.get('forWhoInsert') or {}
    nf = row.get('newForm') or ''
    if fwi.get('when') != 'always' or not fwi.get('value') or not nf.startswith('-') or nf.lower() == verb.lower() \
            or nf.lower() not in M.new_console:
        return None
    return nf + ' ' + fwi['value']

def _drop_lsvars(text):
    """`text` with every ${...} taken out (braces nest; an unclosed one runs to the end) - what is left is what the line
    says literally, whatever the variables expand to."""
    out, depth, i = [], 0, 0
    while i < len(text):
        if text.startswith('${', i):
            depth += 1; i += 2; continue
        if depth and text[i] == '{': depth += 1
        elif depth and text[i] == '}': depth -= 1
        elif not depth: out.append(text[i])
        i += 1
    return ''.join(out)

def not_a_forwho(tok):
    """True when a console argument CANNOT be a for-who, by the bot's for-who grammar:
      a plain number    the grammar reads a bare number as an actor id - a value that changes every time the actor
                        zones, so it is never written into a script (and no EQ2 toon name is a number);
      quoted text with a space (outside any ${...})   the grammar has no space combinator: a for-who with a space
                        in it matches nobody, so nobody writes one.
    Anything else - a word, a ${...}, `auto`, `all`, `igw:...` - may be a for-who: a word is a toon or session name to
    the grammar, so it is never guessed."""
    if re.fullmatch(r'[0-9]+', tok): return True
    return len(tok) >= 2 and tok[0] == '"' and tok[-1] == '"' and bool(re.search(r'\s', _drop_lsvars(tok[1:-1])))

def console_first_arg(line, end):
    """The first argument token after a console verb that ends at line[end] - the way console_hits() splits a line
    (`"quoted text"` or a run of non-blanks) - or '' when none follows."""
    m = re.match(r'\s+("[^"]*"?|\S+)', line[end:])
    return m.group(1) if m else ''

def console_kept_forwho(M, row, verb, first):
    """The console half for a verb that KEPT its name and only gained the for-who the new console puts first (forWhoInsert `auto`,
    always; -ImmRes, -ZoneDoor, -Mentor, -ApplyVerb, -Raid, -EndScript). -> 'insert' (write `auto` before `first`),
    'converted' (`first` is the `auto` a converter writes - a Classic line never had one there: Classic read `auto` only as a
    for-who), or None (a to-do, as before).
    It inserts only when `first` cannot be a for-who (not_a_forwho): `-ZoneDoor 1` -> `-ZoneDoor auto 1`,
    `-ApplyVerb "a worn monument" "Polish Monument"` -> `-ApplyVerb auto "a worn monument" ...`. A word or a ${...}
    first (`-Mentor Bob`, `-ZoneDoor "${UserInput}"`) may already be the line's for-who, so it is the writer's.
    IDEMPOTENT by construction: the `auto` it writes is not a not_a_forwho token, so a second `fix` reads the converted
    line as converted and adds nothing; and a line someone converted by hand starts with its for-who, which is never
    a not_a_forwho token either."""
    fwi = row.get('forWhoInsert') or {}
    nf = row.get('newForm') or ''
    if fwi.get('when') != 'always' or fwi.get('value') != 'auto' or nf.lower() != verb.lower() \
            or nf.lower() not in M.new_console:
        return None
    if first.lower() == 'auto' or first.lower().startswith('auto+'): return 'converted'
    return 'insert' if not_a_forwho(first) else None

def call_args(line, at):
    """The top-level arguments of the `[...]` that opens at line[at] (each stripped), or None when it does not close
    on this line. Brackets, braces and "quoted text" nest; only a comma at the call's own level splits."""
    args, cur, depth, quoted = [], [], 0, False
    for i in range(at, len(line)):
        c = line[i]
        if quoted:
            quoted = c != '"'
        elif c == '"':
            quoted = True
        elif c in '[{':
            depth += 1
            if depth == 1: continue
        elif c in ']}':
            depth -= 1
            if depth == 0:
                args.append(''.join(cur).strip())
                return [] if args == [''] else args
        elif c == ',' and depth == 1:
            args.append(''.join(cur).strip()); cur = []; continue
        cur.append(c)
    return None

# Console rows that KEPT their name but lost arguments off their END (2026-11-10): a Classic line that still passes them
# is rewritten, by the same rules the bot uses when it converts a saved MCP button (test_ogre_convert_rewrites.py holds the
# two tables together). `kept` = the parameters the row has now, one letter each ('f' a for-who, 'v' a value, 'r' every word up to the next command); `dropped` = the ones it
# lost. 'b' is -Invite's / -RaidInvite's raid word: TRUE (or 1) picks -RaidInvite, FALSE (or 0) -Invite.
DROPPED_TAILS = {
    '-checkmounttraining':   ('f',  'v'),    # forcecheck - the force is retired
    '-f2pwindow_setoptions': ('f',  'v'),    # option
    '-invite':               ('fv', 'b'),
    '-raidinvite':           ('fv', 'b'),
    '-tempadorns':           ('fv', 'v'),    # overwrite - Apply always applies
}

def _unq(t):
    return t[1:-1] if len(t) >= 2 and t[0] == '"' and t[-1] == '"' else t

def _ends_values(t):
    """A word that ends a row's values: any -word (a row, a reserved word), as the MCP button conversion reads it."""
    return bool(re.match(r'^-[A-Za-z]', _unq(t)))

def _read_values(toks, i, kinds):
    """The index past the values `kinds` reads from toks[i] on, the way the console reads them."""
    for k in kinds:
        if k == 'f':
            if i < len(toks) and not _unq(toks[i]).startswith('-'): i += 1
        elif k == 'r':
            while i < len(toks) and not _ends_values(toks[i]): i += 1
            if i < len(toks) and _unq(toks[i]).lower() == '-endargs': i += 1
        elif i < len(toks) and not _ends_values(toks[i]):
            i += 1
    return i

# -AutoCurse / -AutoCure / -AutoGroupCure read Classic's request words again, as new-form options. The bot applies the SAME
# translation to a saved MCP button (test_ogre_convert_rewrites.py runs both through the same cases). `words` = the words after the for-who (-AutoGroupCure: Classic's toon word first, which was only a tag) or after the
# victim (-AutoCurse, -AutoCure). -> (new words, notes) or None when a word is not understood: the line is left as it is
# and the row refuses it by naming the word - never a guess (a wrong cure can kill).
#   AutoRemove N -> -AutoRemove N      AutoRemoveMS N -> -AutoRemove ceil(N/1000)      CustomFlag X -> -tag X
#   a e n t / arcane elemental noxious trauma -> the kind (-AutoCure, -AutoGroupCure); curse stays a kind on -AutoCure only
#   aX 3 / arcaneX 3 ... -> the kind; on -AutoGroupCure the number is -count, when every kind named has the same one
#   any -> no kinds      exclusive only DirectTarget TRUE (and curse on -AutoCurse / -AutoGroupCure) -> dropped
CURE_KINDS = ('arcane', 'elemental', 'noxious', 'trauma')
CURE_KIND_WORDS = {'a': 0, 'arcane': 0, 'e': 1, 'elemental': 1, 'n': 2, 'noxious': 2, 't': 3, 'trauma': 3}
CURE_VERBS = {'-autocurse': 'curse', '-autocure': 'cure', '-autogroupcure': 'group'}

def _whole(v, lo, hi):
    return int(v) if re.fullmatch(r'[0-9]{1,9}', v) and lo <= int(v) <= hi else None

def cure_words(verb, words):
    count = [0, 0, 0, 0]; order = []; anyw = curse = False
    seconds = ms = 0; toon_tag = flag_tag = ''; notes = []
    p = 0
    while p < len(words):
        raw = words[p]; word = _unq(raw); lw = word.lower()
        if verb == 'group' and p == 0:
            if word and lw != 'notsupplied': toon_tag = raw
            p += 1; continue
        if lw in ('exclusive', 'only', 'directtarget', 'true'):
            if lw in ('exclusive', 'only') and verb == 'cure':
                notes.append('`%s` is gone: it cured that one kind with /cureplayer, which the new -AutoCure never uses - the kind '
                             'words alone narrow it' % word)
            p += 1; continue
        if lw == 'any': anyw = True; p += 1; continue
        if lw == 'curse':
            if verb == 'cure': curse = True
            p += 1; continue
        if lw in ('autoremove', 'autoremovems'):
            if p + 1 >= len(words): return None
            n = _whole(_unq(words[p + 1]), 1 if lw == 'autoremove' else 0, 600 if lw == 'autoremove' else 600000)
            if n is None: return None
            if lw == 'autoremove': seconds = n
            else: ms = n
            p += 2; continue
        if lw == 'customflag':
            if p + 1 >= len(words) or not _unq(words[p + 1]): return None
            f = words[p + 1]
            if flag_tag and flag_tag != f: return None
            flag_tag = f; p += 2; continue
        base = lw[:-1] if lw.endswith('x') and lw[:-1] in CURE_KIND_WORDS else lw
        if base not in CURE_KIND_WORDS or verb == 'curse': return None   # a kind means nothing to a curse call: not guessed
        k = CURE_KIND_WORDS[base]; n = 1
        if base != lw:
            if p + 1 >= len(words): return None
            n = _whole(_unq(words[p + 1]), 1, 6)
            if n is None: return None
            p += 1
        if count[k] == 0: order.append(k)
        count[k] += n
        p += 1
    if anyw and order: return None                                  # `any` beside named kinds: which wins is the writer's call
    life = (ms + 999) // 1000 if ms > 0 else seconds
    if ms > 0 and life < 1: life = 1
    if life > 600: return None
    tag = toon_tag
    if flag_tag:
        if tag and tag != flag_tag: return None
        tag = flag_tag
    gcount = 1
    if verb == 'group' and order:
        if any(count[k] != count[order[0]] for k in order): return None   # unequal thresholds: the writer's call
        gcount = count[order[0]]
    kinds = [CURE_KINDS[k] for k in order] + (['curse'] if curse else [])
    out = []
    if verb == 'group':
        # options first: a first word that is a -word is how the console (and this function) tell the new form from Classic's toon word
        if tag: out += ['-tag', tag]
        if life: out += ['-AutoRemove', str(life)]
        if gcount > 1 or (kinds and not out): out += ['-count', str(gcount)]
        out += kinds
    else:
        out += kinds
        if life: out += ['-AutoRemove', str(life)]
        if tag: out += ['-tag', tag]
    return out, notes

def _cure_span(toks, i, verb):
    """(from, to) - the Classic words of the cure row at toks[i], read the way the console reads them."""
    fw = _read_values(toks, i + 1, 'f')
    start = fw if verb == 'group' else _read_values(toks, fw, 'v')
    return start, _read_values(toks, start, 'r')

def call_end(line, at):
    """The index just past the `]` that closes the `[...]` opening at line[at], or None when it does not close on this line
    (the same nesting call_args reads)."""
    depth, quoted = 0, False
    for i in range(at, len(line)):
        c = line[i]
        if quoted: quoted = c != '"'
        elif c == '"': quoted = True
        elif c in '[{': depth += 1
        elif c in ']}':
            depth -= 1
            if depth == 0: return i + 1
    return None

# The Classic calls that take the same request words, by map row id -> the verb translation they use.
CURE_API = {'OgreBotAPI:AutoCurse': 'curse', 'OgreBotAPI:Cursed': 'curse', 'OgreBotAPI:AutoCure': 'cure',
            'OgreBotAPI:AutoGroupCure': 'group'}

def cure_api_call(row, line, m):
    """`OgreBotAPI:AutoGroupCure["all","Flora_Oozing"]` -> `OgreBotAPI.Cures:RequestGroupWatch["all","-tag","Flora_Oozing"]`: a call
    that passes Classic's request words after its victim (a group cure: after its for-who) is written with the words the new
    method reads (cure_words). -> (new text, span end, notes) | 'asis' (nothing after the victim, or a `${...}` word the tool
    cannot read: the ordinary rename applies) | None (a literal word it does not understand: the writer's)."""
    verb = CURE_API.get(row['id'])
    if not verb or line[m.end():m.end() + 1] != '[': return 'asis'
    end = call_end(line, m.end())
    args = call_args(line, m.end())
    if end is None or args is None: return 'asis'
    fixed = 1 if verb == 'group' else 2
    words = args[fixed:]
    if not words or any('${' in a for a in words): return 'asis'
    r = cure_words(verb, words)
    if r is None: return None
    new, notes = r
    if verb == 'group' and len(args) <= 1: return 'asis'
    q = lambda t: t if t.startswith('"') or t in words else '"%s"' % t
    return '%s[%s]' % (row['newForm'], ','.join(args[:fixed] + [q(t) for t in new])), end, notes

def console_changed_rows(line, n, todo):
    """A console line's rows whose ARGUMENTS changed (DROPPED_TAILS, -LogToonIn, -LoginAtCharacterSelect), rewritten to
    what the row reads now. -> the line. Every rewrite is a DONE; a raid word the tool cannot read (a ${...}) is a to-do.
    A line already in the new shape is left alone, so a second `fix` adds nothing. A command in quotes is not touched
    (console_hits() reports it)."""
    m = CONSOLE_LINE.search(line)
    if not m: return line
    spans = [[t.group(0), m.start(1) + t.start(), m.start(1) + t.end()] for t in re.finditer(r'"[^"]*"?|\S+', m.group(1))]
    if any(re.match(r'^"\s*-[A-Za-z]', s[0]) for s in spans): return line
    toks = [s[0] for s in spans]
    edits = []                                     # (start, end, text) on the line, applied right to left
    i = 0
    while i < len(toks):
        w = toks[i]; wl = w.lower()
        if wl in CURE_VERBS:
            verb = CURE_VERBS[wl]
            a, b = _cure_span(toks, i, verb)
            words = toks[a:b]
            if words and _unq(words[-1]).lower() == '-endargs': words = words[:-1]
            r = cure_words(verb, words) if words else None
            if words and r is None:
                todo.append((n, toks[i], 'signature', 'a word after it is not one the new row reads - nothing was changed, and the row refuses '
                             'the request naming that word. Classic\'s request words are now: kinds (a e n t, arcane elemental noxious '
                             'trauma), -AutoRemove <seconds>, -tag <name>, and on -AutoGroupCure -count <n>. exclusive, only, DirectTarget and '
                             'TRUE are gone. A group cure whose kinds had different thresholds (aX 3 eX 1) needs one -AutoGroupCure each.'))
            elif r is not None and r[0] != words:
                if r[0]: edits.append((spans[a][1], spans[b - 1][2], ' '.join(r[0])))
                else: edits.append((spans[a - 1][2], spans[b - 1][2], ''))
                todo.append((n, toks[i], 'DONE', '-> %s' % (' '.join([toks[i]] + toks[i + 1:a] + r[0])) + ''.join(' (%s)' % x for x in r[1])))
            i = max(b, i + 1); continue
        if wl in DROPPED_TAILS:
            kept, dropped = DROPPED_TAILS[wl]
            a = _read_values(toks, i + 1, kept); b = _read_values(toks, a, dropped)
            if b > a:
                gone = ' '.join(toks[a:b])
                if dropped == 'b':
                    v = _unq(toks[a])
                    if '${' in v:
                        todo.append((n, w, 'signature', 'its last word (%s) picks the row now: TRUE is `-RaidInvite`, '
                                     'FALSE is `-Invite` - write that row and drop the word.' % v))
                        i = b; continue
                    if wl == '-invite' and (v.upper() == 'TRUE' or v == '1'):
                        edits.append((spans[i][1], spans[i][2], '-RaidInvite')); w = '-RaidInvite'
                    elif wl == '-raidinvite' and (v.upper() == 'FALSE' or v == '0'):
                        edits.append((spans[i][1], spans[i][2], '-Invite')); w = '-Invite'
                edits.append((spans[a - 1][2], spans[b - 1][2], ''))
                todo.append((n, toks[i], 'DONE', '-> %s, without `%s` (the row no longer reads it)' % (w, gone)))
            i = max(b, i + 1); continue
        if wl == '-logtoonin':
            # Its first word names the BOX. `auto` (or "") names none: the character it logs in is the box.
            if i + 2 < len(toks) and not _ends_values(toks[i + 1]) and not _ends_values(toks[i + 2]):
                box, toon = _unq(toks[i + 1]), _unq(toks[i + 2]).strip()
                if (box == '' or box.lower() == 'auto') and toon:
                    edits.append((spans[i + 1][1], spans[i + 1][2], toks[i + 2]))
                    todo.append((n, w, 'DONE', '-> -LogToonIn %s %s (`%s` names no box now; the character it logs in '
                                 'names it)' % (toks[i + 2], toks[i + 2], toks[i + 1])))
            i += 1; continue
        if wl == '-loginatcharacterselect':
            # `<fw> <character>` -> `-LogToonIn <character> <character>`. With no character it pressed
            # Play on whatever was selected - nothing does that now, so the line stays and its to-do says so.
            c = _read_values(toks, i + 1, 'f')
            if c < len(toks) and not _ends_values(toks[c]):
                toon = _unq(toks[c]).strip()
                if toon and toon.lower() != 'does_not_exist':
                    edits.append((spans[i][1], spans[c][2], '-LogToonIn %s %s' % (toks[c], toks[c])))
                    todo.append((n, w, 'DONE', '-> -LogToonIn %s %s' % (toks[c], toks[c])))
                    i = c + 1; continue
            i += 1; continue
        i += 1
    for a, b, text in sorted(edits, reverse=True):
        line = line[:a] + text + line[b:]
    return line

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
        # 'compatible' too: the old call passes what the new form needs and the arguments are kept exactly as written -
        # CancelCasting[fw, Args...] -> Abilities:CancelCasting[fw, except..., -flags]. A profile's command text is moved
        # to the new form by this same rule when the bot loads it.
        args_ok = (not has_args) or row.get('argsCheck') in ('same-count', 'compatible')
        # the map proves the two signatures line up, not that THIS call passes what the new form needs - a call
        # that leaves off (or blanks) an argument the new form requires is the writer's to finish
        need = row.get('argsNeeded') or 0
        given = call_args(line, m.end()) if has_args else []
        # only a VISIBLY short call: `${...}` text can expand to several arguments, so a call holding one is not
        # counted short (nor is one whose `[` does not close on the line)
        short = need > 0 and given is not None and not any('${' in a for a in given) \
            and (len(given) < need or any(not a for a in given[:need]))
        fwi = row.get('forWhoInsert') or {}
        # a moved/renamed call; or a call whose ONLY change is the for-who it never had (forWhoInsert `always`)
        rewrite = (st in ('moved', 'renamed') and args_ok) or \
            (st == 'signature' and fwi.get('when') == 'always' and row.get('argsCheck') == 'same-count')
        cure = cure_api_call(row, line, m) if (rewrite and safe and not short) else 'asis'
        if cure is None:
            todo.append((n, old, st, 'a word it passes is not one the new method reads - nothing was changed, and the method refuses the '
                         'request naming that word. Kinds (arcane noxious elemental trauma, or a e n t), -AutoRemove <seconds>, -tag <name>, '
                         'and on RequestGroupWatch -count <n> are the words now (AutoRemoveMS -> seconds, CustomFlag -> -tag, '
                         'exclusive / only / DirectTarget gone).'))
            continue
        if cure != 'asis':
            text, end, notes = cure
            out.append(line[pos:m.start()]); out.append(text); pos = end
            todo.append((n, old, 'DONE', '-> %s' % text + ''.join(' (%s)' % x for x in notes)))
            continue
        if rewrite and safe and not short and not row.get('argsDropped'):
            ins, used = with_forwho(fwi, line[m.end():])
            out.append(line[pos:m.start()]); out.append(nf + ins); pos = m.end() + used
            todo.append((n, old, 'DONE', '-> %s' % nf + (FW_DONE % fwi['value'] if ins else ''))); continue
        why = row.get('howToFix') or ''
        if st in ('moved', 'renamed', 'signature') and m.group(1):
            # a FUNCTION-FORM call (`call OgreBotAPI.DestroyItem "X" 3`): never rewritten (`safe`), and its arguments are
            # the Classic function's - the counts below do not apply (they read "needs 2 argument(s) ... leaves one off"
            # on every row)
            why = function_form_todo(nf, row.get('newSignature')) + why
        elif st in ('moved', 'renamed', 'signature') and not args_ok:
            why = 'check the arguments first - the map cannot prove they line up. ' + why
        elif st in ('moved', 'renamed', 'signature') and short:
            why = ('check the arguments first - the new form needs %d argument(s) here and this call leaves one off or blank. '
                   % need) + why
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
    # A Classic framework TYPE renamed to a new-bot type - Object_Timer -> ogretimer (2026-10-24): the same methods and
    # members, so swapping the declared type is the whole conversion. Only where it IS the type: `variable[(scope)]
    # <Old> <name>` and `declarevariable <name> <Old>`; any other use is still said below.
    for name, fw in M.by_fw.items():
        nf = fw.get('newForm') or ''
        if fw['status'] != 'renamed' or not re.match(r'^[a-z][a-z0-9_]*$', nf):
            continue
        pats = (re.compile(r'(\bvariable(?:\([a-z]+\))?\s+)%s(?=\s)' % re.escape(name)),
                re.compile(r'(\bdeclarevariable\s+\S+\s+)%s(?=\s|$)' % re.escape(name)))
        hit = False
        for pat in pats:
            if pat.search(new):
                new = pat.sub(lambda _m: _m.group(1) + nf, new); hit = True
        if hit:
            todo.append((n, name, 'DONE', '-> %s' % nf))
    for u in unmapped_hits(M, new, own):
        fw = M.by_fw.get(u)
        if fw:
            if fw['status'] != 'unchanged': todo.append((n, u, fw['status'], fw.get('howToFix') or ''))
            continue
        todo.append((n, u, 'UNKNOWN', 'a Classic global the map has no row for (%s) - stop and ask' % M.unmapped[u]))
    new = console_changed_rows(new, n, todo)
    for verb, quoted, at in reversed(console_hits(M, new)):
        row = M.by_verb.get(verb.lower())
        if quoted: todo.append((n, verb, 'QUOTED', 'remove the quotes around the console command and its arguments'))
        if row is None and verb.lower() not in M.new_console:
            todo.append((n, verb, 'UNKNOWN', 'console verb not in the map or the new console'))
        elif row and row['status'] == 'renamed' and row.get('newForm') and not row.get('note'):
            new = new[:at] + row['newForm'] + new[at + len(verb):]
            todo.append((n, verb, 'DONE', '-> %s' % row['newForm']))
        elif row and console_forwho(M, row, verb):
            new = new[:at] + console_forwho(M, row, verb) + new[at + len(verb):]
            todo.append((n, verb, 'DONE', '-> %s' % row['newForm'] + FW_DONE % row['forWhoInsert']['value']))
        elif row and not quoted and console_kept_forwho(M, row, verb, console_first_arg(new, at + len(verb))) == 'insert':
            new = new[:at + len(verb)] + ' ' + row['forWhoInsert']['value'] + new[at + len(verb):]
            todo.append((n, verb, 'DONE', '-> %s' % row['newForm'] + FW_DONE % row['forWhoInsert']['value']))
        elif row and not quoted and console_kept_forwho(M, row, verb, console_first_arg(new, at + len(verb))) == 'converted':
            pass                                         # converted already (its `auto`) - nothing left to do
        elif row and row['status'] != 'unchanged':
            todo.append((n, verb, row['status'], row.get('howToFix') or ''))
    return new

def backup_name(path):
    stem, ext = os.path.splitext(path)
    return stem + '.classic' + (ext or '.iss')

def cmd_fix(M, path, outp, in_place=False, follow=None):
    # #includes: followed on a dry run unless --no-follow-includes; a WRITE follows only with --follow-includes
    writes = bool(outp) or in_place
    if follow is None: follow = not writes
    if in_place and outp:
        print('fix: use -o OR --in-place, not both'); return 2
    if not follow:
        return fix_one(M, path, outp, in_place)
    files, skipped = include_tree(path)
    base = None
    if outp:
        # -o is a FOLDER here: each file lands at its place under the Scripts folder (else under the main file's)
        home = scripts_home(path)
        root = os.path.join(home, 'Scripts') if home else os.path.dirname(os.path.abspath(path))
        base = root if all(same_file_key(f).startswith(same_file_key(root) + os.sep) for f in files) \
            else os.path.dirname(os.path.abspath(path))
    rc = 0
    for f in files:
        out = os.path.join(outp, os.path.relpath(os.path.abspath(f), base)) if outp else None
        if out and os.path.dirname(out) and not os.path.isdir(os.path.dirname(out)): os.makedirs(os.path.dirname(out))
        rc = max(rc, fix_one(M, f, out, in_place))
    say_skipped(skipped)
    print('fix: %d file(s) - %s and the include files it reaches%s' % (len(files), path,
          (', %d #include(s) not followed (listed above)' % len(skipped)) if skipped else ''))
    return rc

def fix_one(M, path, outp, in_place=False):
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
def files_of(paths, follow=False):
    """Every file to read: the files named, every .iss / .inc / .json in the folders named, and - with `follow` -
    the include files each script reaches (each file once, whatever reaches it twice)."""
    seen = set()
    for p in paths:
        if os.path.isdir(p):
            named = []
            for root, _, fs in os.walk(p):
                for f in fs:
                    if f.lower().endswith(('.iss', '.inc', '.json')): named.append(os.path.join(root, f))
        else:
            named = [p]
        for f in named:
            if not follow or f.lower().endswith('.json'):
                if same_file_key(f) not in seen:
                    seen.add(same_file_key(f)); yield f
                continue
            files, skipped = include_tree(f, seen)
            say_skipped(skipped)
            for g in files: yield g

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

def cmd_sweep(M, paths, coverage=False, follow=True):
    bad = warn = n_files = n_hits = 0
    for f in files_of(paths, follow):
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
            if not coverage:
                # a row that kept its name but still passes words it no longer reads (`fix` drops them)
                left = []
                console_changed_rows(line, i, left)
                for _, verb, st, why in left:
                    n_hits += 1; bad += 1
                    print('%s:%s: OLD     %s - %s' % (f, i, verb, ('run fix: ' + why[3:]) if st == 'DONE' else why))
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

def cmd_sites(paths, follow=True):
    n = 0
    for f in files_of(paths, follow):
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
    fi = ap.add_mutually_exclusive_group()
    fi.add_argument('--follow-includes', dest='follow', action='store_true', default=None,
                    help="follow the script's own #include files (the default, except for fix -o / --in-place)")
    fi.add_argument('--no-follow-includes', dest='follow', action='store_false',
                    help='only the files named - not their #include files')
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
    a.args = a.args + [x for x in extra if x not in ('-o', '--out', '--map', '--in-place', '--follow-includes',
                                                     '--no-follow-includes')]
    M = Map(find_map(a.map))
    if a.cmd == 'lookup': cmd_lookup(M, a.args); return 0
    follow = True if a.follow is None else a.follow
    if a.cmd == 'fix': return cmd_fix(M, a.args[0], a.out, a.in_place, a.follow)
    if a.cmd == 'sites': return cmd_sites(a.args, follow)
    return cmd_sweep(M, a.args, coverage=(a.cmd == 'coverage'), follow=follow)

if __name__ == '__main__':
    sys.exit(main())

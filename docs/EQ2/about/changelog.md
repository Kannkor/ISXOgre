# Changelog

This page tracks ISXOgre and OgreBot version updates.

!!! info
    There is no longer a separate development build. Everything is patched directly to live.

For the complete historical changelog with all 313+ patches dating back to 2018, visit the [wiki revision history](https://wiki.ogregaming.com/eq2/index.php/RevisionHistory).

---

## ISXOgre-2024.11.30

### OgreBot 17.525

**Fighter Threat Management**

- `ThreatFighterIgnoreList` commands: `_Add`, `_Remove`, `_Clear`, `_List` (returns JSON)

**Rescue Ability Casting**

- New `-CastRescue_AP` command with parameters:
    - `-NPCRequired` -- use current target
    - `-ActorID #` -- specify target by ID
    - `-NoForceTargets` -- exclude force target abilities

### OgreBot 17.512

**OET (Ogre Effect Tracker)**

- Alpha feature that examines detrimental effects
- Logs: name, IconIDs, effects/descriptions
- Storage: `Scripts\EQ2OgreCommon\OgreEffectTracker\Temp\`
- Merge function consolidates zone files to `Detrimentals\` folder

### OgreBot 17.492

**Alias Changes**

- Reverted recent alias selection order changes -- back to first person found

**IRC Integration**

- PING sent every minute to server
- Reconnect triggered on 2 missed pings
- Maintains auth list on reconnection

**OgreConsole Enhancement**

- IRC commands rerouted to OC if IRC is disconnected, enabling solo raid running without IRC

### OgreBot 17.484

- CastStack tab clears selection on profile load
- Threat options moved to Settings tab for global application

### OgreBot 17.483

- MCP button behavior updated (left-click requires mouse release over button)
- Added perk resetter window type support
- `Champions_Zone_Resetter[forwho,"zone name"]` API command
- New CastStack options: `[ANF]` Aggro On Non Fighter Only, `[ANMe]` Aggro on Not Me

### OgreBot 17.479

- Stunned/stifled cure now honors group/raid and single target cure disable checkboxes

### OgreBot 17.478

- Visual Studio build routine issues resolved
- Chat/Spawn/Despawn events support double-click enable/disable
- Load tab handles bracket syntax properly
- Listbox editing escapes special characters

### OgreBot 17.471

- IRC connection wait extended (3s to 10s + 1s)
- New option: Cure Curse in Reverse Order (bottom-up processing)

---

## ISXOgre-2024.07.16

### OgreBot 17.420

- Basic travel mesh capabilities for Instance Controller
- Updated default files: Corrupted Caldera, Fort Sunder, Stonebrunt Defile, Blackhook Badlands

### OgreBot 17.418 -- Sodden Archipelago: Thawed Marshes [Raid]

- Joggu the Steadfast: automated pet management during joust
- Monuseru, Titan of the Depths: tank designation, circle spawn mechanics
- Grand Shaman Grungizt: automatic ground target jousting

### OgreBot 17.413

- Bot reload clears overseer and pack pony timers
- `Get_ReviveLocation` API method
- Updated revive command syntax with search string support

### OgreBot 17.412 -- Sodden Archipelago Initial Content

- Barlsbit the Scavenger: auto-cure (non-fighters first, fighters last)
- Sommumun the Frenzied: automatic sneak/shroud/stealth
- Joggu the Steadfast: joust automation
- Bucko & Chieftain Maferi: complex movement phase automation
- Vitoth of the Gnarled Roots: circle avoidance, add management

### OgreBot 17.411

- Pack Pony alternate appearance support
- Overseer multi-choice reward auto-accept
- `Get_CursedID` API method with filtering parameters

### OgreBot 17.400

- Ability Tracker add method via API/OC
- Ogre IM executes ESC after TSE run

---

## ISXOgre-2023.05.29

Notable features from this release series include Instance Controller group size monitoring, Smartloot sorting, `Get_RotationData` JSON method, `Set_CampSpotJump_Handle` for jump mechanics, auto-intercept code, and major OgreConsole rewrite with 7000+ lines of MCP command updates.

---

## Older Versions

For the complete changelog including all versions from 2018 through 2023, see the [full revision history on the wiki](https://wiki.ogregaming.com/eq2/index.php/RevisionHistory).

<!-- Source: wiki.ogregaming.com/eq2/index.php/RevisionHistory - This page may need updating -->

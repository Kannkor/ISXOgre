# OgreIRC

OgreIRC is an IRC bridge that hooks into your uplink and allows commands to pass through it. It enables bot control across multiple players in raid situations and provides CLI access to OgreBot functions from any IRC client.

!!! warning "Unsupported Feature"
    OgreIRC is 100% unsupported. It works, but there are no timelines or extensive support for it.

---

## How It Works

Two scripts operate together:

- **OgreIRC** -- runs in the uplink
- **OgreIRCSession** -- runs in each game session

Data flows: Sessions &rarr; OgreIRC &rarr; IRC channel (bidirectional).

---

## Requirements

### ISXIM Installation

ISXIM is required on **one** computer that serves as the IRC-to-network bridge.

- Download from isxgames.com, or directly download `ISXIM.dll` to `innerspace/x64/extensions/isxdk35/`
- Console command alternative:
  ```
  httpget -file "${LavishScript.HomeDirectory}/x64/Extensions/ISXDK35/ISXIM.dll" <url>
  ```
- Run `ext isxim` once to update
- Do **not** add ISXIM to startup

### OgreConsole Configuration

Fill in IRC information on the right side of the [OgreConsole](../ogrebot/tabs/ogre-console.md) tab:

| Field | Description |
|-------|-------------|
| **UplinkName** | Name of the uplink running the IRC bridge |
| **IRCServer** | Target IRC server |
| **DefaultUser** | IRC username |
| **DefaultChannel** | Single channel only (current limitation) |
| **ChannelPassword** | IRC channel password |

---

## Loading OgreIRC

Console command:

```
ogre irc
```

This relays sessions to load OgreIRCSession, then loads OgreIRC into the uplink. You can also set it to load automatically via the [Load](../ogrebot/tabs/load.md) tab.

### Recommended Load Configuration

| Session | What to Load |
|---------|-------------|
| **Tank (Uplink)** | Ogre IRC Uplink (bridge only) |
| **Tank (Session)** | Show IRC Interface (for tells/messages) |
| **All Sessions** | Ogre IRC (this session) -- connects everyone |

---

## In-Game Interface

- **Access:** ++ctrl+grave++ (same as console but hold Ctrl)
- **Tell Display:** OgreIRCConsole window
- Messages containing NULL characters truncate at that point

### Color Coding

| Color | Meaning |
|-------|---------|
| **Green** | Chat for humans |
| **Red** | Bot commands |
| **Yellow** | In-game tells |

---

## Command Structure

### Basic Format

```
!c [ForWho] [commands]
!command [ForWho] [commands]
```

### ForWho Options

| Target | Description |
|--------|-------------|
| `all` | All bots listen |
| `Bot_Name` | Specific IRC bot only (not the toon name) |
| `me` | Only the commanding player |

### Example

```
!c all -cs all -jst-off casters -jstout all -assist someone all
```

---

## Command Reference

### Authentication

| Command | Description |
|---------|-------------|
| `-auth` | Add IRC bot to auth list (overrides ignore settings) |
| `-authlist` | List authorized users |
| `-unauth` | Remove IRC bot from auth list |
| `-unauthall` | Clear entire auth list |

### Movement

| Command | Description |
|---------|-------------|
| `-Come2Me` / `-ComeToMe` | Move target to command sender |
| `-Move2Area` / `-MoveToArea` | Move to XZ coordinates |
| `-OgreFollow` / `-OFol` | Follow specified player |
| `-OFol++` / `-OFol--` | Adjust OgreFollow distance |
| `-Holdup` | Hold position |
| `-LetsGo` | Resume movement |
| `-NoMove` | Set NoMove flag (cleared by LetsGo) |

### Flight

| Command | Description |
|---------|-------------|
| `-FlyUp` | Press Home (swim/fly up) |
| `-FlyDown` | Press End (swim/fly down) |
| `-FlyStop` | Release both Home and End |
| `-FlyUpForWho` / `-FlyDownForWho` / `-FlyStopForWho` | Flight for a specific character |

### CampSpot

| Command | Description |
|---------|-------------|
| `-campspot` / `-cs` | Set campspot for target |
| `-ChangeCampSpot` / `-CCS` | Change coordinates (X, Y, Z) |
| `-ChangeCampSpotForWho` / `-CCSW` | Change campspot for specific player |
| `-CS-JO-JI` | CampSpot + JoustOff + JoustIn combo |

### Joust

| Command | Description |
|---------|-------------|
| `-jst-in` / `-joustin` | JoustIn for target |
| `-jst-off` / `-joustoff` | JoustOff for target |
| `-jst-out` / `-joustout` | JoustOut for target |

### Casting

| Command | Description |
|---------|-------------|
| `-Cast` | Cast spell (who, spell name) |
| `-CastOn` | Cast spell on target (who, spell, target) |
| `-RaidDebuff` | Cast DoV raid debuff |
| `-CancelMaintained` | Cancel ability by name |
| `-ChangeCastStack` / `-CCStack` | Modify cast stack |

### Ability / Targeting

| Command | Description |
|---------|-------------|
| `-Assist` / `-Ass` | Change assist target |
| `-Target` | Target specified entity |
| `-NoTarget` | Clear all targets |
| `-AutoTargetToggle` / `-ATT` | Toggle auto-target |
| `-LoadAutoTargetList` / `-LATL` | Load saved autotarget list |
| `-Special` | Click nearest special |
| `-SpecialForWho` | Click special for specific character |

### Items

| Command | Description |
|---------|-------------|
| `-UseItem` | Use item (who, item name) |
| `-UseItemOn` | Use item on target (who, item, target) |
| `-GetFlag` | Get rally banner |
| `-UseFlag` | Use rally banner |
| `-Repair` / `-RepairGear` | Repair gear |

### Combat

| Command | Description |
|---------|-------------|
| `-Rebuff` | Cancel all maintained abilities from spellbook |
| `-PetOff` | Force pets to back off |
| `-Evac` | Cast Evacuate (any character with the ability) |
| `-ImmRes` | Use Cleric Immaculate Resurrection |
| `-Res` | Remove StopRes flag |
| `-ResStone` | Cast priest res stone |
| `-Revive` | Force character revive |

### Group / Raid

| Command | Description |
|---------|-------------|
| `-Invite` / `-Raidinvite` | Stagger raid/group invites |
| `-Disband` | Disband all from group/raid |
| `-Group` | Send message via group chat |
| `-Raid` | Fire OnChat event |
| `-Tell` | Send tell from one character to another |

### Mount / Movement

| Command | Description |
|---------|-------------|
| `-Mount` | Toggle mount on/off |
| `-Run` / `-Walk` / `-RunWalk` | Toggle run/walk |
| `-Jump` | Press spacebar |
| `-AutoRun` | Press OgreBotAutoRunKey |

### Zone

| Command | Description |
|---------|-------------|
| `-Door` / `-DoorX` | Select door option while zoning |
| `-Zone` | Click zone object |
| `-ZoneResetAll` | Reset all available zones (no confirmation) |
| `-CallGH` | Call to Guild Hall |
| `-PortalToGuild` / `-ToGuild` | Click portal to guild house |

### Bot Control

| Command | Description |
|---------|-------------|
| `-LoadBot` | Load bot on all sessions |
| `-EndBot` | End OgreBot on all sessions |
| `-ReloadBot` | Reload bot if active |
| `-LoadExt` | Load ISXOgre |
| `-Unloadext` | Unload ISXOgre |
| `-Connect` | Run connect uplink script |
| `-Disconnect` | Run disconnect uplink script |
| `-DevBot` | Load dev bot on all sessions |
| `-EndScript` | Relay endscript |
| `-LoadProfileForWho` | Load profile for player |
| `-Profile` / `-LoadProfile` | Load OgreBot profile |

### Interface

| Command | Description |
|---------|-------------|
| `-Main` | Toggle OgreBot Main window |
| `-ClsWdw` | Close most recently opened window |

### Bot State

| Command | Description |
|---------|-------------|
| `-Pause` | Pause bot |
| `-Resume` | Resume bot |
| `-sleep` | Put IRC bot to sleep (only responds to `-wake`) |
| `-wake` | Wake IRC bot from sleep |
| `-available` / `-a` | Check if character is logged in |

### Advanced

| Command | Description |
|---------|-------------|
| `-ApplyVerb` | Right-click actor option (verb is **case sensitive**) |
| `-Uplinkoption` / `-UO` | Change UI options (requires ogreuixml.xml reference) |

---

## Not Implemented

The following commands exist in the codebase but are not functional:

- Trak-HUD, Turt-HUD
- RelayRunScript, RawCommand
- OgreBotAtom / OgreBotAtomRelay
- ExecuteAtom, OgreCommand

Most require special coding or infinite parameters.

<!-- Source: wiki.ogregaming.com/eq2/index.php/OgreIRC:OgreIRC - This page may need updating -->

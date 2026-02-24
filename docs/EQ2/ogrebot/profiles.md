# Profiles

Profiles are how OgreBot saves and loads all of your settings. Every checkbox, ability priority, heal threshold, alias, and configuration option is stored in a profile. Understanding the profile system helps you manage settings efficiently across multiple characters.

---

## What Is a Profile?

A profile is an XML file stored in the `EQ2OgreBot/Save/` folder. It contains everything about how OgreBot is configured for a character: the Settings tab, Cast Stack, Ability Rotation, Aliases, HUD positions, and every other tab in the UI.

When OgreBot starts, it loads a profile and applies all of its settings. When you make changes in the UI, those changes are saved back to the profile.

---

## Profile Types

### Character-Specific Profiles

By default, each character gets its own profile file named after the server and character:

- `EQ2Save_Maj'Dul_MyWizard.xml`
- `EQ2Save_Isle of Refuge_MyTank.xml`

This means every character has completely independent settings.

### Master Profiles (Recommended)

A **Master Profile** is a single profile shared by all characters of the same class. Instead of maintaining separate profiles for each of your six Rangers, one Master profile handles all of them.

**Example:** `EQ2Save_Master_Ranger.xml` is used by every Ranger character on your account.

!!! tip "Why Use Master Profiles?"
    Master profiles save you significant time. When you update your Ranger's Cast Stack, the change applies to **all** your Rangers automatically. No need to update each character individually.

### How Master Profiles Are Assigned

OgreBot uses a routing file called `EQ2Save_Settings.xml` to decide which profile each character loads. The routing works by priority:

| Priority | Matches On | Example |
|----------|-----------|---------|
| 1 (highest) | Server + Class + Character | `Maj'Dul.Wizard.MyWiz` |
| 2 | Class + Character | `Wizard.MyWiz` |
| 3 | Character name only | `MyWiz` |
| 4 | Server + Class | `Maj'Dul.Wizard` |
| 5 | Class only | `Wizard` |
| 6 | Global fallback | `all` |
| 7 (lowest) | Auto-generated | Default filename pattern |

**The most common setup** is to add an entry at priority 5 (class only), which makes all characters of that class use the same Master profile:

```
Wizard  -->  EQ2Save_Master_Wizard.xml
Ranger  -->  EQ2Save_Master_Ranger.xml
```

If you need one specific character to use different settings, add a higher-priority entry for just that character.

---

## Profile Parts

Profile Parts let you split specific tabs out of your main profile into separate files. This is useful for sharing common settings across all characters regardless of class.

### Why Use Profile Parts?

Consider these tabs that are the same for every character you play:

- **Pack Pony** -- inventory management (same for everyone)
- **HUDs** -- HUD positions on your screen (same for all DPS, or same for all tanks)
- **Settings** -- master checkboxes (similar for tanks vs. non-tanks)
- **Overseer** -- overseer preferences (same for everyone)
- **OSA** -- on-screen assistant (same for everyone)

Without Profile Parts, you would need to update each of these in every Master profile whenever you make a change. With Profile Parts, these shared tabs live in separate files and every profile references the same file.

### How Profile Parts Work

1. Profile Parts files are stored in `EQ2OgreBot/Save/ProfileParts/`
2. Your main profile contains a mapping that says "for this tab, load from this external file"
3. When Profile Parts are enabled, OgreBot loads each mapped tab from its external file instead of from the main profile
4. Tabs without a mapping still load normally from the main profile

### Common Profile Parts Setup

| Part File | What It Contains | Shared By |
|-----------|-----------------|-----------|
| `Settings_Tank.xml` | Tank-specific checkbox settings | All tank classes |
| `Settings_NotTank.xml` | DPS/Healer checkbox settings | All non-tank classes |
| `HUD_Tank.xml` | Tank HUD positions | All tank classes |
| `HUD_NotTank.xml` | DPS/Healer HUD positions | All non-tank classes |
| `PackPony_AllToons.xml` | Pack pony configuration | All characters |
| `OSA_AllToons.xml` | On-Screen Assistant settings | All characters |
| `Overseer_AllToons.xml` | Overseer preferences | All characters |

!!! note "Profile Parts Are Optional"
    You do not need to use Profile Parts to use OgreBot. They are an organizational tool for players who box many characters and want to keep shared settings in one place.

---

## Importing Profiles From Others

One of the most common profile tasks is importing someone else's Cast Stack (ability priorities) into your own profile. Here is how to do it safely.

### What Is Safe to Import

These tabs are **class-specific** and are the most common things to import:

| Tab | Notes |
|-----|-------|
| **Cast Stack** | Ability priorities -- this is the main reason to import |
| **Ability Rotation** | Ability-specific durations and interrupt settings |
| **Item Rotation** | Item usage configuration |
| **Pre-Cast / Post-Cast** | Ability linking before/after casts |

### What to Keep From Your Own Profile

These tabs contain **personal settings** that should not be overwritten:

| Tab | Why Keep Yours |
|-----|---------------|
| **Settings** | Your personal enable/disable preferences |
| **Setup** | Your thresholds (attack %, heal %, follow distance) |
| **HUDs** | Your screen layout positions |
| **Aliases** | Your group member mappings |
| **Assist** | Your assist target |
| **Loot** | Your loot preferences |
| **Profile Parts** | Your Profile Parts configuration |
| **Load Execute** | Your custom scripts that run on profile load |

### How to Merge a Profile

!!! warning "Always Back Up First"
    Before making any changes, copy your current profile to a backup file. If anything goes wrong, you can restore it.

**The safe approach:**

1. **Back up** your current profile (e.g., copy `EQ2Save_Master_Wizard.xml` to `EQ2Save_Master_Wizard_backup.xml`)
2. **Open** the other player's profile in a text editor
3. **Copy** only the Cast Stack section (the `<Set Name="CastStack">...</Set>` block)
4. **Open** your profile in a text editor
5. **Replace** only the Cast Stack section in your profile with the copied one
6. **Save** and reload OgreBot

!!! tip "Profile Parts Alternative"
    You can also save an imported Cast Stack as a Profile Part. Create a new file in the `ProfileParts/` folder with just the Cast Stack data, and map it in your profile. This keeps your main profile clean and makes it easy to swap between different Cast Stacks.

---

## Loading Profiles

You can switch profiles without restarting OgreBot:

- **From the UI:** Use the profile dropdown in the OgreBot interface
- **From the console:** Type the appropriate load command
- **Cross-session:** Load a profile on all characters at once using cross-session commands

---

## Summary

```
How Profile Loading Works:

EQ2Save_Settings.xml  --->  EQ2Save_Master_Ranger.xml
    (routing table)              (main profile)
                                      |
                     +----------------+----------------+
                     |                |                |
               Tabs from main    Tabs from parts   Tabs from main
               (CastStack,      (Settings,         (Aliases,
                Setup, etc.)     HUDs, PackPony)    Assist, etc.)
                                      |
                               ProfileParts/
                               +-- Settings_NotTank.xml
                               +-- HUD_NotTank.xml
                               +-- PackPony_AllToons.xml
                               +-- OSA_AllToons.xml
                               +-- Overseer_AllToons.xml
```

**Key takeaway:** When importing a profile from someone else, only update the class-specific tabs (Cast Stack, Ability Rotation, etc.). Your personal settings and shared Profile Parts remain untouched.

<!-- Source: Internal OgreBot Profile System Reference - This page may need updating -->

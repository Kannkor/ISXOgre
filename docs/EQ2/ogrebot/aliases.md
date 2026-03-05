# Aliases

An alias is a way to identify a character by role instead of by name. Instead of updating every setting when your group composition changes, you can use aliases like `@Tank` or `*Healer` and OgreBot resolves them to the right character automatically.

---

## Alias Types

OgreBot supports three types of aliases:

### Built-in Aliases (`@` prefix)

These are determined automatically by OgreBot based on your current group composition. You cannot modify them -- they update dynamically as group members change.

> **:memo: Red Text**
>
> If a built-in alias displays in red, it means no matching character was found in your current group for that role.

### User-Defined Aliases (`*` prefix)

These are aliases you create yourself on the **Aliases** tab. Use these when you want to assign a custom name to a specific group member or role that the built-in aliases do not cover.

### Pet Aliases (`Pet:` prefix)

These reference the pet owned by a specific player. For example, `Pet:Kannkor` targets whatever pet Kannkor currently has active.

### Direct Names

You can also use a player's character name directly without any prefix. This references that player as a group or raid member.

---

## Built-in Alias Reference

| Alias | Targets |
|-------|---------|
| `@Me` | Your current character |
| `@Group` | Each group member individually |
| `@Raid` | The entire raid roster |
| `@NotSelfGroup` | All group members except yourself |
| `@PCTarget` | The player character you currently have targeted |
| `@Tank` | The fighter in your group |
| `@Bard` | The bard in your group |
| `@Enchanter` | The enchanter in your group |
| `@Healer1` through `@Healer6` | Healers by priority |
| `@DPS1` through `@DPS6` | DPS characters by priority |

### Healer Priority Order

When multiple healers are in the group, they are assigned in this order:

1. Shaman (Mystic, Defiler)
2. Druid (Fury, Warden)
3. Cleric (Templar, Inquisitor)
4. Shaper (Channeler)

So `@Healer1` is always the Shaman (if one exists), `@Healer2` is the Druid, and so on.

### DPS Priority Order

When multiple DPS are in the group, they are assigned in this order:

1. Sorcerer (Wizard, Warlock)
2. Predator (Ranger, Assassin)
3. Animalist (Beastlord)
4. Summoner (Conjuror, Necromancer)
5. Rogue (Brigand, Swashbuckler)

> **:memo: Multiple of the Same Archetype**
>
> If you have two characters of the same archetype (e.g., two Sorcerers), they are randomly assigned between the numbered aliases. The ordering between same-archetype members is not guaranteed.

---

## Using Aliases

Aliases can be used anywhere OgreBot expects a character name:

- **Assist tab** -- Set your assist target to `@Tank`
- **Cast Stack** -- Target heals to `@Healer1` or `*MainTank`
- **Chat Commands** -- Reference group members by role

### Example: Setting Up a Custom Alias

1. Open the OgreBot main UI
2. Click the **Aliases** tab
3. Add a new entry with a `*` prefix name (e.g., `*MT`)
4. Set its value to the character name of your main tank

Now you can use `*MT` anywhere in OgreBot and it resolves to that character.

---

## Viewing Active Aliases

To see all currently active aliases and what they resolve to:

1. Open the OgreBot UI
2. Go to the **Aliases** tab
3. Click the **Display Aliases** button

This prints all active aliases and their current targets to the InnerSpace console.

<!-- Source: wiki.ogregaming.com/eq2/index.php/Aliases - This page may need updating -->

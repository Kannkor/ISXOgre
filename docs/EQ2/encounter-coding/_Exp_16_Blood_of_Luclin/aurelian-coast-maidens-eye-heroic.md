# Aurelian Coast: Maiden's Eye [Heroic]

**Expansion:** Blood of Luclin (Exp 16)

This heroic zone contains 3 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Xylox the Poisonous](#xylox-the-poisonous) | Positioning and jousting to avoid poison |
| [The Shadow Overlord](#the-shadow-overlord) | Auto-target priority for add phases |
| [Va Dyn Kar](#va-dyn-kar) | Curse management with selective curing |

---

## Xylox the Poisonous

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A positioning and jousting fight. The tank and the rest of the group are placed at separate positions. When poison fills the area, the group jousts to an alternate camp spot to avoid the damage.

### What the Module Does

**Positioning:**

- The tank is positioned at the front of the boss
- The rest of the group is placed at a separate raid position behind the boss

**Poison Joust:**

- When the message "This should help clear the air..." appears, the entire group jousts to the alternate camp spot away from the poison
- Pets are automatically pulled back during the joust to prevent them from staying in the poison
- After the poison clears, the group returns to their original positions

### Player Notes

- The joust is triggered by the in-game text message. Stay with the group and let the module handle repositioning.
- Pets are pulled back automatically during the joust phase.

---

## The Shadow Overlord

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

An add-management encounter where shadow adds spawn at various HP thresholds. The module automatically configures target priorities so the group kills adds before returning to the named.

### What the Module Does

**Auto-Target Setup:**

- Automatically configures target priorities for the group
- At each HP threshold (75%, 50%, 25%, 10%, and 0%), shadow adds spawn that must be killed
- **Shadowed Lord of Magic** and **Shadowed Lord of Might** are set as priority targets above the named
- Once the adds are dead, the group automatically retargets the named

### Player Notes

- Target switching is fully automatic. Let the module handle priority targeting.
- Adds spawn at multiple HP thresholds throughout the fight -- expect several waves.

---

## Va Dyn Kar

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A curse management encounter where the boss applies multiple curses, but only one specific curse should be cured. Curing the wrong curse can be deadly.

### What the Module Does

**Selective Curse Curing:**

- Monitors for the **Words of Shadow** curse on group members
- When detected, automatically requests a cure for the correct curse only
- Ignores the other curse that should NOT be cured, preventing accidental deaths

### Player Notes

- Do NOT manually cure curses during this fight. The module handles which curse to cure and which to leave alone.
- Curing the wrong curse can kill the player -- trust the automation.

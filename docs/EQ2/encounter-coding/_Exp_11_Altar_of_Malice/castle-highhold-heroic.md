# Castle Highhold [Heroic]

**Expansion:** Altar of Malice (Exp 11)

This zone has 2 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Sa'Dax Senshali](#sadax-senshali) | Color orb clicking automation |
| [Gudre Blackhand](#gudre-blackhand) | Sunder verb, tapestry clicking, fire stack management |

---

## Sa'Dax Senshali

Setup command: `Set up for Senshali` (also accepts `Set up for Sa'Dax`)

### Overview

A fight with a color orb mechanic where specific orb combinations must be clicked based on the announced color.

### What the Module Does

**Color Orb Automation:**

- When the boss teleports skyward, detects the announced color (Orange, Purple, or Green)
- Orange: clicks Yellow then Red orb
- Purple: clicks Blue then Red orb
- Green: clicks Yellow then Blue orb
- Campspot movement is disabled during orb clicking and re-enabled when the boss returns

**Dark Luclinite:**

- Automatically clicks nearby Dark Luclinite objects when no color has been called

### Player Notes

- Requires full group control for orb clicking automation

---

## Gudre Blackhand

Setup command: `Set up for Gudre` (also accepts `Set up for Blackhand` or `Move to next Tapestry spot`)

### Overview

A fight with fire stack management, tapestry interaction, and sunder mechanics.

### What the Module Does

**Tapestry Interaction:**

- Monitors Smouldering Combustion debuff stacks
- When stacks reach 10, automatically finds and clicks the nearest tapestry
- Cycles through 4 raid positions as tapestries are used up
- At key tapestry thresholds (4/6/8), sends a group say to move the group

**Sunder:**

- On specific boss chat triggers, automatically applies the Sunder verb on Gudre Blackhand

### Player Notes

- The group moves through multiple positions as tapestries are consumed

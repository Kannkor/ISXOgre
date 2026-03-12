# Chamber of Rejuvenation [Raid]

**Expansion:** Kunark Ascending (Exp 13)

!!! warning "Work in Progress"
    This module is still under development. Some encounters may have partial or missing automation.

This zone has 1 boss encounter with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Trakanon](#trakanon) | Death touch tank swap, bite timer, massive jawing, bursting spores joust, face-off port, detonator handling, toxic life rotation, bard cloud activation |

---

## Trakanon

Setup command: `Set up for Trakanon`

### Overview

A heavily scripted raid encounter with numerous mechanics including death touches, jousting, archetype-specific challenge ports, add handling, and ability rotations.

### What the Module Does

**Death Touch / Tank Swap:**

- When Trakanon targets someone as his "next victim," a 60-second HUD countdown is displayed
- If your character is the target: stops offensive actions and casts threat-shedding abilities, then resumes after 60 seconds
- Fighters receive an alert if the death touch target is still tanking near the deadline

**Bite Timer:**

- When Trakanon prepares a poisonous bite, a 45-second HUD countdown is displayed

**Massive Jawing:**

- Tracks the jawing cycle with a 35-second HUD countdown
- Fighters automatically cast Tower of Stone shortly before the next expected jawing

**Bursting Spores Joust:**

- When you contract bursting spores, your campspot shifts away from the group
- Re-checks every 5 seconds and returns to normal position once the debuff drops
- Enchanters in groups 2+ are excluded (they stay at their enchanter spots)

**Face Off (Challenge Port):**

- When a player is chosen to face off against a challenge NPC, the module identifies which archetype-specific NPC to target (Knight, Invoker, Deliverer, or Sower)
- Disables campspot and movement, then targets the challenge NPC
- When the challenge NPC dies, re-enables campspot and uses a speed boost to return to position

**Summoned Detonator:**

- Announces detonator spawns with a waypoint
- **Marked toons** automatically use Detect Weakness on the detonator when it comes within range
- Reports whether the detonator is Armed (must be killed) or Inert (must not be killed) with raid markers

**Toxic Life Rotation:**

- When the reet Ritualist spawns, group members are assigned a rotation order
- Each member casts Toxic Life when their turn comes, cycling through the group every 50 seconds

**Bard Cloud Activation:**

- Bards are assigned noxious clouds based on their raid group number
- They automatically navigate to their cloud and activate it using Reverse Intent

**Attunement Tracking:**

- Displays a 90-second HUD countdown when attuned to Trakanon's noxious aura

### Player Notes

- **Marked toons are required** for the Summoned Detonator Detect Weakness mechanic
- Enchanters are positioned at specific spots per raid group (groups 2, 3, and 4 each have separate enchanter positions)
- Enchanters get their pets dismissed and are set to ranged auto-attack mode during setup

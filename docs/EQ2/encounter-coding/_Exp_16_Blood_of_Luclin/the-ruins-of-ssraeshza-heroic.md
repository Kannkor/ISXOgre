# The Ruins of Ssraeshza [Heroic]

**Expansion:** Blood of Luclin (Exp 16)

This heroic zone contains 2 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Kor Va Xian](#kor-va-xian) | Auto-destroys Luclinite Bombs and solves shadow gate symbol puzzle |
| [Rath](#rath) | Clock puzzle solver |

---

## Kor Va Xian

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

An encounter with two mechanics: Luclinite Bombs that appear in your inventory and must be destroyed, and a shadow gate symbol puzzle that requires reading central symbols and inputting correct answers at transporter room statues.

### What the Module Does

**Luclinite Bomb Destruction:**

- Monitors your inventory for Luclinite Bombs
- When a Luclinite Bomb appears, it is automatically destroyed

**Shadow Gate Symbol Puzzle:**

- Reads the center main symbols (hammer, sword, symbol, or staff) based on their tint flags
- Determines the correct answer from the symbol combination
- When using Special Zone Specific at the transporter room statues, automatically inputs the correct answer

### Player Notes

- Luclinite Bombs are destroyed automatically -- no manual action needed.
- For the shadow gate puzzle, use **Special Zone Specific** near the transporter room statues to have the module auto-input the correct answer.

---

## Rath

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

An encounter with a clock puzzle mechanic. Players must read clock face positions and input the correct time.

### What the Module Does

**Clock Puzzle Solver:**

- When using Special Zone Specific near a clock adjustment, the module reads the hour and minute hand headings
- Converts the hand positions to the correct time
- Automatically inputs the correct answer

### Player Notes

- Use **Special Zone Specific** near the clock adjustment to trigger the automatic solver.
- The module reads the clock hands and calculates the correct time for you.

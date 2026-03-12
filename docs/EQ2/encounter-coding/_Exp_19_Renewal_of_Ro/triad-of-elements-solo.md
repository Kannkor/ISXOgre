# Triad of Elements [Solo]

**Expansion:** Renewal of Ro (Exp 19)

!!! warning "Work in Progress"
    Automation for this zone is still under development.

This solo zone contains 1 boss encounter.

## Available Setups

| Boss | Description |
|------|-------------|
| [Ozani](#ozani) | Automated claw puzzle solver (WIP) |

---

## Ozani

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a claw puzzle mechanic that must be solved by clicking claws in the correct sequence.

### What the Module Does

**Claw Puzzle Solver:**

- Detects the state (up/down) of each claw on 2 pillars (6 claws per pillar) using collision detection
- Automatically clicks claws 1 through 5 in sequence to solve the puzzle
- Uses a special "wiggle" pattern (clicking claws 4→1→2→5) to solve the 6th claw
- Automatically moves to each click position

### Player Notes

- The puzzle solver handles the clicking sequence automatically
- Allow the module to work through the sequence without manual clicking

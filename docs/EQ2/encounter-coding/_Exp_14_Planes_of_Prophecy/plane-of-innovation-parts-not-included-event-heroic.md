# Plane of Innovation: Parts not Included [Event Heroic]

**Expansion:** Planes of Prophecy (Exp 14)

This zone has 1 boss encounter with an OgreBot automation module.

## Available Setups

| Boss | Description |
|------|-------------|
| [Fixit Microtock / Fixit Omegatock](#fixit-microtock--fixit-omegatock) | Auto-repositioning behind NPCs, Overload systems verb (WIP) |

---

## Fixit Microtock / Fixit Omegatock

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

!!! warning "Work in Progress"
    This encounter's automation is still under development.

### Overview

A dual-boss fight with repositioning mechanics and an item-use verb.

### What the Module Does

**Auto-Repositioning:**

- On different trigger messages, repositions all characters behind the correct NPC (Microtock or Omegatock)
- Fighters are positioned in front, non-fighters behind

**Overload Systems Verb:**

- When the overheating exhaust dispatch begins, uses spare energy cell inventory item to overload Omegatock's systems

### Player Notes

- Keep spare energy cells in inventory for the overload mechanic

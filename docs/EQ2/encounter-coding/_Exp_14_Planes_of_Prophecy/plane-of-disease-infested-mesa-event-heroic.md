# Plane of Disease: Infested Mesa [Event Heroic]

**Expansion:** Planes of Prophecy (Exp 14)

This zone has 2 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [The Carrion Walker](#the-carrion-walker) | Organ failure cancellation in correct order |
| [Grimror](#grimror) | Larvae flesh matching and corpse clicking |

---

## The Carrion Walker

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight where organ failures must be cancelled in the correct order.

### What the Module Does

**Organ Failure Cancellation:**

- Detects three organ failure debuffs (Brain, Heart, Stomach)
- Cancels them in the correct priority order: Brain first, then Heart, then Stomach
- Only cancels when the matching special actor is present

### Player Notes

- The organ cancellation sequence is fully automated

---

## Grimror

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight where the correct character must click a matching larvae corpse.

### What the Module Does

**Larvae Flesh Matching:**

- Tracks which flesh type the boss currently has (scaevian, harrion, generian, or sengian)
- When a character's Host debuff matches the current flesh type, that character moves to the matching larvae corpse and clicks it
- Returns to camp spot after clicking

### Player Notes

- The module matches characters to the correct corpse automatically based on their Host debuff

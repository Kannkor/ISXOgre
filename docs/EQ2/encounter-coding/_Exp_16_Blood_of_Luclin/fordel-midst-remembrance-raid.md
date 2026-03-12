# Fordel Midst: Remembrance [Raid]

**Expansion:** Blood of Luclin (Exp 16)

This zone has 4 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Nhekrin](#nhekrin) | General placement with jousting and light pillar avoidance |
| [Portabellius Shrieker](#portabellius-shrieker) | Acid spawn avoidance with dynamic safe-spot calculation |
| [Vestigial Broker](#vestigial-broker) | Reads named's guild text to move group to correct merchant cart |
| [Palomidiar Allakhaji](#palomidiar-allakhaji) | Zone-specific bookcase interaction |

---

## Nhekrin

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A placement and jousting encounter where fighters get a separate tank position and the raid must avoid pillars of light that spawn as ring AoEs.

### What the Module Does

**General Placement:**

- Fighters receive a separate tank position
- All other players are placed at a raid position

**Pillar of Light Avoidance:**

- When a pillar of light spawns (ring AoE), the module detects the danger zone
- The raid automatically repositions to the camp spot furthest from the pillar

### Player Notes

- Fighters and non-fighters are positioned separately.
- When light pillars appear, the group automatically moves to the safest location.
- Stay with the group repositioning -- do not manually run away from pillars.

---

## Portabellius Shrieker

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

An encounter where acid spawns at multiple locations and the group must quickly move to the safest available position.

### What the Module Does

**Acid Spawn Avoidance:**

- When acid spawns, the module calculates the safest position from the 4 acid spawn points
- It finds the 2 closest acid spawns and moves the group to the midpoint between them (the location furthest from danger)
- Once the acid phase is over, the group repositions back to normal

### Player Notes

- The safe-spot calculation is automatic -- the module finds the best position relative to all acid spawns.
- You will be moved during the acid phase and returned to position once it clears.

---

## Vestigial Broker

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

An encounter where the named's guild text indicates which merchant cart the group must move to. The module reads this text and repositions the raid to the correct cart automatically. Challenge mode (Vestigial Poltergeist) is supported.

### What the Module Does

**Merchant Cart Identification:**

- Automatically reads the named's guild text (e.g. "Wearing Amethyst Ring") to determine the correct cart
- Supports all five cart types: Amethyst, Ruby, Emerald, Amber, and Sapphire Inlaid Merchant Cart
- Moves the entire group to the correct cart and targets it

**Challenge Mode:**

- Fully supports the Vestigial Poltergeist challenge mode variant

### Player Notes

- The module handles cart identification and group movement entirely on its own.
- All five merchant cart types are supported.
- Challenge mode (Vestigial Poltergeist) uses the same automation.

---

## Palomidiar Allakhaji

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

An encounter that involves interacting with bookcases in the environment.

### What the Module Does

**Bookcase Interaction:**

- The Special Zone Specific button will push on bookcases (interactable objects near the player)

### Player Notes

- Use the Special Zone Specific button to interact with nearby bookcases when needed.

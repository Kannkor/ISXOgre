# Aether Wroughtlands: Native Mettle [Heroic III]

**Expansion:** Ballads of Zimara (Exp 20)

This heroic zone contains 5 boss encounters. Several encounters in this zone require significant manual player interaction alongside the automation.

> **:information_source: Forum Resource**
>
> For detailed strategies and discussion, visit the [OgreBot Forums](https://forums.ogregaming.com/viewforum.php?f=8).

## Available Setups

| Boss | Description |
|------|-------------|
| [The Aurum Outlaw](#the-aurum-outlaw) | HO automation with manual add pulling |
| [Nugget](#nugget) | Manual harvesting and node movement |
| [Coppernicus](#coppernicus) | Manual add and boss pulling |
| [Goldfeather](#goldfeather) | Manual box collection |
| [Goldan](#goldan) | Manual pad positioning with dual setup |

---

## The Aurum Outlaw

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with automated HO management but requiring manual add pulling. The module handles several automated mechanics while the player manages positioning.

### What the Module Does

**Heroic Opportunity (HO) Management:**

- Fighters are flagged to manage Window of Opportunity HOs
- Scouts are flagged to manage Scout's Honor HOs
- HO automation runs throughout the fight

**Bulwark of Order:**

- Fighters automatically cast Bulwark of Order

**Named Stacks HUD:**

- Displays a HUD indicator showing the current stack count on the named

**Curse Handling:**

- Quick curse handling is enabled for the fight

### Player Notes

- **YOU** need to pull the adds manually
- HOs are handled automatically by fighters and scouts
- Watch the HUD display for stack counts on the named

---

## Nugget

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight requiring manual harvesting and movement to nodes.

### What the Module Does

- Basic fight setup and targeting

### Player Notes

- **YOU** need to harvest and move to the nodes manually
- The module provides basic automation but the core mechanic requires player interaction

---

## Coppernicus

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight requiring manual pulling of adds and the boss.

### What the Module Does

- Basic fight setup and targeting

### Player Notes

- **YOU** need to pull the 4 adds, then pull the named
- Follow the correct pull order for the encounter

---

## Goldfeather

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight requiring manual box collection and pulling.

### What the Module Does

- Basic fight setup and targeting

### Player Notes

- **YOU** need to get the boxes, then use one to pull the named
- The module provides basic automation but the core mechanic requires player interaction

---

## Goldan

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight requiring manual pad positioning with a dual setup sequence.

### What the Module Does

- Basic fight setup and targeting
- Requires running the setup twice before engaging

### Player Notes

- **YOU** need to get to the pads and run setup twice (`SetUpFor` x2) before aggroing the named
- The dual setup ensures all positioning is correctly configured

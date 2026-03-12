# Temple of Veeshan: Laboratory of Mutation [Heroic]

**Expansion:** Tears of Veeshan (Exp 10)

This zone has 2 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Experiment](#experiment) | Positioning |
| [Gangel the Resurrected](#gangel-the-resurrected) | Helper script management |

---

## Experiment

Setup command: `Set up for Experiment`

### Overview

A positioning-only setup.

### What the Module Does

**Positioning:**

- Sets a single raid spot for everyone

### Player Notes

- Positioning only, no mechanic automation

---

## Gangel the Resurrected

Setup is automatic when engaged.

### Overview

A fight managed by an external helper script.

### What the Module Does

**Helper Script:**

- When Gangel spawns, fighters start the `ogre tov_gangel` helper script
- When Gangel despawns, the helper script is stopped

### Player Notes

- The main mechanic handling is done by the external helper script

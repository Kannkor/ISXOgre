# The Venom of Ssraeshza [Event Heroic]

**Expansion:** Blood of Luclin (Exp 16)

This event heroic zone contains 2 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Rhag'Sekez](#rhagsekez) | Crystal color mechanic with tank movement and phase targeting |
| [Rhag'Voreth](#rhagvoreth) | Color scale mechanic with auto-movement and add targeting |

---

## Rhag'Sekez

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A crystal color encounter where the boss gains Red or Blue buffs from nearby crystals. The tank must move the boss toward the opposite-color crystal to remove the buff. The fight alternates between crystal phases and kill phases.

### What the Module Does

**Camp Spot Requirement:**

- Use camp spot to enable movement during the encounter
- Do NOT use camp spot if you want no movement

**Crystal Color Management:**

- Monitors the named for Red and Blue crystal buffs
- When the named has a **Red buff**, the tank moves it toward the Blue crystal
- When the named has a **Blue buff**, the tank moves it toward the Red crystal
- When the named is **Balanced** or has no buff, the group attacks normally

**Phase-Based Targeting:**

- During crystal phases, the module self-targets to prevent DPS while the tank repositions
- During kill phases, the module retargets the named for the group

**HUD Display:**

- Displays HUD messages showing the current phase and crystal color status

### Player Notes

- The tank movement between crystals is fully automatic.
- During crystal phases, the group will stop DPS automatically until the boss is in position.
- Watch the HUD messages for current phase information.

---

## Rhag'Voreth

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A color scale encounter where the boss gains detriments tied to specific colors. The group must move to the matching color location to deal damage. The fight involves continuous repositioning as the boss cycles through different scale colors.

### What the Module Does

**Scale Color Detection and Movement:**

- Detects which scale detriment the named currently has: Silver, Green, Orange, or Purple
- Automatically moves the entire group to the corresponding color location:

| Scale Color | Location |
|-------------|----------|
| Silver | Black/white area |
| Green | Blue + yellow area |
| Orange | Red + yellow area |
| Purple | Red + blue area |

- Fighters alternate sides when the group is already near the correct position

**Add Targeting:**

- During movement phases, the module targets sentry adds for the group

**Default Positioning:**

- When no scale detriment is active, fighters are positioned in front of the named and non-fighters behind

**Post-Fight Cleanup:**

- After the named despawns, the module repositions the group

**HUD Display:**

- Displays HUD messages showing the current scale color and target location

### Player Notes

- Movement between color locations is fully automatic. Do not move manually.
- Watch the HUD for the current color and location information.
- Sentry adds are targeted automatically during movement phases.
- After the boss despawns, the group is automatically repositioned.

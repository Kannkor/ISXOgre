# Encounter Coding

OgreBot includes fight-specific automation modules for many EverQuest 2 dungeon and raid encounters. These modules handle boss mechanics automatically -- jousting, target switching, clicking objects, curing detriments, managing positioning, and more.

This section documents what each encounter module does, which setups are available, and any requirements your group needs to meet.

---

## Supported Expansions

| Expansion | Zones |
|-----------|-------|
| Rage of Cthurath (Exp 22) | See below |

### Rage of Cthurath (Exp 22)

| Zone | Type |
|------|------|
| [Gerion: Ark of Ascension [Untold Heroic]](_Exp_22_Rage_of_Cthurath/gerion-ark-of-ascension-untold-heroic.md) | Untold Heroic |
| [Gerion: Captive Audience [Raid]](_Exp_22_Rage_of_Cthurath/gerion-captive-audience-raid.md) | Raid (WIP) |
| [Gerion: Dominion of Pain [Untold Heroic]](_Exp_22_Rage_of_Cthurath/gerion-dominion-of-pain-untold-heroic.md) | Untold Heroic |
| [The Unknown: Edge of Oblivion [Untold Heroic]](_Exp_22_Rage_of_Cthurath/the-unknown-edge-of-oblivion-untold-heroic.md) | Untold Heroic |
| [The Unknown: Sacrificial Pursuits [Untold Heroic]](_Exp_22_Rage_of_Cthurath/the-unknown-sacrificial-pursuits-untold-heroic.md) | Untold Heroic |
| [Yon Gorroth: The Infinite Abyss [Raid]](_Exp_22_Rage_of_Cthurath/yon-gorroth-the-infinite-abyss-raid.md) | Raid |
| [Yon Gorroth: Voidshell Caverns [Raid]](_Exp_22_Rage_of_Cthurath/yon-gorroth-voidshell-caverns-raid.md) | Raid (WIP) |
| [Zon Zobboz: Gaze of the Oglth [Raid]](_Exp_22_Rage_of_Cthurath/zon-zobboz-gaze-of-the-oglth-raid.md) | Raid |
| [Zon Zobboz: The Chimeric Chain [Untold Heroic]](_Exp_22_Rage_of_Cthurath/zon-zobboz-the-chimeric-chain-untold-heroic.md) | Untold Heroic |
| [Zon Zobboz: The Graftwerk [Untold Heroic]](_Exp_22_Rage_of_Cthurath/zon-zobboz-the-graftwerk-untold-heroic.md) | Untold Heroic |
| [Zon Zobboz: The Outer Swarmyard [Raid]](_Exp_22_Rage_of_Cthurath/zon-zobboz-the-outer-swarmyard-raid.md) | Raid |

---

## How Encounter Modules Work

Encounter modules are loaded automatically when you zone into a supported instance. Setup is automatic when the boss is engaged. You can also use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to trigger the setup immediately. The module then monitors combat and handles mechanics in real time.

Each boss encounter may have:

- **Camp spots** -- Positions where characters are placed during the fight
- **Flags** -- Role assignments for specific mechanics (e.g., who handles a debuff)
- **Auto-target rules** -- Which mobs to prioritize and when
- **Detriment tracking** -- Monitoring and responding to specific debuffs
- **Phase handling** -- Adjusting behavior as the fight progresses

> **:memo: Setup**
>
> Setup happens automatically when the boss is engaged. You can also use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to trigger the setup immediately before pulling. This configures camp spots, flags, and UI settings for the fight.

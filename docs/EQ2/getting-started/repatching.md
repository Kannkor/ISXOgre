# Repatching ISXOgre

ISXOgre uses OgrePatcher to keep all files up to date. The patcher automatically scans every file it needs each time you load ISXOgre.

---

## Automatic Patching

Simply opening a new EQ2 session and loading ISXOgre will automatically check for and apply any needed patches. In most cases, you do not need to do anything special.

---

## Manual Repatch

If you are already in-game and need to force a repatch without restarting:

1. Open the InnerSpace console (press `~`)
2. Type the following command and press Enter:

```
ext -unload isxogre && timedcommand 10 ext isxogre
```

This unloads ISXOgre and reloads it, which triggers the patcher to rescan all files.

<!-- Source: wiki.ogregaming.com/eq2/index.php/Help:Repatch -->

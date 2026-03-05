# Removing Memory and FPS Display

By default, InnerSpace shows memory usage and FPS counters in the top-left corner of your screen. These are InnerSpace features, not ISXOgre features. Here is how to hide them.

---

## Steps

1. Right-click the InnerSpace icon in your system tray and select **Configuration**
2. Under **Session** (not Uplink), click **Startup** (not Pre-Startup)
3. Select the entry you want to hide -- either **Memory Indicator** or **FPS Indicator**
4. Change `-show` to `-hide`
5. Click **Apply**, then **Accept**
6. Close all EQ2 sessions and restart InnerSpace for the change to take effect

> **:bulb: Keep the Entry**
>
> Changing `-show` to `-hide` is better than deleting the entry entirely. This way you can easily re-enable the display later by changing it back to `-show`.

<!-- Source: wiki.ogregaming.com/eq2/index.php/Help:RemovingMemoryAndFPSFromSession -->

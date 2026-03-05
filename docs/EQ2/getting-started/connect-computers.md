# Connecting Computers via Uplink

If you run EQ2 on multiple computers, you can connect them through InnerSpace's Uplink feature so OgreBot can communicate across machines.

> **:memo: Note**
>
> The Uplink is an InnerSpace feature, not an ISXOgre feature. This guide covers the common setup issues.

---

## Step 1: Verify Connection Settings

1. Right-click the InnerSpace icon in your system tray and select **Configuration**
2. Check that your computer has a **unique name** that matches your actual computer name exactly
3. Confirm that **Accept incoming connections** is selected
4. If you changed any settings, click **Apply**, close EQ2 and InnerSpace, then restart both

> **:warning: Restart Required**
>
> If you had to enable "Accept incoming connections", you must fully close InnerSpace and restart it for the change to take effect.

---

## Step 2: Connect Using OgreBot

1. Open the InnerSpace console and type `ogre mcp` to open the Ogre MCP window
2. Go to the **Other** tab
3. Click **Connect** on the right side
4. Wait approximately 5 seconds
5. Click **List_IPs** to verify the connections

You should see your local computer (LOCAL HOST) and any other machines you configured in the [Uplink Info](../ogrebot/tabs/uplink-info.md) tab.

> **:memo: Reconnection**
>
> You need to reconnect each time InnerSpace is closed and reopened. Closing EQ2 alone does not require reconnection.

<!-- Source: wiki.ogregaming.com/eq2/index.php/Help:HowToConnectComputersViaUplink -->

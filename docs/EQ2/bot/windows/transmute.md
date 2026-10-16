# Level Transmuting

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../index.md).
</div>

> **:bulb: In game - the ? button on this window says**
>
> Levels your Transmuting skill: buys cheap transmuter's stones from Barnaby Blunderbuss in Butcherblock and transmutes them, round after round.
>
> **What you can do here**
>
> - **Buy** sets how many stones to hold after each visit. Leftover stones are used first.
> - **round(s)** is the most visits one run makes. The run also stops when your skill is capped.
> - **Start** begins the run. **Stop** ends it. **Refresh** redraws the window.
> - **Buys** shows the merchant visits and how many stones they really added.
> - **Transmutes** shows how many stones were tried and how many really got used up. If any failed, it says why: the cast was refused, the ability never became ready, or the stone was still there afterwards.
>
> **Good to know**
>
> - Start pauses OgreBot for the run. When the run ends it resumes OgreBot, unless OgreBot was already paused.
> - Start opens the Persona window on Skills > General to read your skill. It closes it again when the run ends, however it ends.
> - Not next to Barnaby? The window tells you, and Start travels to him first, even with OgreBot closed. Stop ends the trip.
> - Each stone costs 1 Gnomish Currency Exchange, not coin. Without any, the buy adds nothing and the run stops and says so.
> - Only items named "Transmuter's Stone" or "Transmutation Stone" are ever transmuted.
> - A round that buys nothing, or transmutes nothing, stops the run, so a problem never repeats for every round.
> - Closing this window does not stop a run.

**Open it:** Type `ogre leveltransmuting panel` (or `ogre lt panel`). Plain `ogre lt` only prints the status to the console. `ogre end leveltransmuting` stops a run but leaves the window open.

[![Level Transmuting](../assets/transmute/window.png)](../assets/transmute/window.png "Click for full size")

## What it is for

A skill-up grinder for the Transmuting tradeskill. You stand next to Barnaby Blunderbuss in Butcherblock. The bot buys Minor Lapis Lazuli Transmuter's Stones from him, transmutes them, and repeats until your Transmuting skill is capped or the round limit is reached. It only ever transmutes items whose name contains "Transmuter's Stone" or "Transmutation Stone" - nothing else in your bags is touched. It never walks: if you are not within 10 of Barnaby, it stops.

## Header and the stones-only notice

The dot is green while a run is going. Next to it is what the bot is doing right now.

[![Header and the stones-only notice](../assets/transmute/header.png)](../assets/transmute/header.png "Click for full size")

## The readout

Merchant and Item are fixed - the tool only works with Barnaby and his cheapest stone. Transmuting is your skill as last read from the Persona window (it is read once at the start of each round, so it shows unavailable until a run has started). Rounds counts merchant visits out of the most you allowed. Transmuted is how many stones this run has transmuted so far. Last is the latest thing that happened.

[![The readout](../assets/transmute/readout.png)](../assets/transmute/readout.png "Click for full size")

## Quantity and round limit

[![Quantity and round limit](../assets/transmute/controls.png)](../assets/transmute/controls.png "Click for full size")

| Control | What it does | Default |
|---|---|---|
| **Buy** | How many stones you want to be holding when each visit to Barnaby is done. The bot only buys the difference, so stones left over from the last round are used first. 1 to 800.<br>*Locked while a run is going. It is a total to hold, not an amount added every round.* | 60 |
| **per visit, at most ... round(s)** | The hard stop: the most merchant visits one run will make. The run also stops earlier if the Transmuting skill is readable and capped. 1 to 500.<br>*If the skill cannot be read, this is the only thing that stops the run.* | 20 |

## Start, Stop, Refresh

[![Start, Stop, Refresh](../assets/transmute/controls.png)](../assets/transmute/controls.png "Click for full size")

| Control | What it does |
|---|---|
| **Start** | Starts a run with the two numbers above. Each round: read your Transmuting skill, check Barnaby is within 10, buy up to the Buy amount, then transmute every stone in your bags (at most 200 per round), 2 seconds apart.<br>*Greyed out while a run is going. Stops by itself if you do not have the Transmuting ability, or after 3 rounds in a row where the merchant purchase failed.* |
| **Stop** | Stops the run straight away, even in the middle of buying or transmuting.<br>*Only active while a run is going.* |
| **Refresh** | Redraws the window with the latest numbers. It does not change anything. |
| **Title bar close (X)** | Closes the window only. A run that is going keeps going.<br>*Use Stop (or `ogre end leveltransmuting`) to stop the run.* |

## When the skill cannot be read

The bot reads your Transmuting skill from the Persona window, Utility skills tab, once at the start of every round. It never opens that window for you. If it is not open, Transmuting shows 'unavailable' in orange and a note appears; the run then stops only at the round limit. Before the first round of a run the skill has not been read yet, so the window also shows 'unavailable' and the note even when the Persona window is open.

[![When the skill cannot be read](../assets/transmute/skillhint.png)](../assets/transmute/skillhint.png "Click for full size")

## What the window shows

- Dot and phase text (top right): green dot = running. Phase is one of idle, waiting for the world, reading the Transmuting skill, looking for the merchant, buying, transmuting stones, BLOCKED - cannot transmute, stopped.
- Box at the top: always there. It says the tool transmutes Transmuter's and Transmutation stones only, and that other items are transmuted by the Inventory Manager (`ogre im -tse`).
- Transmuting: 'current / max' in green from the last round's read of the Persona window's Utility skills tab; 'unavailable' in orange when it could not be read, or when no round has run yet.
- Rounds: 'N of M (buys issued: B)' - merchant visits started out of your limit.
- Transmuted: 'N stones this run' - stones transmuted since Start.
- Last: the latest step or the reason the run stopped, for example 'Unable to find  Barnaby Blunderbuss' or 'Transmuting is at its cap for this level'.
- Footer: a reminder that the tool never walks and that the skill is read passively.

## Good to know

- Stand within 10 of Barnaby Blunderbuss (Butcherblock) before pressing Start. If he is further away the run stops at once with 'Unable to find  Barnaby Blunderbuss'.
- Open the Persona window on the Utility skills tab first, or the run cannot tell when your skill is capped and will use every round you allowed.
- Before you press Start, Transmuting always shows unavailable - the skill is only read when a round begins, and Refresh does not read it.
- Buy is a target to hold, not an amount per round. If stones were left over, the next visit buys fewer (or none).
- Any item whose name contains "Transmuter's Stone" or "Transmutation Stone" is transmuted, not just the ones this tool bought.
- Closing the window does not stop a run.
- Plain `ogre lt` prints the status; add `panel` to open the window.

## When the Persona window is closed

![Stopped, with the skill unreadable](../assets/transmute/idle.png)

Without the Persona window open on the Utility skills tab, the skill reads **unavailable** and the round limit is the only stop. It also reads unavailable before your first run, because the skill is only read when a round starts.


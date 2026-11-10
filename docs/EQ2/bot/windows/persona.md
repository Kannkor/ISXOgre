<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../index.md).
</div>

# Persona

> **:bulb: In game - the ? button on this window says**
>
> Say which profile file each class uses on this PC, for example all rangers use `master_ranger.json`. A new character in a class with no rule starts from the class sample.
>
> **What you can do here**
>
> - **Server** narrows the rules to one server. Blank means every server. A short form like `ior` works.
> - **Pick a file** on a row sets the rule for that class. **All** is the rule for every class, on every server.
> - **Clear** forgets a rule.
> - **Characters that override a rule** lists those whose own setting beats a rule shown here. **Clear** puts one back on the rules.
>
> **Good to know**
>
> - A change applies the next time that class loads.
> - One character's own setting is on the **Persona** tab in OgreBot.
> - `ogre end persona` closes this window.

**Open it:** Type `ogre persona`, or press Open Persona window on OgreBot's Persona tab. If the window is already open, this does nothing. `ogre end persona` (or the window's X) closes it.


## What it is for

A persona is one character in one class. This window says which profile file a class uses on this PC, for example all rangers use `master_ranger.json`. A rule can cover every server or one server. A character with no rule and no setting of its own starts from the sample profile for its class. One character's own setting, which beats these rules, is on the Persona tab in OgreBot.

## Which rules are shown

The Server box says which rules the rows below are for.


| Control | What it does |
|---|---|
| **Server** | Blank shows and sets the rules for every server. A server name shows and sets the rules for that server only. A short form like `ior` works. |
| **Show** | Shows the rules for the server in the box, and reads the routing file again. Enter in the box does the same. |



## Rules

One row for All and one for each of the 26 classes. Each says which file it uses now.


| Control | What it does |
|---|---|
| **Pick a file** | Sets the rule for this class to a profile file from your Main profiles folder. The All row is the rule for every class that has no rule of its own, and it has no server form. |
| **Clear** | Forgets this rule. |



## Characters that override a rule

A character listed here has its own setting for a class that has a rule shown above, so the rule does not reach it.


| Control | What it does |
|---|---|
| **Clear** | Forgets this character's own setting, so it follows the rules again. |



## What the window shows

- A row with no rule says what happens instead: another rule that still applies, or that it starts from the class sample.
- The footer shows what the last button did.

## Good to know

- A change applies the next time that class loads. A character already on that class is not changed until then.
- With every server shown, a character with its own setting counts as overriding the All rule too.
- A character's own setting wins over any rule here. It is set on the Persona tab in OgreBot.
- Every character on this PC shares these rules (OgreSave/EQ2/OgreBot/Profiles/Routing.json).


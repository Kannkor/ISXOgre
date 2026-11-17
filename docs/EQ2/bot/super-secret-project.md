# The super secret project

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../index.md).
</div>

Where to even start! I guess a super brief history of how OgreBot became to be. I'd guess the basics of my story was the same as most people's here. A friend wanted me to play eq2 with them (they wanted me to make a bot, as I had done so for eq1). I said sure, but I was ONLY playing 1 toon. Pretty sure I made a troubadour. I was coding at low levels but it was hard back then. It logically only made sense, to have a second account for a priest. It's only 2 accounts, that's basically just 1 account.

Then I was killing slow... so may as well add some dps to the group... 3 accounts is barely more than the 2 I already have. It's only 1 more. Yes, you can absolutely hear the "justification" to myself about how this is all fine. The friend who got me into eq2, I'm pretty sure at this stage, is absolutely laughing his ass off, because he new this would happen, and he knew exactly what was coming next.

Well, if I'm already at 3, then I may as well just have my own group. Then there were 6.

Okay, fast forward almost 20 years or something now. Lax/Innerspace comes out with LGUI2 (it's what OgreCraft2's UI is done in). It provided a TON more options for dealing with GUIs, but LGUI2 isn't very friendly. I find it way over complicated, it was very new, so minimal documentation or examples. I made it work, but still didn't like it.

Then others, decided to bring in external GUIs. I thought this was an interesting idea, but the problem is, EVERYTHING is tied to my current GUI, that changing would be an absolute nightmare. It would basically be a rewrite of Ogrebot... and for what? To change the GUI?

Then a friend (don't tell him I called him that) and I were talking and joking... How long would it take, to rewrite Ogrebot from scratch, and make it work with a new GUI. With basically full parity (meaning, no loss of features). Our estimate was over a year. That assumes I focus the majority of my time there. That was absolutely not going to be worth it. Full stop, no thanks.

I didn't want to code untolds above tier 20, because Dominion of Pain sucks, so I was looking for a way to distract myself. I thought I'd look into these alternate GUIs to run some performance bench marks. If a new fancy GUI would be a net loss in performance, that's not worth it, at all. FPS (frames per second, not first person shooter) is way more important than having a fancy dancy GUI.

Did a bunch of research, and choose one. It is built using HTML (basically a webpage). This is fantastic, because HTML is likely the most common language ever (I didn't actually check to see if that's true, but almost every single website uses html). That means there's infinite amount of examples, and support etc etc.

I figured, okay, lets load this up, see how it works, do some performance tests, then go from there.

A WEEK LATER, I finally get it working. Like... me working on it every spare moment I have for an entire week. I was ready to bash my head into a wall.

Now that I've wasted a week, figured I should do some performance tests. I figured sink or swim new GUI. I created 3 identical GUIs. One in LGUI1, one in LGUI2, and one in this newGUI. They had something like 50 checkboxes, 50 labels etc.

I then had the same script monitor the fps while idle, then I started sending information to them every frame (this isn't realistic, but it's a good test). It was doing I think almost 200 changes to the GUI every frame. (a label that goes from 1, to 2, to 3, sliders going up like a progress bar etc). I figured put it under stress and see what happens.

Here's the results (higher numbers are better)

Static:

NewGUI: 45.7

LGUI1: 39.4

LGUI2: 33.2

Under extreme load:

NewGUI: 41.9

LGUI1: 36.7

LGUI2: 26.1

Well, that tells two stories. LGUI2 is bad on performance, is difficult to work with, and is in the garbage.

NewGUI is actually better than LGUI1 in performance, and looks better. How about that.

Okay, cool story, time to move on... ... ...

I started messing around to see what it looked like, and what it was capable of doing. Thought it would be nifty, but honestly, a rewrite of Ogrebot still was not worth it. Too time consuming.

But for a new project... maybe.

So I started a new extension, got things loaded up, but wasn't sure what new project to work on. I thought okay, I'll just re-create something of Ogre. I'll do OgreConsole, keep it simple, doesn't require any external things like isxeq2, it simply displays information.

Did that, was pretty nifty. But it was basically a listbox. I used 1 element. May as well do another window. Was curious how it could handle something like MCP. Being able to drag and resize, how it could handle right clicking with new windows, swapping buttons, frame in frame (static vs changing buttons), etc. This was going to be a good test.

It was.. overall.. pretty simple. It was HTML... webpages. Almost anything you want to do, has 25309235 examples available.

Okay, so the GUI works. How am I going to make it actually usable. I've always known that lavishscript is "slow" overall, and here I am using an extension written in c++ (which is very fast). Well, lets go down that road a little bit, and see if I can figure out how to do more stuff in c++, then start testing performance, to see where this goes. As you can tell, performance is likely the highest priority I have. I want more FPS, and never want to lose any FPS. Could I move any big number crunching, into c++. For example, there's HUNDREDS of checks for Ogrebot to find an ability it wants to cast from the caststack. I start down that road....

Okay, have a mock of that working, but the real test is having an actual cast stack. Well, what if we just made a little mock up of Ogrebot's GUI, then loaded the caststack in, and see how it goes.

Well, in order to have a usable caststack, you need an export, so gotta load that up too.

Here's where it became very obvious to me. Loading the export in lavishscript, you know when you load ogrebot, and it has that bed red message of "Loading..." on top of the GUI, most of that time is loading the export and pulling it apart (finding the highest ability etc). It's something like 2-5 seconds.

I have the export in c++, and did the same thing, had it pull out the highest abilities etc. I load it... it loads. Like.. instantly. Okay, I must have missed something... oh no. It's done.. instantly.

Pretty sure I pivoted, and started running tests. Just simple tests.

In lavishscript, doing ${Me.Name}, ${Me.Health}. Doing it both in lavish and in c++. Ran them a few hundred thousand times, turns out c++ does them 3 to 10 times faster (depending, string vs int etc). Everything, is just insanely faster in c++. Okay, how much can I do solely in c++?

Apparently, I started rewriting Ogrebot, in c++, as kind of a, lets see how this goes. Every time I ran performance tests, with the new GUI, and c++, it absolutely destroyed lavishscript and LGUI1 (that's what Ogrebot is currently in). Apparently I was going down this rabbit hole, that I said was not worth it at all.

I had to take a pause and started thinking. Okay, if I'm doing this, it's going to break *EVERYTHING*. Every single side script out there that touches my GUI. If I'm basically re-doing it in c++, that's going to break OgreBotAPI... breaking everything. I had to decide, am I okay with breaking everything? If I'm going to break things, then I may as well fix things too. For example, I'm sure you've all heard of the famous "ForWho". That decides who listens to the various commands. Almost everything has a forwho... but did you know, 27 things either did not have a forwho, or had it in the wrong spot? But i couldn't change it, because it would break things. GUESS WHAT! I'M ALREADY BREKAING THINGS!

I still have not told anyone except my "friend" that got me into this mess. He was sworn to secrecy, because I knew where he lives. Well.. I know he lives in USA.

At the time of writing this portion of this, I'm still a long ways away from having something for alpha testers. Most of the important subsystems are built. The caststack, campspot, mcp, ogreconsole, osa. 100% within c++, and all with this new fancy html GUI. It's super speedy! And as I have been going along, I have been trying to put together a list of "what do I think works well" and "what needs improved". There are some seriously cool QoL (quality of life) features. I'll document them as I get there, but most of them you will be able to find on your own.

So, what does this mean for the future of Ogre? It's changing with the times. It's getting a complete overhaul. A face lift (new GUI), and complete back end rewrites.

Here's the short "good and bad" about this.

The good:

New, modern GUI that is much easier to use, and more familiar for people.

FPS increase, although I'm not going to hold my breath until I get more and am able to use it in a zone etc.

Everything has it's own TLO and datatypes, and for scripters, this means you can LSTYPE things! (if you're not a scripter, this won't mean anything).

The bad:

Every single script/side script out there, will stop working immediately. While this is really unfortunate, it was the only way to do this project. I'm going to have documents that explain, with examples, of how scripts can be updated to a new format that will work (basically instead of calling the GUI this way, you do it this way).

I will also do my best to help people who have scripts, but got them from people who no longer play, and help you convert them.

People will need to "learn" a new GUI, but I honestly don't think this will be a big deal. It looks modern, but the same. Once you see it, you'll understand.

That's it for now. I would like to say, I have learnt my lesson.. by putting off doing untolds, I ended up with a much, much bigger project on my hands... but I have definitely not learned anything from this...

&lt;fast forward like 2 months&gt;

It's Oct 14th, 2026. I have said I am going to add some testers this week. So.. this is coming out for people to see and test, REAL soon.

Anyone who was paying attention to my clues I was giving, one of them was this, a common phrase I say:

`____ _______`

4 letter word, space, 7 letter word. Only 1 person got it. I think everyone got caught up, on the 4 letter word had to be "ogre", but it wasn't.

It was "full rewrite". One person did guess "ogre rewrite", which was half right, I suppose.

Which then leads to a question of "full rewrite of what?", and the answer to that, is "EVERYTHING".

Now, lets talk about what, everything means. Oh, it means everything. Every, single, thing.

From authentication, to ogrebot, to craft (yes, another rewrite), to mcp, etc etc. When you are rewriting things, you know what that means? UPGRADES! So many things, got upgrades. When in doubt, right click.

I took 20 years of Ogre content, and rewrote all of it. Was it worth it? I guess in the end, that depends on how you all think of it. So far, I am very pleased with it.

P.S. the writing of this, was done entirely by me, with no AI.

P.S.S. Of course, when I say "this", I mean this specific document only :)

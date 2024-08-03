# The-Adventure-Oracle

This is a pretty simple python script really. You can find instructions to install python at [https://www.python.org/](https://www.python.org/).

Then download a copy of this repository to a folder on your hard drive. Click on the green Code button and select download zip will work. Or click here: [https://github.com/GilgameshofUT/The-Adventure-Oracle/archive/refs/heads/main.zip](https://github.com/GilgameshofUT/The-Adventure-Oracle/archive/refs/heads/main.zip) Then extract it somewhere.

Open a command line and go to the folder where you saved the files from this repository.

Run:

python adventure\_oracle.py

That should be it.

It will open a menu on your screen and output both to your screen and also to a markdown file in the logs directory. This file is in markdown and should read fine in Obsidian or other markdown readers. There is a sample output there if you want to have a look. Feel free to delete it if you are starting over with your own adventure.

It has two two starting adventures currently. I will be adding more as time permits but you can easily make your own.

One is a space opera fit for a crew of explorers from a 1960s TV show.

The other is a horror murder mystery "Tockley Manor" by Tana Pigeon of [https://WordMillGames.com](https://WordMillGames.com) published in Mythic Magazine Volume 11\. Used with permission.

**Update**: I have added an incredibly huge new adventure based on the first 15 chapters of the public domain book *A Princess of Mars* staring the great pulp hero John Carter of Mars. As well as instructions for how I created it and how you can create your own based on modules you own or obtain for free on the internet. If there is interest I may add some more modules based on public domain stories. Feel free to let me know if there is a particular adventure that interests you. Public domain works can be found at Project Gutenberg.  

# So What does it do?

I would encourage you to start with buying Mythic Magazine vol 11 from DriveThroughRPG and reading Tana's excellent article where she explains this system in depth. The goal is to play written modules solo. What she produces there might be more described as writing modules for solo play as an existing module will need a bit of work to convert it to this system but the end result is pretty nifty. It combines her excellent Mythic GM Emulator with her Location Crafter and uses a series of tables to capture some of the creative feel of solo RPG but also the planned structure of a written module.

I will write a longer introduction when I have time but Tana's example is excellent and it was what I started with when I was coding this. It immediately struck me that most of the hard work involved could be automated by converting all the charts to JSON and using some simple python logic to simulate the draws. This simplifies a lot of bookkeeping for the user. It also opens a world of possibility for solo play on modules written by someone else where you can truly follow a well planned story without spoilers and without a GM. It could also do a lot to act as a GM or assist a GM for a group, majorly reducing prep time.  There is some fun stuff she adds to it to increase the probability of drawing from the early parts of tables in the early game and working your way down as things progress. I did some interesting things to capture this mechanic in a slightly different way but it works out the same. Some of the statistical odds changed a bit and I will likely still tweak them further to get the feel I want.

Basically you begin with a detailed opening scene to jumpstart the adventure, possibly including some NPCs you may already be introduced to and some threads that are already established as this is common for written modules. Tana ties her example closely to Mythic's mechanics but it should not be hard to swap it out for many popular oracles. Although I have to say Mythic is a great system. Almost everyone doing solo RPG is at least familiar with it and many systems imitate it to varying degrees. It is perhaps a bit on the “crunchy” side for some people, but many really enjoy its detailed structure.

So when you launch the program it gives you a list of files in the adventures directory. One file per written module. select the one you want to play. It then outputs the opening scene and initial thread and character list. Mythic has built in mechanics to use such lists, but so do many other oracle systems. Capture these lists with your oracle and continue to build and use thread and character lists as you normally would. This information isn't repeated by the program and might or might not reference these elements directly. The program is not designed to update these lists for you. They are just to help you get started. Your oracle should bring them back into focus with your play through the regular mechanics of random events it provides.

Throughout the playing of the adventure it is highly recommended you combine this tool with another oracle such as Mythic, Game Master’s Apprentice, MUNE, One Page Solo Engine, or another similar system. The intent of the program is to provide structure to the story. There will still be plenty of other questions to ask an oracle. Of course you will likely want to use a TTRPG system as well to give your game rules. Savage Worlds, Dungeon World, and ICRPG are some of my favorites, but there are hundreds of great ones out there to explore and find something that fits your playstyle and setting.

Your adventure is divided into regions which contain areas. A region may be a town. The areas would then be shops, parks, houses etc. that you might visit while in this region. Your region may be a building. Then the areas would be the individual rooms. Your region may be a forest. Then areas might be a particular clearing or thicket. You get the idea. 

Each area has three elements that define it:

- location  
- encounter  
- object

As you move to a new area in the region, the program will give you information on these three elements. use that to create your scene. Use your RPG rules and Oracle to play out the scene as appropriate. Feel free to journal what you are doing in the same markdown file the program outputs to. It should work fine. When it is time to move to a new area consult the program again. It will give you three new elements. You may always revisit areas you have been to. There is no need to interact with the program when doing so. Use your Oracle and RPG rules to determine if anything changed or if a wandering monster showed up or whatever. You must fill in the logical gaps of traveling between areas, but usually they should make sense being close to each other.

At some point you will discover a new region. A haunted mansion to explore or a cave to delve. Once this happens you will have a new menu option to travel to a new region. Use your RPG rules to handle travel if that is important in your game. As before you may travel back to a known region/area. The program saves its state of each region so if you leave a region and then return to explore more, it picks up where it left off. You can also close and reopen the program and resume where you were. A file is created in the state directory to keep track of things.

Additionally another mechanic Tana uses is Keyed Scenes. These are scenes that really must happen to advance the story (basically railroading). These keyed scenes are tied to a region and will only occur there. Tana used some fun mechanics that I have approximated in the program to control when these fire. When a keyed scene fires, try to work it into the current context. If it doesn't fit well, then I guess you now have two scenes to roleplay.

There are some special elements: Expected, Random, Special, and Weird. These are included to have your oracle determine what they are. Tana gives a breakdown of each one in her article. Elements (except location) can also be “None” because sometimes a closet is just a closet.

You don't have to explore a region longer than you want to assuming you have discovered somewhere else to go. Eventually you will have explored all that was prepared and the creativity of the system will run out of juice and the elements will simply say "Complete". Probably time to move on to another region if this happens or keep it going under your own creativity.

Eventually, you will hit the end of the adventure. You will have solved the mystery, found the big bad, wooed the princess, or whatever. When this happens the resolution will be printed out. Now this could be a very definitive resolution that wraps it all up for you, but Tana presented an interesting menu of options and a mechanic to determine how it all sorts out. I like that because it leaves a lot of flexibility to the player.

I think that is enough to get you started.

# So how do I write a module

JSON is a format for structuring text data. It uses a fairly complex pattern of punctuation and parentheses, brackets, and braces that is more than I can explain here but is fully documented on other sites. AI is great at formatting and fixing JSON and there are many specialized editors that make editing it very easy. If you are not very technical, focus on editing what is inside the quotation marks. This does mean that you will need to be careful about putting quotes inside of quotes. Such things can be done by adding a backslash before the quote \\” . New lines can also be noted with a \\n and there are other conventions. Again AI is great at this sort of thing and can probably help. I plan on putting together some prompts to have AI take in a loosely formatted set of information and output it in valid JSON. I even think it might be able to write some adventures. More on that to come.

# Detailed JSON breakdown

The JSON file has the following Root level elements  
    
Root level elements:

- **firstScene**: Can be as lengthy as you like. Remember the output is going to a markdown file and you may want to write in markdown for best formatting. The only function of this element is to display this info when an adventure is started so anything needed to set the scene, explain anything unusual, introduce any context, etc.  
  - **threads**: Again this exists purely to produce an output on initialization of the adventure. The program makes no effort to update this list or reference it during the adventure. It is expected the user will take note of it and use it either editing it herself in the markdown file or placing it in some other tool to add threads as they develop and use with her preferred oracle system. It should be populated with threads introduced at the start of the adventure.  
  - **characters**: Same as threads but with characters.  
  - **regions**: This is where the magic happens. All the logic is focused here. You need to decide how many regions you want and which regions will reveal travel to which other regions.   
  - **resolution**: This is a final element that will be displayed once resolutionPossible is set to true. This actually doesn’t end the program and you can continue to play if that makes sense, but this is some text with instruction on how to wrap the adventure up and usually would be used after the big bad enters a final showdown.


  Every element has the following three subelements

  - **id**: This should be a unique number. Doesn’t really matter if you number things in order or if you skip numbers. Just used mostly to make sure each element is unique as you may commonly have multiple elements that are otherwise identical.  
  - **name**: Everything needs a name. For regions particularly this will be important as you need to refer to them by their exact name to open travel to them. This generally reflects the entry you would place on a roll table.  
  - **description**: Here is where you can add a little or a lot more detail. This can be a useful place to give ideas to the user to determine how the element described might be interpreted in your story. Remember users should be adding lots of stuff from their own oracle as they play through so keep it loose to make it easy to work into many situations, but give it enough detail that they can get a good idea of where the story should be going for important elements. Remember they wanted more structure than just a random roll table if they are using this.


  Region properties:

  - **isStartingRegion**: One region, usually the first, must have this value set to true. This is of course where the adventure starts. From here they must discover and travel to other regions (or I suppose it could all just happen in one region). How big and complex your adventure is will be determined by the number of regions and the number of sub elements in each region.

	  
	Regions have the following sub elements. All of these are “Unique” as outlined in Tana’s article. Basically once an element is used, it is crossed off the list. If you want an element to potentially occur multiple times, give it multiple entries (with a unique id number). This allows you to also control a max number of occurrences. This is a bit of deviation from Tana’s method but I think it works pretty well. Also in a bit of a deviation I didn’t make a “complete” trigger for each region. It simply goes until it runs out of elements, then it will say “complete” if more are drawn. This does mean every element will eventually fire if the user spends enough time there. I think this is a good thing and simplifies some of the needed triggers for keyed scenes. It also means that vital clue will eventually show up. This might make keyed scenes less needed overall but there will be certain times when you want to make sure multiple elements come together or more explanatory detail is given.

- **locations**: Where is this area? How can it be described?  
  - **encounters**: Can be an NPC, a trap or other danger, or a puzzle, or anything a player might interact with.  
  - **objects**: Usually something physical. Perhaps something a player might add to their inventory. Or maybe it is something fixed but interesting, such as a statue.  
  - **keyedScenes**: These are scenes that need to happen to move the story along. They are tied to the region and have two ways you can trigger them explained below.


  All four of these sub elements have the following properties:


  - **minScene**: currentScene is a number that increments every time a new area is selected for a region from the menu. This value is compared to that number and will not be selected unless the currentScene is at least this value. This emulates the mechanic of rolling a d6 and then tracking progress points to add to future rolls. On a regular sheet this puts the first 6 elements as possible at the beginning roll and pushes you further down the list as you progress, making more dramatic things happen later. As you add elements consider how late in exploration you want them to occur and set this number. That does not mean they will fire on that query but they will enter a pool of options to possibly fire then. If you want a specific element to always fire first set it and only it to minScene: 1\. Keep in mind if you have more mundane options like “None” or “Expected” and set all these to minScene: 1, you may have a large pool of uninteresting stuff clogging the beginning of your adventure. The stats work out a bit differently than the d6 method but you actually have a lot of control with this. Experiment to find what is satisfying.  
  - **newRegion**: This tag should have a value of the exact name of the new region in quotes. When an element allows a player to now travel to a new region, this value should be set. Make sure every region has elements allowing a player to travel to other planned regions in the order intended for your adventure. A region that does not have this tag set for it in some other region cannot be visited.  
  - **resolutionPossible**: An element with this set is something that opens up the end of the adventure. Whether a keyedScene or location or holy grail, if it is basically the end of the story, set this element to true. The resolution text will then be displayed giving details on how to wrap up the adventure in whatever way works best for your adventure.

  KeyedScene properties: These have two special properties in addition to the above to control when they fire. You may set both values but the event will fire only once, with whichever happens first.

  - **triggerPercent**: After reaching the minScene value, the trigger will have this percentage of likelihood to fire.  
  - **triggerNumber**: When the currentScene reaches this value, this will always fire. Useful if you want to have strong control over an event happening.
 
  # OK So how do I convert my favorite prewritten adventure into a module for this system

  I have full instructions you can find in the "Making an Adventure" folder. Some minor editing of the prompts and some cut and paste and you can have AI turn any text based advenuture module into correct JSON for this program.

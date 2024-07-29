# The-Adventure-Oracle

This is a pretty simple python script really. You can find instructions to install python at https://www.python.org/.

The download a copy of this repository to a folder on your hard drive.

Open a command line and go to the folder where you saved the files from this repository.

Run:
> python adventure_oracle.py

That should be it.

It will open a menu on your screen and output both to your screen and also to a file in the logs directory. This file is in markdown and should read fine in Obsidian or other markdown readers. There is a sample output there if you want to have a look. Feel free to delete it if you are starting over.

It has two two starting adventures currently. I will be adding more as time permits but you can easily make your own.

One is a space opera fit for a crew of explorers from a 1960s TV show.

The other is a horror murder mystery "Tockley Manor" by Tana Pigeon of https://WordMillGames.com published in Mythic Magazine Volume 11. Used with permission.

# So What does it do?

I would encourage you to start with buying Mythic Magazine vol 11 from DriveThroughRPG and reading Tana's excellent article where she explains this system in depth. The goal is to play written modules solo. What she produces there might be more described as writing modules for solo play as an existing module will need a bit of work to convert it to this system but the end result is pretty nifty. It combines her excellent Mythic GM Emulator with her Location Crafter and uses a series of tables to capture some of the creative feel of solo RPG but also the planned structure of a written module. 

I will write a longer introduction when I have time but Tana's example is excellent and it was what I started with coding this. It immediately struck me that most of the hard work involved could be automated by converting all the charts to JSON and using some simple python logic to simulate the draws. There is some fun stuff she adds to it to increase the probably of drawing from the early parts of tables in the early game and working your way down as things progress. I did some interesting things to capture this mechanic in a slightly different way but it works out the same. Some of the statistical odds changed a bit and I will likely still tweak them further to get the feel I want.

Basically you begin with a detailed opening scene, possibily including some NPCs you may already be introduced to and some threads that are already established as this is common for written modules. Tana ties her example closely to Mythic's mechanics but it should not be hard to swap it out for many popular oracles. 

So when you launch the program it gives you a list of files in the adventures directory. One file per written module. select theone you want to play. It then outputs the opening scene and initial thread and character list. Capture these lists with your oracle and continue to build and use thread and character lists as you normally would. This information isn't repeated by the program and might or might not reference these elements directly. Your oracle should bring them back into focus with your play through the regular machanics of random events it provides. 

Your adventure is divided into regions which contain areas. A region may be a town. The areas would then be shops, parks, houses etc. that you might visit while in this region.

Each area has three elements that define it:
- location
- encounter
- object

As you move to a new area in the region the program will give you information on these three elements. use that to create your scene. Use your RPG rules and Oracle to play out the scene as appropriate. Feel free to journal what you are doing in the same markdown file the program outputs to. It should work fine. When it is time to move to a new area consult the program again. It will give you three new elements. You may always revisit areas you have been to. There is no need to use the program when doing so. Use your Oracle and RPG rules to determine is anything changed or is a wandering monster showed up or whatever. You must fill in the logical gaps of traveling between areas, but usually they should make sense being close to each other.

At some point you will discover a new region. A haunted mansion to explore or a cave to delve. Once this happens you will have a new menu option to travel to a new region. Use your RPG rules to handle travel if that is important. As before you may travel back to a known region/area. The program saves its state of each region so if you leave a region and then return to explore more, it picks up where it left off. You can also close and reopen the program and resume where you were.  

Additionally another mechanic Tana uses is Keyed Scenes. These are scenes that really must happen to advance the story (basically railroading). These keyed scenes are tied to a region and will only occur there. Tana used some fun mechanics that I have approvimated in the program to control when these fire. When a keyed scene fires, try to work it into the current context. If it doesn't fit well, then I guess you now have two scenes to roleplay. 

You don't have to explore a region longer than you want to assuming you have discovered somewhere else to go. Eventually you will have explored all that was prepared and the creativity of the system will run out of juice and the elements will simply say "Complete". Probably time to move on to another region if this happens or keep it going under your own creativity. 

Eventually, you will hit the end of the adventure. You will have solved the mystery, found the big bad, wooed the princess, or whatever. When this happens the resolution will be printed out. Now this could be a very definitive resolution that wraps it all up for you, but Tana presented an interesting menu of options and a mechanic to determine how it all sorts out. I like that because it leaves a lot of flexibility to the player.

I think that is enough to get you started.

# So how do I write a module

I need to write this up. Take a look at the adventure-frame.json file in any text editor and you will see the format you need to put it in. Have a look at the adventures directory to see at least two adventures already filled out. Hopefully the file itself is straightforward, but I will be writing a more detailed explanation a bit later. Check back. I will be playing with this a fair bit, but it is usable now so I wanted to share it.

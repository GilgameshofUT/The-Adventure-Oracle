We are going to write an adventure together for a program that reads a JSON script to act as a gamemaster or oracle for a ttrpg game. We will take this creation in steps.

First carefully read through the documentation below wrapped in <documentation> tags. This will explain how the program works and how each element of the JSON file is used. 

Next read through the examples that follow wrapped in the <example> tags. These examples are for two very different adventures. One is a murder mystery horror adventure set in a town and a mansion. The other is an adventure set in Star Trek The Original Series where they explore a planet. 

We are going to convert an adventure from a FATE Core adventure module about John Carter of Mars to this system. You will find the story to convert wrapped in the <story> tags. Our goal is not to shorten or summarize but to convert it to this different format. You should freely quote from the original text when it makes sense to do so.

First adapt a satisfying plot line from <story> that has the feel of one of the John Carter books. 

Then produce the root elements firstScene, threads, and characters in correct JSON format.  Be sure to include all information that a game master would be expected to give to players at the beginning of the adventure. Sometimes this may involve quoting blocks of flavor text in the description fields. There is not a need to shorten or summarize information that would normally be given to players at the start of the game.

Then produce a plan for the regions appropriate to the adventure, including which regions should open up travel to which other regions. You should break the regions plan into smaller regions. Consider what elements of the story go with each other and would likely be explored together when forming a region. If logical with the storyline a single region can lead to multiple other regions.

We will produce the actual regions elements and the resolution element in a future step.

<story>
## A Princess of Mars: Upon the Red Planet - A FATE Core Adventure Module

**Welcome to Barsoom, adventurer!** You are John Carter, thrust into a world of dying civilizations, savage green warriors, and wonders beyond imagining. This adventure module, based on Edgar Rice Burroughs’s classic tale, encompasses the first act of your Martian saga. Prepare for a thrilling ride! 

**Character Creation:**

You are John Carter, a former soldier, adaptable, resourceful, and a stranger in a strange land. Define your character:

* **High Concept:** Experienced Soldier Thrust into a Martian Mystery 
* **Trouble:** Haunted by Earthly Memories (choose a specific event)
* **Aspects:** Examples:  Resourceful Survivor, Honorable to a Fault,  Adaptable to Strange Circumstances, Skilled with Blade and Gun, Seeking Purpose in a New World.  
* **Skills:** Choose skills reflecting your background: Physique, Fight, Shoot (military), Notice, Stealth (survival), Will, Empathy, Provoke (adaptability).
* **Stunts:** Enhance combat prowess, survival instincts, or ability to understand alien languages and cultures.

**Starting Gear:**  
* Confederate Army Revolver (Weapon: +2 when facing multiple opponents, Limited Ammo) 
* Sturdy Hunting Knife (Weapon: +2 when used strategically) 
* Dilapidated Journal and Pen  (+2 to overcome Create Advantage actions based on knowledge gathering)
* Worn Compass (Advantage when navigating unfamiliar terrain)

**Part 1: Under the Two Moons of Barsoom**

**Scene 1: Awakening on a Dying World**

You awake, disoriented, in a vast, desolate plain beneath two moons. Survival is your first challenge. 

**Map Points:**

**1. The Ancient Crater (Starting Location):** 
   - **Aspects:** Desolate and Silent,  Whisper of Ancient Winds, Echoes of a Forgotten Past
   - **Description:** A vast crater with remnants of past Martian life scattered throughout.
   - **Potential Encounters/Discoveries:**  
      - Crumbling ruins with a decipherable mural hinting at lost technology and planetary history. 
      - A small oasis offering temporary water, but also potentially attracting local fauna.
      - Tracks of a large, predatory thoat – a dangerous Martian creature that could pose an immediate threat. 

**2. The Whispering Forest:**
   - **Aspects:**  Strange and Unsettling, Shifting Shadows, Thorny Embrace
   - **Description:** Spindly, sharp-thorned plants create an unsettling maze.
   - **Potential Encounters/Discoveries:**  
      - Rodent-like creatures, a source of food if desperation calls for it.
      - An underground tunnel network, potentially offering shelter or leading to other points of interest.
      - A strange, shimmering fruit, its properties unknown –  a potential source of nourishment or a deadly poison?

**3. The Cairn of Skulls:**
   - **Aspects:**  Ominous and Foreboding,  Stench of Decay, Whispers of Past Sacrifices
   - **Description:**  A towering cairn made entirely of skulls – humanoid and otherwise – creating a macabre landmark.
   - **Potential Encounters/Discoveries:**  
       - Signs of a recent struggle suggesting something powerful hunts in this area.
       - A hidden compartment within the cairn containing a strange artifact or a message from the past. 

**4. The Red Dust Dunes:**
   - **Aspects:**  Vast and Unforgiving,  Shifting Sands,  Hidden Dangers Beneath
   - **Description:**  Unforgiving dunes where navigation and the elements are the enemy.
   - **Potential Encounters/Discoveries:**  
      - A sudden sandstorm that could disorient you or bury you alive.
      - Bioluminescent insects that attract larger predators after dusk, a tempting source of light but a dangerous beacon.
      - A shimmering mirage, potentially a hallucination or a sign of a true oasis in the distance.

**5. The Thoat Watering Hole:**  
    - **Aspects:**  Scarce Resource, Territorial Disputes, Signs of Passage  
    - **Description:**  A muddy depression where thoats gather to drink, offering a chance to observe these creatures, track them, or even witness a territorial clash. 

**6. The Ancient Observatory:**
    - **Aspects:**  Silent Sentinel,  A Window to the Stars,  Whispers of Lost Knowledge  
    - **Description:**  A ruined structure with remnants of astronomical instruments. It could hold clues to Martian navigation, secrets of the Ninth Ray, or a vantage point to observe the surroundings.

**7. The Crystal Cave:**
    - **Aspects:**  Blinding Light,  Disorienting Beauty,  Whispers of Energy 
    - **Description:** A cavern filled with glowing crystals that refract the light of the two moons, potentially disorienting and attracting wildlife. 

**8.  The Meteorite Scar:**
    - **Aspects:**  Otherworldly Materials,  Residual Heat,  Signs of Impact
    - **Description:**  The site where a meteorite crashed into Barsoom, potentially offering strange materials, evidence of ecological impact, or even remnants of what it carried.

**Challenges:**

* **Overcome:**  The Effects of Low Gravity (Athletics):  Move with coordination, or risk stumbling and taking stress.
* **Create an Advantage:**  Finding Shelter from the Harsh Sun (Notice): Locate shade to recover from the initial stress of your arrival. 

**Scene 2: First Contact with the Tharks**

You encounter the Tharks, a fearsome race of green-skinned warriors. Your actions in this first encounter will determine your fate.

**Potential First Contact Locations:**

**1. The Oasis Ambush (Following tracks from the Crater):** 
    - **Aspects:**  Desperate Need,  Hidden Predators, First Strike Advantage
    - **Description:**  The Tharks lie in wait at the oasis, a test of survival from the moment you arrive. 
    - **Challenges:** 
        - **Overcome:** Thark Surprise Attack: Survive the initial ambush, using the environment to your advantage. 
        - **Create an Advantage:**  Even the Odds:  Use the spring, vegetation, and terrain to create distance or cover. 

**2. The Cairn Confrontation:** 
    - **Aspects:**  Sacred Ground,  Show of Strength, Opportunity for Communication
    - **Description:**  You encounter a lone Thark guard, a test of diplomacy in the face of a powerful warrior.
    - **Challenges:**
        - **Overcome:**  Language Barrier (Empathy/Lore):  Use gestures and observation to convey peaceful intentions. 
        - **Create an Advantage:** Demonstrate Respect:  Show reverence for the Cairn to gain a measure of trust.

**3. The Dust Dune Chase:**
    - **Aspects:**  Vast and Exposed,  Test of Endurance, Flight or Fight?
    - **Description:**   A Thark patrol on thoats (six-legged steeds) spots you, leading to a chase across the dunes.
    - **Challenges:**  
        - **Overcome:**  Outrun the Thoats (Athletics):  A test of stamina with consequences for failure.
        - **Create an Advantage:**  Find Cover: Use the dunes and potential sandstorms as cover. 

**4. The Valley of the Moonstones (If First Contact is Delayed):**
    - **Aspects:**  Eerie Beauty,  Strange Energies,  Hidden Dangers
    - **Description:**  A valley filled with phosphorescent stones.  Beautiful but potentially dangerous, attracting predators or invoking Thark superstition. 

**5.  The Ancient Battlefield (If First Contact is Delayed):**
    - **Aspects:**  Echoes of War,  Shattered Weapons,  A Warning Unheeded 
    - **Description:**  A barren land littered with the remnants of past Martian wars.  Discover clues, scavenge for weapons, but risk discovery yourself.

**6. The Shifting Sands:**
    - **Aspects:**  Treacherous Terrain,  Hidden Sinkholes,  A Test of Cunning
    - **Description:**  A region of ever-changing sand dunes that challenges even the most skilled navigators.

**NPCs Introduced:**

**Tars Tarkas (Ambitious Thark Warrior)**
* **High Concept:**  Ambitious and Ruthless Thark Warrior
* **Aspects:**  Unmatched Strength,  Craves Power,  Pragmatic and Observant,  Hides a Sense of Honor 
* **Skills:**  Great (+4) Fight, Good (+3) Athletics, Fair (+2) Provoke,  Average (+1)  Physique, Will.

**Sola (Compassionate Thark Woman)**
* **High Concept:**  Kind-Hearted Thark Outcast
* **Aspects:**  Compassionate Despite Her Upbringing,  Skilled Hunter,  Yearns for a Different Life 
* **Skills:**  Good (+3) Notice, Stealth, Fair (+2)  Empathy, Average (+1) Fight, Physique. 

**Challenges Regardless of Location:**

* **Overcome:**  Thark Prejudice (Empathy/Provoke):  Overcome their distrust and demonstrate that you are not a threat.
* **Choice:**   Do you fight, flee, or attempt to reason? This first impression will resonate throughout your adventures.

**Scene 3:  Life Among the Tharks**

You are a captive within the Thark horde,  forced to adapt or perish.

**Map Points (Moving Locations):**

**1. The Thark Marching Column:**
    - **Aspects:**  Relentless Pace,  Strict Hierarchy, Strength in Numbers 
    - **Challenges:**
        - **Overcome:**  The Rigors of the March (Athletics/Physique):  Keep pace, endure the elements, and avoid exhaustion. 
        - **Create an Advantage:**  Learn Thark Customs (Empathy/Lore):  Observe and adapt to their hierarchy and rituals. 

**2.  A Night Camp Under the Moons:**
    - **Aspects:**  Circle of Fires, Whispers in the Dark,  Momentary Respite 
    - **Challenges:**  
        - **Overcome:**  Prove Your Worth:  Engage in contests (physical or mental) to earn respect. 
        - **Create an Advantage:**  Forge Alliances:  Identify potential allies dissatisfied with Thark leadership (perhaps with Sola's guidance). 

**3. A Raid on a Red Martian Outpost:**
    - **Aspects:**  Chaos and Violence, Cultural Clash,  Chance for Escape?
    - **Challenges:** 
        - **Overcome:**  Survive the Chaos:  Stay alive during the raid, using chaos to your advantage. 
        - **Create an Advantage:**  Exploit the Confusion:  Free prisoners, steal supplies, or attempt escape. 

**4. The Ruins of Horz:**
    - **Aspects:**  City of Ghosts,  The Weight of History,  Whispers of a Curse
    - **Description:**   A ruined city, said to be cursed, offering a glimpse into Thark lore, potential treasure, and dangers fueled by superstition.

**5.  A Thark Hunting Ground:**
    - **Aspects:**  Test of Skill,  Predator and Prey,  The Law of the Wild
    - **Description:**   Prove your worth by participating in a Thark hunt, testing your survival skills and challenging your moral compass.

**6.  A Gathering of Hordes:**
    - **Aspects:**  Rivalries and Alliances,  A Sea of Green,  Opportunity and Danger in Equal Measure 
    - **Description:**   Your horde encounters another. Tensions run high, offering chances to observe dynamics, forge alliances, or get caught in power struggles.

**7.  The Ruins of a Dead City (Alternative):** 
    - **Aspects:**  The Price of Arrogance,  Silent Warnings,  Whispers of Forbidden Technology 
    - **Description:**   The Tharks camp in a destroyed Red Martian city.  Discover clues to their downfall, perhaps finding still-functional technology. 

**8. A Thark Coming-of-Age Ritual:** 
    - **Aspects:**  Brutal Tradition,  Tests of Endurance,  A Chance to Impress or Disgust 
    - **Description:** Witness or participate in a brutal ritual.  Earn respect with unexpected mercy, your knowledge, or challenge Thark traditions. 

**Ongoing Challenges:**

* **The Language Barrier:**  Continuously make Empathy or Lore checks to progress in understanding Thark language.
* **Sola’s Guidance:** Maintain a good relationship with Sola to gain insight and aid (or face the consequences of her fear).
* **Tars Tarkas’s Scrutiny:**  Impress him (or become a pawn in his games) by showcasing your unique skills.

**Additional Element:**

* **Test of Mettle:**  John Carter is tasked with using his Earth knowledge to solve a problem for the Tharks - fixing a weapon, navigating, providing medical aid, etc., further proving his worth beyond mere fighting. 

**Scene 4:  The Princess of Helium**

Amidst the raid, you see her - Dejah Thoris, Princess of Helium, a captive who sparks a new purpose within you.

**Map Points:**

**1. The Outskirts of the Red Martian City:**
    - **Aspects:**  A Glimmer of Civilization,  Tense Standoff,  Vulnerability of Beauty 
    - **Challenges:** 
       - **Choice:**  Participate in the raid, stand apart, or warn the Red Martians?
       - **Create an Advantage:**  Observe and Learn (Lore/Notice):  Study Red Martian defenses, tactics, and technology.

**2. The Captured Palace:** 
    - **Aspects:**  Splendor and Imprisonment,  Whispers of Rebellion,  A Captive Audience 
    - **Challenges:**
        - **Overcome:**  The Language Barrier (Empathy/Linguistics):  Find a way to communicate with Dejah Thoris.
        - **Create an Advantage:**  Earn a Moment Alone: Use the chaos to engineer a private conversation with the princess. 

**3. The Slave Caravan:**
    - **Aspects:**  A Long Journey Ahead,  Hidden in Plain Sight,  Whispers of Discontent 
    - **Challenges:**
       - **Overcome:**  Thark Security (Stealth/Deceive): Get close to Dejah Thoris without raising suspicion.
       - **Create an Advantage:**  Sow Seeds of Doubt:  Subtly exploit Thark tensions to aid in a potential escape. 

**4. The Gardens of the Palace:**
    - **Aspects:**  Serene Beauty,  A Moment of Tranquility,  Hidden in Plain Sight
    - **Description:**  A peaceful garden within the besieged palace, offering a chance for a first encounter with Dejah Thoris, but also potential dangers.

**5.  The Hall of Ancestors:**
    - **Aspects:**  Honoring the Past,  Whispers of Lineage,  Clues to a Legacy 
    - **Description:**   A hall dedicated to the ancestors of the Red Martian residents, potentially revealing clues about Dejah Thoris's lineage or hidden passages.  

**NPC Introduced:**

**Dejah Thoris (Courageous and Intelligent Princess)**
* **High Concept:**  Princess Fighting for Her People's Freedom
* **Aspects:**  Sharp Intellect,  Unwavering Courage,  Skilled Diplomat, Master of Martian Lore
* **Skills:**  Great (+4)  Empathy, Lore, Good (+3)  Contacts, Will,  Fair (+2)  Deceive

**Challenges Throughout:**

* **Sola’s Warning:** Heed or ignore Sola’s advice against getting involved, impacting your relationship with her. 
* **Tars Tarkas’s Ambition:**  Navigate his interest in Dejah Thoris and decide if you can use it to your advantage.

**Additional Element:**

* **Dejah Thoris’s Cunning:**  Showcase her resourcefulness – she attempts to communicate in code, uses Thark customs against them, or has a hidden tool, actively seeking a way out of her predicament. 

**Scene 5:  The Arena at Warhoon**

You arrive at Warhoon, the Thark city, and face a brutal test of survival in the arena. 

**Map Points:**

**1. The Gates of Warhoon:**
    - **Aspects:**  Imposing and Ancient, Throngs of Green Warriors,  Whispers of Past Glories and Terrors
    - **Challenges:**
        - **Overcome:**  Thark Social Dynamics (Empathy/Lore):  Avoid causing offense or instigating a challenge.  
        - **Create an Advantage:**  Gather Intelligence (Notice/Contacts/Resources):  Learn about the arena, potential allies, and Dejah Thoris's whereabouts.  

**2. The Warhoon Arena:**
    - **Aspects:**  A Theatre of Cruelty, Sand Stained Red, The Roar of the Crowd 
    - **Challenge:**
        - **Combat:** The White Ape (Major Encounter): Utilize your skills and the environment to defeat the creature. 

**3. The Holding Pens:**
    - **Aspects:**  Confined and Anxious,  A Symphony of Scents and Sounds,  Desperate Hope 
    - **Challenges:**
        - **Overcome:**  Maintain Morale (Empathy/Rapport):  Keep your spirits high amidst fear and despair.
        - **Create an Advantage:**  Seek an Unlikely Ally:  Find someone with useful knowledge, a weapon, or influence.  

**4. The Jeddak's Viewing Platform:**
    - **Aspects:**  A Display of Power,  The Crowd Below,  A Desperate Gambit 
    - **Description:**  Tal Hajus's private box, offering a risky chance to plead for your life, attempt escape, or subtly influence the Jeddak.

**5. The Arena’s Underbelly:**
    - **Aspects:**  The Stench of Fear,  Confined Beasts,  A Desperate Alliance?  
    - **Description:**  The holding pens beneath the arena, where you might encounter a future ally, a beast to overcome, or a means to escape. 

**6.  The Hall of Trophies:**
    - **Aspects:**  Victories Past,  Whispers of Legends,  A Test of Character
    - **Description:**  A hall dedicated to past arena champions. Glean information from Tharks, discover resonant objects, or make a choice that influences their perception of you. 

**7. The Gladiator’s Pit of Despair:**
    - **Aspects:**  No Hope, No Escape,  The Smell of Death
    - **Description:**  A forgotten pit below the arena where the condemned await their fate.  John Carter must use his wits and the environment to escape.

**Challenges Beyond the Arena:**

* **Dejah Thoris’s Presence:**  Seeing her captive strengthens your resolve, but how will you reach her? 
* **The Eyes of Tars Tarkas:**  Interpret his scrutiny. Does he see a potential tool or a threat?

**Additional Elements:**

* **Gladiatorial Variety:**  Before the white ape, face a smaller arena challenge showcasing other combat skills.  
* **Thark Ritual (Expansion):**  You witness or are forced to partake in a ritual that deepens your understanding of Thark culture and potentially impacts your standing within the horde. 

**Scene 6:  Seeds of Rebellion**

You navigate the political landscape of Warhoon as discontent festers and Tars Tarkas makes his move. 

**Map Points:**

**1. The Victor’s Feast:** 
    - **Aspects:**  Heady Victory,  Intoxicating Power,  Hidden Agendas 
    - **Challenges:**
        - **Overcome:**  Thark Etiquette (Empathy/Rapport/Deceive):  Avoid missteps that could lead to conflict.
        - **Create an Advantage:**  Identify Potential Allies (Notice/Empathy/Provoke):  Find those who oppose Tal Hajus.

**2.  Sola’s Quarters:** 
    - **Aspects:**  Conflicted Loyalties,  Whispers of Truth,  A Moment of Respite 
    - **Challenges:**
       - **Overcome:** Sola’s Fear (Empathy/Rapport):  Convince her that taking action is necessary.
       - **Create an Advantage:**  Interpret the Rumors (Lore/Contacts): Decipher the truth about plots against Tal Hajus. 

**3.  The Jeddak’s War Council:** 
    - **Aspects:**  Clashing Ambitions,  The Weight of Tradition,  A Calculated Risk 
    - **Challenges:**
        - **Overcome:** Gaining Audience (Empathy/Rapport/Provoke):  Earn a moment to speak without raising ire.  
        - **Create an Advantage:**  Sow Discord:  Subtly manipulate existing tensions to weaken Tal Hajus’s hold.

**4. The Grove of Issus:**
    - **Aspects:**  Sacred and Forbidden,  Ancient Trees,  A Place of Whispered Plots 
    - **Description:**  A hidden grove where dissident Tharks meet, offering access to secret deals, vital information, and potentially requiring displays of loyalty. 

**5. The Armory of Warhoon:**
    - **Aspects:**  Weapons of War,  Heavily Guarded,  Temptation and Risk 
    - **Description:**  A tempting but dangerous target.  Breaching the armory could provide weapons for the rebellion or aid your escape, but failure is not an option.

**6. The Den of Ill Repute:**
    - **Aspects:**  Hidden Agendas,  Whispers and Deals,  A Place of Dangerous Secrets 
    - **Description:**  Warhoon's underbelly – a gambling den, black market, or clandestine meeting place.  Gather information, uncover plots, or use your skills for high-stakes deception. 

**Challenges Throughout:**

* **Tars Tarkas’s Game (Deceive vs. Deceit or Will):** Discern his true motives and whether he's an ally or a threat. 
* **Dejah Thoris’s Unseen Influence:** Rumors of her wisdom might aid your cause, even in her captivity. 

**Additional Elements:**

* **Thark Prophecy (Expansion):**  Your arrival coincides with a Thark prophecy, making you a potential figurehead. 
* **Sola's Secret:**  She reveals a hidden agenda or information that complicates your relationship and the rebellion. 

**Scene 7: Escape From Warhoon**

With the city on the brink of civil war, you make a desperate bid for freedom.

**Map Points:**

**1.  The Undercity:**
    - **Aspects:**  Dark and Labyrinthine,  Whispers in the Shadows,  Forgotten Passages
    - **Challenges:** 
        - **Overcome:**  Navigating the Darkness (Lore/Notice/Survival):  Don’t get lost in the maze. 
        - **Create an Advantage:**  Exploit the Undercity’s Secrets (Lore/Investigate):  Find hidden resources or escape routes.

**2. The Jeddak's Palace:**
    - **Aspects:**  Heavily Guarded,  A Place of Power and Vulnerability,  Every Wall Has Ears  
    - **Challenges:**
       - **Overcome:**  Breaching Thark Security (Stealth/Deceive): Get past the palace guards.
       - **Create an Advantage:**  Turn the Palace Against Itself (Forgery/Deceive/Provoke):  Use existing tensions to create chaos and cover your escape.  

**3.  The Thoat Pens:**
    - **Aspects:**  Beasts of Burden,  A Chance for a Wild Ride,  Beyond the City Walls
    - **Challenges:** 
        - **Overcome:** Taming the Thoats (Physique/Animal Handling): Secure mounts without causing more trouble.
        - **Create an Advantage:**  Create a Diversion (Resources/Burglary/Larceny/Provoke):  Distract the Tharks to cover your escape. 

**4. The Ancient Aqueduct:**
    - **Aspects:**  Forgotten Passage,  Treacherous Footing,  A Race Against Time  
    - **Description:**  A crumbling aqueduct, offering a hidden but dangerous escape route requiring skillful navigation.

**5.  The Sky-Ship Docking Port:**
    - **Aspects:**  Technological Marvel,  Heavily Guarded,  A Desperate Gamble
    - **Description:**   Warhoon’s seldom-used dock for flying ships. Escape on one would be daring, requiring cunning, technical skill, and a plan for avoiding pursuit. 

**6.  The Ancient Catacombs:**
    - **Aspects:**  Forgotten Tombs,  Whispered Legends of Guardians,  A Desperate Shortcut
    - **Description:**  Ancient catacombs beneath the city, rumored to be haunted and potentially guarded.  A swift but perilous escape route. 

**Challenges Throughout:**

* **Tars Tarkas’s Ultimatum:**  Join his rebellion and claim Dejah Thoris or face his wrath. What do you choose?
* **Sola’s Choice:** Will she help, hinder, or remain neutral in your escape? 

**Additional Elements:**

* **Chase Complications:**  Introduce unexpected obstacles – sandstorms, rival Thark factions, or hidden traps. 
* **Dejah Thoris as Co-Conspirator:**  She plays an active role, providing information or creating distractions.

**Conclusion of Part 1:**

Your escape from Warhoon marks the end of the beginning. You have survived the trials of a dying world, faced down savage warriors, and touched the heart of a princess.  But your adventures are far from over.  The fate of Dejah Thoris, and perhaps all of Barsoom, hangs in the balance.   Prepare for the challenges that await in Part 2:  The Princess of Helium!

**Rewards:**

* **Advancement:**  Award players with 3-4 Fate points for completing Part 1 to purchase new skills, increase attributes, or acquire new stunts.
* **New Aspects:** Players may choose to add new Aspects reflecting their experiences.
* **Connections:**  The relationships with Sola and Tars Tarkas will have lasting impacts, for good or ill. 

**GM Note:**

This is just the framework for a grand adventure! Use these elements as building blocks, incorporating your own creativity, player choices, and twists to bring the vibrant world of Barsoom to life! 


</story>

<documentation>
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



</documentation>

<example>
{
    "firstScene": {
      "description": "The first Scene should involve your Character arriving in the isolated New England town of Closport. A sleepy village with fewer than 5,000 people, Closport was once a thriving wine making community. That was many years ago, however. These days the place is slowly withering. A murder has taken place and you are here to help."
    },
    "threads": [
      {
        "id": 1,
        "name": "Get to the bottom of the murder"
      }
    ],
    "characters": [
      {
        "id": 1,
        "name": "Francis Herrera",
        "description": "Closport Chief of Police"
      },
      {
        "id": 2,
        "name": "Ann Sharpe",
        "description": "Proprietor of The Steamport Inn"
      },
      {
        "id": 3,
        "name": "Zane Hoxel",
        "description": "Owner of Hoxel's Farm"
      },
      {
        "id": 4,
        "name": "Closport Citizen",
        "description": "Generic citizen of Closport"
      }
    ],
    "regions": [
      {
        "id": 1,
        "name": "Closport",
        "isStartingRegion": true,
        "description": "A sleepy village with fewer than 5,000 people, Closport was once a thriving wine making community. That was many years ago, however. These days the place is slowly withering.",
        "locations": [
          {
            "id": 1,
            "name": "Expected",
            "description": "An Element listing under a Category can simply say 'Expected'. This Category Element represents the mundane in your Region. As your Character enters a Region and explores, you will have expectations of what you will find: dark hallways in a dungeon, tangles of vines in a forest, enemy henchman patrolling a villain's lair. A Category result of 'Expected' produces just that, what you most expect for that Category.",
            "minScene": null
          },
          {
            "id": 2,
            "name": "Public Space",
            "description": "This can be any expected, outdoor public space in town such as a sidewalk, an alley between buildings, a stone bench, an overlook of the ocean, etc.",
            "minScene": null
          },
          {
            "id": 3,
            "name": "Active Shop",
            "description": "This is a working store in Closport. Most of the shops that are active sell items useful to local citizens, such as food and goods, clothing, and fishing and hunting equipment. There may also be some curio type shops, such as antiques, as well as a couple of small restaurants.",
            "minScene": null
          },
          {
            "id": 4,
            "name": "Town Square",
            "description": "This is the center of Closport, a circular area ringed by public buildings. There is a small park in the middle of the town square, a grassy spot with a few trees and benches.",
            "minScene": null
          },
          {
            "id": 5,
            "name": "Steamport Inn",
            "description": "This is the only hotel in Closport, an old two-story house that's been renovated into an inn by its owner Ann Sharpe. The Fate Question Odds of her being easily found at the front desk during the day or early evening is Very Likely.",
            "minScene": null
          },
          {
            "id": 6,
            "name": "Police station",
            "description": "The Closport Police Station is a small storefront with a single office inside. Closport's police chief, Francis Herrera, is also the town's only police officer. The Fate Question Odds of him being in the station during normal working hours is Very Likely.",
            "minScene": null
          },
          {
            "id": 7,
            "name": "Public Space",
            "description": "This can be any expected, outdoor public space in town such as a sidewalk, an alley between buildings, a stone bench, an overlook of the ocean, etc.",
            "minScene": 2
          },
          {
            "id": 8,
            "name": "Expected",
            "description": "An Element listing under a Category can simply say 'Expected.' This Category Element represents the mundane in your Region. As your Character enters a Region and explores, you will have expectations of what you will find: dark hallways in a dungeon, tangles of vines in a forest, enemy henchman patrolling a villain's lair. A Category result of 'Expected' produces just that, what you most expect for that Category.",
            "minScene": 2
          },
          {
            "id": 9,
            "name": "Empty Storefront",
            "description": "An abandoned and boarded up shop, most likely near the center of town.",
            "minScene": 2
          },
          {
            "id": 10,
            "name": "Docks",
            "description": "Closport is a seaside community. Although the town's primary commerce has historically been wine making, there is some small fishing business as well. The docks are poorly maintained and reflect the town's overall poverty.",
            "minScene": 2
          },
          {
            "id": 11,
            "name": "Expected",
            "description": "An Element listing under a Category can simply say 'Expected.' This Category Element represents the mundane in your Region. As your Character enters a Region and explores, you will have expectations of what you will find: dark hallways in a dungeon, tangles of vines in a forest, enemy henchman patrolling a villain's lair. A Category result of 'Expected' produces just that, what you most expect for that Category.",
            "minScene": 2
          },
          {
            "id": 12,
            "name": "Radford Regional Park",
            "description": "This is a part of the forest bordering Closport that is maintained by the federal government. It's a wild area of thick trees and occasional streams. This is an ideal outdoor area for your Character to have an encounter or discovery.",
            "minScene": 3
          },
          {
            "id": 13,
            "name": "Special",
            "description": "As the name says, something amazing or unusual. Consult your Oracle for details. Maybe it's twice as large, or unusual for this setting.",
            "minScene": 3
          },
          {
            "id": 14,
            "name": "Hoxel's Farm",
            "description": "Hoxel Farm is a vineyard on the periphery of Closport. The property is sprawling and aged, with dying vines and a barn that is leaning to one side in its decrepitude.",
            "minScene": 4
          },
          {
            "id": 15,
            "name": "Expected",
            "description": "An Element listing under a Category can simply say 'Expected.' This Category Element represents the mundane in your Region. As your Character enters a Region and explores, you will have expectations of what you will find: dark hallways in a dungeon, tangles of vines in a forest, enemy henchman patrolling a villain's lair. A Category result of 'Expected' produces just that, what you most expect for that Category.",
            "minScene": 4
          },
          {
            "id": 16,
            "name": "Random",
            "description": "A bit more interesting than 'expected' but not something so memorable or supernatural as 'wierd'. Consult your oracle.",
            "minScene": 5
          },
          {
            "id": 17,
            "name": "House Of The Wind",
            "description": "The House of the Wind is a very old church in Closport. It is a little outside of town and unlikely to find unless someone is really looking. The place is a simple single story structure with a steepled roof. It's abandoned, although there may still be signs of some use. The House of the Wind is another opportunity for a site for something unusual to happen.",
            "minScene": 5
          },
          {
            "id": 18,
            "name": "Expected",
            "description": "An Element listing under a Category can simply say 'Expected.' This Category Element represents the mundane in your Region. As your Character enters a Region and explores, you will have expectations of what you will find: dark hallways in a dungeon, tangles of vines in a forest, enemy henchman patrolling a villain's lair. A Category result of 'Expected' produces just that, what you most expect for that Category.",
            "minScene": 6
          }
        ],
        "encounters": [
          {
            "id": 1,
            "name": "None",
            "description": null,
            "minScene": null,
            "newRegion": null
          },
          {
            "id": 2,
            "name": "None",
            "description": null,
            "minScene": null,
            "newRegion": null
          },
          {
            "id": 3,
            "name": "Expected",
            "description": "An Element listing under a Category can simply say 'Expected.' This Category Element represents the mundane in your Region. As your Character enters a Region and explores, you will have expectations of what you will find: dark hallways in a dungeon, tangles of vines in a forest, enemy henchman patrolling a villain's lair. A Category result of 'Expected' produces just that, what you most expect for that Category.",
            "minScene": null,
            "newRegion": null
          },
          {
            "id": 4,
            "name": "None",
            "description": null,
            "minScene": null,
            "newRegion": null
          },
          {
            "id": 5,
            "name": "Closport Citizen",
            "description": null,
            "minScene": null,
            "newRegion": null
          },
          {
            "id": 6,
            "name": "Expected",
            "description": "An Element listing under a Category can simply say 'Expected.' This Category Element represents the mundane in your Region. As your Character enters a Region and explores, you will have expectations of what you will find: dark hallways in a dungeon, tangles of vines in a forest, enemy henchman patrolling a villain's lair. A Category result of 'Expected' produces just that, what you most expect for that Category.",
            "minScene": null,
            "newRegion": null
          },
          {
            "id": 7,
            "name": "None",
            "description": null,
            "minScene": 2,
            "newRegion": null
          },
          {
            "id": 8,
            "name": "Francis Herrera",
            "description": null,
            "minScene": 2,
            "newRegion": null
          },
          {
            "id": 9,
            "name": "Closport Citizen",
            "description": null,
            "minScene": 2,
            "newRegion": null
          },
          {
            "id": 10,
            "name": "Learn About Tockley",
            "description": "This is a special Encounter where Tockley Manor is introduced to your Character. If you have already learned about Tockley through a Keyed Scene, then your Character gets more information about the Manor in this Encounter. You'll need to determine two things: how you learn about Tockley, and what information is attached to it. The how can be answered through a Fate Question using what seems most logical given the Context. For instance, if your Character is in a shop in Closport and you roll this Encounter, you may determine that the owner of the store tells you about it. \"The woman behind the counter sets down the music box and leans forward, saying in a conspiratorial voice, 'Have you heard of Tockley Manor?'\"  Aside from Characters, you may also learn of the Manor through books or journals. After you determine how you learn about the Manor, you need to attach what you learn about it. This should contain some element of mystery or local legend to it. For inspiration, roll on the Action Meaning Tables. For instance, in our example above of the shopkeeper mentioning Tockley, the Player rolls on the Action Meaning Tables and gets \"waste\" and \"emotions\". You may interpret this to mean: \"She shakes her head mournfully. 'A sad place, really. Such a pity what happened to the Tockleys.'\"",
            "minScene": 3,
            "newRegion": "Tockley Manor"
          },
          {
            "id": 11,
            "name": "None",
            "description": null,
            "minScene": 3,
            "newRegion": null
          },
          {
            "id": 12,
            "name": "Something To Say",
            "description": "This is a catchall category Encounter for your Character learning something interesting, either from a Character or another source, such as a journal. What is said can be determined by asking Fate Questions or rolling on the Action Meaning Tables. Whatever is learned it should pertain to the murder, to some local strangeness, or to the next location IF you have learned of its existence yet.",
            "minScene": 4,
            "newRegion": null
          },
          {
            "id": 13,
            "name": "Weird Event",
            "description": "This Encounter is meant as a catchall for something very strange happening to your Character, including something that is overtly supernatural. Roll on the Description Meaning Tables for inspiration of what the Weird Event looks like, and roll on the Action Meaning Tables for inspiration about what happens. The severity of this Encounter is up to you, based on the Context and where your Character is. For instance, if your Character is currently in Radford Regional Park and rolls this Encounter, then gets \"inform\" and \"misfortune\" on the Action Meaning Tables, maybe your Character begins to hear strange whisperings in the woods that sound like threats.",
            "minScene": 4,
            "newRegion": null
          },
          {
            "id": 14,
            "name": "None",
            "description": null,
            "minScene": 4,
            "newRegion": null
          },
          {
            "id": 15,
            "name": "Something To Say",
            "description": "This is a catchall category Encounter for your Character learning something interesting, either from a Character or another source, such as a journal. What is said can be determined by asking Fate Questions or rolling on the Action Meaning Tables. Whatever is learned it should pertain to the murder, to some local strangeness, or to the next location IF you have learned of its existence yet.",
            "minScene": 5,
            "newRegion": null
          },
          {
            "id": 16,
            "name": "None",
            "description": null,
            "minScene": 5,
            "newRegion": null
          },
          {
            "id": 17,
            "name": "Weird Event",
            "description": "This Encounter is meant as a catchall for something very strange happening to your Character, including something that is overtly supernatural. Roll on the Description Meaning Tables for inspiration of what the Weird Event looks like, and roll on the Action Meaning Tables for inspiration about what happens. The severity of this Encounter is up to you, based on the Context and where your Character is. For instance, if your Character is currently in Radford Regional Park and rolls this Encounter, then gets \"inform\" and \"misfortune\" on the Action Meaning Tables, maybe your Character begins to hear strange whisperings in the woods that sound like threats.",
            "minScene": 6,
            "newRegion": null
          },
          {
            "id": 18,
            "name": "None",
            "description": null,
            "minScene": 6,
            "newRegion": null
          },
          {
            "id": 19,
            "name": "None",
            "description": null,
            "minScene": 6,
            "newRegion": null
          }
        ],
        "objects": [
          {
            "id": 1,
            "name": "None",
            "description": null,
            "minScene": null
          },
          {
            "id": 2,
            "name": "None",
            "description": null,
            "minScene": null
          },
          {
            "id": 3,
            "name": "None",
            "description": null,
            "minScene": null
          },
          {
            "id": 4,
            "name": "None",
            "description": null,
            "minScene": null
          },
          {
            "id": 5,
            "name": "Expected",
            "description": "An Element listing under a Category can simply say 'Expected.' This Category Element represents the mundane in your Region. As your Character enters a Region and explores, you will have expectations of what you will find: dark hallways in a dungeon, tangles of vines in a forest, enemy henchman patrolling a villain's lair. A Category result of 'Expected' produces just that, what you most expect for that Category.",
            "minScene": null
          },
          {
            "id": 6,
            "name": "None",
            "description": null,
            "minScene": null
          },
          {
            "id": 7,
            "name": "Random",
            "description": "A bit more interesting than 'expected' but not something so memorable or supernatural as 'wierd'. Consult your oracle.",
            "minScene": 2
          },
          {
            "id": 8,
            "name": "Dead Body",
            "description": "If you generate this Object for an Area, then you have discovered a new murder victim. Interpret how you find the body, and what state it's in, by the current Context and asking any Fate Questions you need to. For instance, let's say your Character is at Hoxel's Farm, rolls an Encounter of Closport Citizen, and rolls Dead Body for Object. After making some Fate Question rolls you may determine the following: Upon arriving at the farm, you look for the owner. You enter the barn and find someone standing over a dead body in the hay. Assuming you have investigated the original death that brought you to Closport, you probably know how that person died. A logical Fate Question to ask when finding a new body is, \"Did they die the same way?\" The Odds of a Yes are Sure Thing",
            "minScene": 2
          },
          {
            "id": 9,
            "name": "Artifact",
            "description": "This Object is meant for any unusual item you may find that adds mystery or information to the Adventure. It should pertain to the murder, to strangeness in town, or to the next area if you've learned of the place. For inspiration on what the Artifact is, roll on the Description Meaning Tables. For inspiration on what the Artifact means to the Adventure, roll on the Action Meaning Tables.",
            "minScene": 3
          },
          {
            "id": 10,
            "name": "None",
            "description": null,
            "minScene": 3
          },
          {
            "id": 11,
            "name": "Journal",
            "description": "Your Character discovers a written work, perhaps a book or personal journal, that contains useful insights. As with Artifact and Something To Say, this is an opportunity to expand on information about the murder, regions you have learned of. The Context of events that have happened so far should be taken into consideration.",
            "minScene": 4
          },
          {
            "id": 12,
            "name": "Expected",
            "description": "An Element listing under a Category can simply say 'Expected.' This Category Element represents the mundane in your Region. As your Character enters a Region and explores, you will have expectations of what you will find: dark hallways in a dungeon, tangles of vines in a forest, enemy henchman patrolling a villain's lair. A Category result of 'Expected' produces just that, what you most expect for that Category.",
            "minScene": 4
          },
          {
            "id": 13,
            "name": "None",
            "description": null,
            "minScene": 5
          },
          {
            "id": 14,
            "name": "Special",
            "description": "As the name says, something amazing or unusual. Consult your Oracle for details. Maybe it's twice as large, or unusual for this setting.",
            "minScene": 5
          },
          {
            "id": 15,
            "name": "Expected",
            "description": "An Element listing under a Category can simply say 'Expected.' This Category Element represents the mundane in your Region. As your Character enters a Region and explores, you will have expectations of what you will find: dark hallways in a dungeon, tangles of vines in a forest, enemy henchman patrolling a villain's lair. A Category result of 'Expected' produces just that, what you most expect for that Category.",
            "minScene": 5
          },
          {
            "id": 16,
            "name": "Random",
            "description": "A bit more interesting than 'expected' but not something so memorable or supernatural as 'wierd'. Consult your oracle.",
            "minScene": 6
          },
          {
            "id": 17,
            "name": "None",
            "description": null,
            "minScene": 6
          },
          {
            "id": 18,
            "name": "None",
            "description": null,
            "minScene": 7
          }
        ],
        "keyedScenes": [
          {
            "id": 1,
            "name": "I Want To Help",
            "triggerPercent": 20,
            "minScene": 3,
            "description": "An NPC approaches your Character, wanting to help with the investigation of the murder. Roll 1d10 to see who this is. On a 1-5 it is a Character from the Characters List. Roll to  Determine which one. On a 6-10 it's a new Character. Roll on the Description Meaning Tables for inspiration on a description for the Character, and roll on the Action Meaning Tables for inspiration on what the Character does or how they approach you. Add the new Character to the Characters List",
            "newRegion": null
          },
          {
            "id": 2,
            "name": "Strange Encounter In Closport",
            "triggerPercent": 20,
            "minScene": 3,
            "description": "This Encounter is meant as a catchall for something very strange happening to your Character, including something that is overtly supernatural. Roll on the Description Meaning Tables for inspiration of what the Weird Event looks like, and roll on the Action Meaning Tables for inspiration about what happens. The severity of this Encounter is up to you, based on the Context and where your Character is. For instance, if your Character is currently in Radford Regional Park and rolls this Encounter, then gets \"inform\" and \"misfortune\" on the Action Meaning Tables, maybe your Character begins to hear strange whisperings in the woods that sound like threats.",
            "newRegion": null
          },
          {
            "id": 3,
            "name": "Mysterious Message",
            "triggerPercent": 20,
            "minScene": 3,
            "description": "Your Character receives a message from a mysterious source, giving them a clue to their investigation. For inspiration on what form this message takes, and what it says, treat this as a Random Event, with an automatic Event Focus of Move Toward A Thread, with the Thread being \"Get to the bottom of the murder.\"",
            "newRegion": null
          },
          {
            "id": 4,
            "name": "Another Death",
            "triggerPercent": 10,
            "minScene": 3,
            "description": "If you generate this Object for an Area, then you have discovered a new murder victim. Interpret how you find the body, and what state it's in, by the current Context and asking any Fate Questions you need to. For instance, let's say your Character is at Hoxel's Farm, rolls an Encounter of Closport Citizen, and rolls Dead Body for Object. After making some Fate Question rolls you may determine the following: Upon arriving at the farm, you look for the owner. You enter the barn and find someone standing over a dead body in the hay. Assuming you have investigated the original death that brought you to Closport, you probably know how that person died. A logical Fate Question to ask when finding a new body is, \"Did they die the same way?\" The Odds of a Yes are Sure Thing",
            "newRegion": null
          },
          {
            "id": 5,
            "name": "Another Death",
            "triggerPercent": 10,
            "minScene": 5,
            "description": "If you generate this Object for an Area, then you have discovered a new murder victim. Interpret how you find the body, and what state it's in, by the current Context and asking any Fate Questions you need to. For instance, let's say your Character is at Hoxel's Farm, rolls an Encounter of Closport Citizen, and rolls Dead Body for Object. After making some Fate Question rolls you may determine the following: Upon arriving at the farm, you look for the owner. You enter the barn and find someone standing over a dead body in the hay. Assuming you have investigated the original death that brought you to Closport, you probably know how that person died. A logical Fate Question to ask when finding a new body is, \"Did they die the same way?\" The Odds of a Yes are Sure Thing",
            "newRegion": null
          },
          {
            "id": 6,
            "name": "Another Death",
            "triggerPercent": 10,
            "minScene": 7,
            "description": "If you generate this Object for an Area, then you have discovered a new murder victim. Interpret how you find the body, and what state it's in, by the current Context and asking any Fate Questions you need to. For instance, let's say your Character is at Hoxel's Farm, rolls an Encounter of Closport Citizen, and rolls Dead Body for Object. After making some Fate Question rolls you may determine the following: Upon arriving at the farm, you look for the owner. You enter the barn and find someone standing over a dead body in the hay. Assuming you have investigated the original death that brought you to Closport, you probably know how that person died. A logical Fate Question to ask when finding a new body is, \"Did they die the same way?\" The Odds of a Yes are Sure Thing",
            "newRegion": null
          },
          {
            "id": 7,
            "name": "Discover Tockley Manor",
            "triggerNumber": 7,
            "minScene": 4,
            "description": "This is a special Encounter where Tockley Manor is introduced to your Character. If you have already learned about Tockley through a Keyed Scene, then your Character gets more information about the Manor in this Encounter. You'll need to determine two things: how you learn about Tockley, and what information is attached to it. The how can be answered through a Fate Question using what seems most logical given the Context. For instance, if your Character is in a shop in Closport and you roll this Encounter, you may determine that the owner of the store tells you about it. \"The woman behind the counter sets down the music box and leans forward, saying in a conspiratorial voice, 'Have you heard of Tockley Manor?'\"  Aside from Characters, you may also learn of the Manor through books or journals. After you determine how you learn about the Manor, you need to attach what you learn about it. This should contain some element of mystery or local legend to it. For inspiration, roll on the Action Meaning Tables. For instance, in our example above of the shopkeeper mentioning Tockley, the Player rolls on the Action Meaning Tables and gets \"waste\" and \"emotions\". You may interpret this to mean: \"She shakes her head mournfully. 'A sad place, really. Such a pity what happened to the Tockleys.'\"",
            "newRegion": "Tockley Manor"
          }
        ]
      },
      {
        "id": 2,
        "name": "Tockley Manor",
        "isStartingRegion": false,
        "description": null,
        "locations": [
          {
            "id": 1,
            "name": "Expected",
            "description": "An Element listing under a Category can simply say 'Expected.' This Category Element represents the mundane in your Region. As your Character enters a Region and explores, you will have expectations of what you will find: dark hallways in a dungeon, tangles of vines in a forest, enemy henchman patrolling a villain's lair. A Category result of 'Expected' produces just that, what you most expect for that Category.",
            "minScene": null
          },
          {
            "id": 2,
            "name": "Expected",
            "description": "An Element listing under a Category can simply say 'Expected.' This Category Element represents the mundane in your Region. As your Character enters a Region and explores, you will have expectations of what you will find: dark hallways in a dungeon, tangles of vines in a forest, enemy henchman patrolling a villain's lair. A Category result of 'Expected' produces just that, what you most expect for that Category.",
            "minScene": null
          },
          {
            "id": 3,
            "name": "Hallway",
            "description": null,
            "minScene": null
          },
          {
            "id": 4,
            "name": "Library/Study",
            "description": "This can be any location that was once used to relax in, such as a library, study, sitting room, etc. This is a good location to search for books and other written records.",
            "minScene": null
          },
          {
            "id": 5,
            "name": "Dining Room",
            "description": "This is what you would expect of a dining room, with a central table and chairs and likely cabinets. There may be multiple dining rooms, some large and some small. You could alternately consider this a tea room with a single small table and a couple of chairs.",
            "minScene": null
          },
          {
            "id": 6,
            "name": "Kitchen",
            "description": "There is only one kitchen in the Manor, and it's a large room with a stove, pots and pans, knifes and cutlery, and plenty of room and counter space to prepare food for dozens of people at a time. Like everything else in the house, however, the room is cobwebby and decrepit.",
            "minScene": null
          },
          {
            "id": 7,
            "name": "Random",
            "description": "A bit more interesting than 'expected' but not something so memorable or supernatural as 'wierd'. Consult your oracle.",
            "minScene": 2
          },
          {
            "id": 8,
            "name": "Master Bedroom",
            "description": "This would be the largest bedroom in the house. It is still fully furnished, with a four poster bed, dresser, mirrors, etc.",
            "minScene": 2
          },
          {
            "id": 9,
            "name": "Hallway",
            "description": null,
            "minScene": 2
          },
          {
            "id": 10,
            "name": "Bedroom",
            "description": null,
            "minScene": 3
          },
          {
            "id": 11,
            "name": "Basement",
            "description": "Finding the basement is a good opportunity for something to happen in the dark and in an enclosed space. What \"basement\" actually means when you find it is up to you ... depending on the Context of the Adventure so far and the results of your Fate Questions.",
            "minScene": 3
          },
          {
            "id": 12,
            "name": "Special",
            "description": "As the name says, something amazing or unusual. Consult your Oracle for details. Maybe it's twice as large, or unusual for this setting.",
            "minScene": 3
          },
          {
            "id": 13,
            "name": "Graveyard",
            "description": "The graveyard is an outdoor location, but should still be considered as part of the house for exploration purposes. Finding the graveyard means you found a connection from your current Area to it, such as a door leading outside. Access from more unlikely locations, such as the second floor, may require more elaborate interpretations, such as a door that leads to an external staircase down to the graveyard. Having been untended for decades, the graveyard has grown wild with vegetation. It will likely feature vine strewn headstones that could obscure things, including encounters. The graveyard may also have other features in it, such as statues, depending on the results of Fate Questions you ask.",
            "minScene": 4
          },
          {
            "id": 14,
            "name": "Walk-in Closet",
            "description": "A mansion this large is going to have some very large closets. These can be considered small rooms and can be interpreted in a number of ways. For instance, if you encounter a walk-in closet after leaving the master bedroom, then it would make sense that this closet is in the bedroom. However, encountering it after leaving the kitchen may indicate that this is actually a walk in freezer. It can also be a pantry, a storage area in the basement, or just about any enclosed space intended for storage.",
            "minScene": 4
          },
          {
            "id": 15,
            "name": "Expected",
            "description": "An Element listing under a Category can simply say 'Expected.' This Category Element represents the mundane in your Region. As your Character enters a Region and explores, you will have expectations of what you will find: dark hallways in a dungeon, tangles of vines in a forest, enemy henchman patrolling a villain's lair. A Category result of 'Expected' produces just that, what you most expect for that Category.",
            "minScene": 5
          },
          {
            "id": 16,
            "name": "Laboratory",
            "description": "This should be considered an unusual room to find in the house, it’s name implying exactly what it is: a room full of scientific apparatus of unknown purpose. Interpretations for what you find in here should be connected with the Context of other strange things you have learned in the Adventure. The laboratory Location is a good way to expand on those earlier findings.",
            "minScene": 5
          },
          {
            "id": 17,
            "name": "Solarium",
            "description": "This is an indoor garden with at least one wall of glass, and the ceiling as well. All the plants are likely dead by now, or some may have grown wild.",
            "minScene": 6
          },
          {
            "id": 18,
            "name": "Random",
            "description": "A bit more interesting than 'expected' but not something so memorable or supernatural as 'wierd'. Consult your oracle.",
            "minScene": 6
          }
        ],
        "encounters": [
          {
            "id": 1,
            "name": "None",
            "description": null,
            "minScene": null,
            "resolutionPossible": null,
            "newRegion": null
          },
          {
            "id": 2,
            "name": "None",
            "description": null,
            "minScene": null,
            "resolutionPossible": null,
            "newRegion": null
          },
          {
            "id": 3,
            "name": "Weird Event",
            "description": "This Encounter is meant as a catchall for something very strange happening to your Character, including something that is overtly supernatural. Roll on the Description Meaning Tables for inspiration of what the Weird Event looks like, and roll on the Action Meaning Tables for inspiration about what happens. The severity of this Encounter is up to you, based on the Context and where your Character is. For instance, if your Character is currently in Radford Regional Park and rolls this Encounter, then gets \"inform\" and \"misfortune\" on the Action Meaning Tables, maybe your Character begins to hear strange whisperings in the woods that sound like threats.",
            "minScene": null,
            "resolutionPossible": null,
            "newRegion": null
          },
          {
            "id": 4,
            "name": "None",
            "description": null,
            "minScene": null,
            "resolutionPossible": null,
            "newRegion": null
          },
          {
            "id": 5,
            "name": "None",
            "description": null,
            "minScene": null,
            "resolutionPossible": null,
            "newRegion": null
          },
          {
            "id": 6,
            "name": "None",
            "description": null,
            "minScene": null,
            "resolutionPossible": null,
            "newRegion": null
          },
          {
            "id": 7,
            "name": "Random",
            "description": "A bit more interesting than 'expected' but not something so memorable or supernatural as 'wierd'. Consult your oracle.",
            "minScene": 2,
            "resolutionPossible": null,
            "newRegion": null
          },
          {
            "id": 8,
            "name": "House Hazard",
            "description": "This Encounter indicates that your Character has run into something dangerous in the house that pertains to the house itself. For instance, you might enter a bedroom and the floor gives out beneath you. Or, while exploring the solarium a piece of broken glass from the ceiling falls on you. For inspiration about the nature of the hazard, you can roll on the Description Meaning Tables for what the hazard looks like and on the Action Meaning Tables for the danger it poses.",
            "minScene": 2,
            "resolutionPossible": null,
            "newRegion": null
          },
          {
            "id": 9,
            "name": "Weird Event",
            "description": "This Encounter is meant as a catchall for something very strange happening to your Character, including something that is overtly supernatural. Roll on the Description Meaning Tables for inspiration of what the Weird Event looks like, and roll on the Action Meaning Tables for inspiration about what happens. The severity of this Encounter is up to you, based on the Context and where your Character is. For instance, if your Character is currently in Radford Regional Park and rolls this Encounter, then gets \"inform\" and \"misfortune\" on the Action Meaning Tables, maybe your Character begins to hear strange whisperings in the woods that sound like threats.",
            "minScene": 2,
            "resolutionPossible": null,
            "newRegion": null
          },
          {
            "id": 10,
            "name": "Opposition",
            "description": "Opposition is an Encounter for anything that might happen that involves someone or something directly opposing your further exploration. How this opposition takes shape will depend a lot on what you've learned so far in the Adventure. For instance, if you've discovered that there is a cult in Closport, which you believe committed the murder, then it would make sense that a cultist confronts you in the house. The opposition could be less violent, too.",
            "minScene": 3,
            "resolutionPossible": null,
            "newRegion": null
          },
          {
            "id": 11,
            "name": "House Hazard",
            "description": "This Encounter indicates that your Character has run into something dangerous in the house that pertains to the house itself. For instance, you might enter a bedroom and the floor gives out beneath you. Or, while exploring the solarium a piece of broken glass from the ceiling falls on you. For inspiration about the nature of the hazard, you can roll on the Description Meaning Tables for what the hazard looks like and on the Action Meaning Tables for the danger it poses.",
            "minScene": 3,
            "resolutionPossible": null,
            "newRegion": null
          },
          {
            "id": 12,
            "name": "The Secret",
            "description": "This Encounter is one of the two possible end goals of the Adventure. The Secret is the answer to the murder that drew you to Closport, or the root of the strangeness you have encountered along the way. What The Secret is can be just about anything. By this point in the Adventure you should have come across clues and information, and probably some oddities as well. This all forms the Context of this Encounter. If you have a good idea what The Secret is, then shape it into a Fate Question and ask.",
            "minScene": 4,
            "resolutionPossible": true,
            "newRegion": null
          },
          {
            "id": 13,
            "name": "The Entity",
            "description": "This is the second of the two possible end goals to the Adventure. The Entity is The Secret. The Entity is someone or something, most likely a supernatural creature, that is responsible for the death and much of the weirdness that you may have met with during the Adventure. This sets up a classic confrontation between your Character and “the boss” of the Adventure. This should be a dangerous encounter, where The Entity will likely try to have you suffer the same fate as the murder victim you are investigating. Determining the nature of The Entity is done randomly using the table below. Before rolling on the table, consider how many supernatural events have occurred to your Character so far in the Adventure, and turn this into a modifier for The Entity table.",
            "minScene": 5,
            "resolutionPossible": true,
            "newRegion": null
          },
          {
            "id": 14,
            "name": "Weird Event",
            "description": "This Encounter is meant as a catchall for something very strange happening to your Character, including something that is overtly supernatural. Roll on the Description Meaning Tables for inspiration of what the Weird Event looks like, and roll on the Action Meaning Tables for inspiration about what happens. The severity of this Encounter is up to you, based on the Context and where your Character is. For instance, if your Character is currently in Radford Regional Park and rolls this Encounter, then gets \"inform\" and \"misfortune\" on the Action Meaning Tables, maybe your Character begins to hear strange whisperings in the woods that sound like threats.",
            "minScene": 6
        },
        {
          "id": 15,
          "name": "Random",
          "description": "A bit more interesting than 'expected' but not something so memorable or supernatural as 'wierd'. Consult your oracle.",
          "minScene": 5,
          "newRegion": null
        },
        {
          "id": 16,
          "name": "Special",
          "description": "As the name says, something amazing or unusual. Consult your Oracle for details. Maybe it's twice as large, or unusual for this setting.",
          "minScene": 5,
          "newRegion": null
        },
        {
          "id": 17,
          "name": "Opposition",
          "description": "Opposition is an Encounter for anything that might happen that involves someone or something directly opposing your further exploration. How this opposition takes shape will depend a lot on what you've learned so far in the Adventure. For instance, if you've discovered that there is a cult in Closport, which you believe committed the murder, then it would make sense that a cultist confronts you in the house. The opposition could be less violent, too.",
        "minScene": 6,
          "newRegion": null
        },
        {
          "id": 18,
          "name": "None",
          "description": "",
          "minScene": 6,
          "newRegion": null
        },
        {
          "id": 19,
          "name": "Weird Event",
          "description": "This Encounter is meant as a catchall for something very strange happening to your Character, including something that is overtly supernatural. Roll on the Description Meaning Tables for inspiration of what the Weird Event looks like, and roll on the Action Meaning Tables for inspiration about what happens. The severity of this Encounter is up to you, based on the Context and where your Character is. For instance, if your Character is currently in Radford Regional Park and rolls this Encounter, then gets \"inform\" and \"misfortune\" on the Action Meaning Tables, maybe your Character begins to hear strange whisperings in the woods that sound like threats.",
          "minScene": 6,
          "newRegion": null
        }
      ],
      "objects": [
        {
          "id": 1,
          "name": "None",
          "description": "",
          "minScene": null
        },
        {
          "id": 2,
          "name": "Expected",
          "description": "An Element listing under a Category can simply say 'Expected.' This Category Element represents the mundane in your Region. As your Character enters a Region and explores, you will have expectations of what you will find: dark hallways in a dungeon, tangles of vines in a forest, enemy henchman patrolling a villain's lair. A Category result of 'Expected' produces just that, what you most expect for that Category.",
          "minScene": null
        },
        {
          "id": 3,
          "name": "None",
          "description": "",
          "minScene": null
        },
        {
          "id": 4,
          "name": "Evidence",
          "description": "This Object is something that reinforces clues your Character has already encountered or her current working theory on what is going on in Closport. If you don’t have a current working theory, then this Object should suggest a possible theory. Roll on the Description Meaning Tables for inspiration of what this Object looks like.",
          "minScene": null
        },
        {
          "id": 5,
          "name": "Expected",
          "description": "An Element listing under a Category can simply say 'Expected.' This Category Element represents the mundane in your Region. As your Character enters a Region and explores, you will have expectations of what you will find: dark hallways in a dungeon, tangles of vines in a forest, enemy henchman patrolling a villain's lair. A Category result of 'Expected' produces just that, what you most expect for that Category.",
          "minScene": null
        },
        {
          "id": 6,
          "name": "None",
          "description": "",
          "minScene": null
        },
        {
          "id": 7,
          "name": "Journal",
          "description": "Your Character discovers a written work, perhaps a book or personal journal, that contains useful insights. As with Artifact and Something To Say, this is an opportunity to expand on information about the murder, regions you have learned of. The Context of events that have happened so far should be taken into consideration.",
          "minScene": 2
        },
        {
          "id": 8,
          "name": "None",
          "description": "",
          "minScene": 2
        },
        {
          "id": 9,
          "name": "Dead Body",
          "description": "If you generate this Object for an Area, then you have discovered a new murder victim. Interpret how you find the body, and what state it's in, by the current Context and asking any Fate Questions you need to. For instance, let's say your Character is at Hoxel's Farm, rolls an Encounter of Closport Citizen, and rolls Dead Body for Object. After making some Fate Question rolls you may determine the following: Upon arriving at the farm, you look for the owner. You enter the barn and find someone standing over a dead body in the hay. Assuming you have investigated the original death that brought you to Closport, you probably know how that person died. A logical Fate Question to ask when finding a new body is, \"Did they die the same way?\" The Odds of a Yes are Sure Thing",
          "minScene": 2
        },
        {
          "id": 10,
          "name": "Evidence",
          "description": "This Object is something that reinforces clues your Character has already encountered or her current working theory on what is going on in Closport. If you don’t have a current working theory, then this Object should suggest a possible theory. Roll on the Description Meaning Tables for inspiration of what this Object looks like.",
          "minScene": 2
        },
        {
          "id": 11,
          "name": "None",
          "description": "",
          "minScene": 2
        },
        {
          "id": 12,
          "name": "Weird Object",
          "description": "This Encounter is meant as a catchall for something very strange happening to your Character, including something that is overtly supernatural. Roll on the Description Meaning Tables for inspiration of what the Weird Event looks like, and roll on the Action Meaning Tables for inspiration about what happens. The severity of this Encounter is up to you, based on the Context and where your Character is. For instance, if your Character is currently in Radford Regional Park and rolls this Encounter, then gets \"inform\" and \"misfortune\" on the Action Meaning Tables, maybe your Character begins to hear strange whisperings in the woods that sound like threats.",
          "minScene": 2
        },
        {
          "id": 13,
          "name": "Special",
          "description": "As the name says, something amazing or unusual. Consult your Oracle for details. Maybe it's twice as large, or unusual for this setting.",
          "minScene": 2
        },
        {
          "id": 14,
          "name": "Expected",
          "description": "An Element listing under a Category can simply say 'Expected.' This Category Element represents the mundane in your Region. As your Character enters a Region and explores, you will have expectations of what you will find: dark hallways in a dungeon, tangles of vines in a forest, enemy henchman patrolling a villain's lair. A Category result of 'Expected' produces just that, what you most expect for that Category.",
          "minScene": 2
        },
        {
          "id": 15,
          "name": "None",
          "description": "",
          "minScene": 2
        },
        {
          "id": 16,
          "name": "Random",
          "description": "A bit more interesting than 'expected' but not something so memorable or supernatural as 'wierd'. Consult your oracle.",
          "minScene": 2
        },
        {
          "id": 17,
          "name": "Expected",
          "description": "An Element listing under a Category can simply say 'Expected.' This Category Element represents the mundane in your Region. As your Character enters a Region and explores, you will have expectations of what you will find: dark hallways in a dungeon, tangles of vines in a forest, enemy henchman patrolling a villain's lair. A Category result of 'Expected' produces just that, what you most expect for that Category.",
          "minScene": 2
        },
        {
          "id": 18,
          "name": "Weird Object",
          "description": "This Encounter is meant as a catchall for something very strange happening to your Character, including something that is overtly supernatural. Roll on the Description Meaning Tables for inspiration of what the Weird Event looks like, and roll on the Action Meaning Tables for inspiration about what happens. The severity of this Encounter is up to you, based on the Context and where your Character is. For instance, if your Character is currently in Radford Regional Park and rolls this Encounter, then gets \"inform\" and \"misfortune\" on the Action Meaning Tables, maybe your Character begins to hear strange whisperings in the woods that sound like threats.",
          "minScene": 2
        }
      ],
      "keyedScenes": [
        {
          "id": 1,
          "name": "Strange Event In Tockley Manor",
          "triggerPercent": 20,
          "minScene": 3,
          "description": "This Encounter is meant as a catchall for something very strange happening to your Character, including something that is overtly supernatural. Roll on the Description Meaning Tables for inspiration of what the Weird Event looks like, and roll on the Action Meaning Tables for inspiration about what happens. The severity of this Encounter is up to you, based on the Context and where your Character is. For instance, if your Character is currently in Radford Regional Park and rolls this Encounter, then gets “inform” and “misfortune” on the Action Meaning Tables, maybe your Character begins to hear strange whisperings in the woods that sound like threats.",
          "newRegion": null
        },
        {
          "id": 2,
          "name": "The Entity Attacks",
          "triggerPercent": 20,
          "minScene": 5,
          "description": "This is the second of the two possible end goals to the Adventure. The Entity is The Secret. The Entity is someone or something, most likely a supernatural creature, that is responsible for the death and much of the weirdness that you may have met with during the Adventure. This sets up a classic confrontation between your Character and “the boss” of the Adventure. This should be a dangerous encounter, where The Entity will likely try to have you suffer the same fate as the murder victim you are investigating. Determining the nature of The Entity is done randomly using the table below. Before rolling on the table, consider how many supernatural events have occurred to your Character so far in the Adventure, and turn this into a modifier for The Entity table.",
          "resolutionPossible": true,
          "newRegion": null
        }
      ]
    }],
    "resolution": "The Entity is someone or something, most likely a supernatural creature, that is responsible for the death and much of the weirdness that you may have met with during the Adventure. This sets up a classic confrontation between your Character and \"the boss\" of the Adventure. This should be a dangerous encounter, where The Entity will likely try to have you suffer the same fate as the murder victim you are investigating. Determining the nature of The Entity is done randomly using the table below. Before rolling on the table, consider how many supernatural events have occurred to your Character so far in the Adventure, and turn this into a modifier for The Entity table.\n\nDetermining the nature of The Entity is done randomly using the table below. Before rolling on the table, consider how many supernatural events have occurred to your Character so far in the Adventure, and turn this into a modifier for The Entity table.\n\nNUMBER OF SUPERNATURAL EVENTS/MODIFIER\nNone/None\n1/+1\n2/+2\n3 or more/+4\n\nThe Entity\n\n1D10+ MODIFIER/THE NATURE OF THE ENTITY\n1/PERSON - The Entity is nothing supernatural, just a human being with motive.\n2-4/POWERED PERSON - As above, but the person is supernatural in some way. Maybe they're a sorcerer, an alchemist, has been gifted power by a demon, etc.\n5-6/VAMPIRE - The Entity is a vampire, an energy sucking creature that lives off the life force of living beings.\n7-8/CONSTRUCT - The Entity is a magical creature constructed by someone. This can be a golem made of clay, an animated statue, a corpse resurrected through strange science, etc.\n9-10/GHOST - The Entity is a ghost of some kind, some manner of incorporeal undead.\n11-14/OTHERWORLDLY BEING - The Entity is something very strange and alien, not of this world. This can be a demon, a creature from another plane of existence, something from beyond the stars, etc.\n\n"
}


</example>

<example>
{
    "firstScene": {
        "description": "Your starship is boldly going where no man has gone before when your comms officer in a fetching red miniskirt uniform informs you she is picking up what might be a distress signal coming from the nearby M class planet Regula Prime. Your science officer agrees that it looks like an older signal using a frequency that has long been discontinued due to its rather short range. The signals are very weak, but there are energy fluctuations from the planet possibly indicating advanced technology. Previously it was believed the planet was uninhabited. You form an away team. Suggested members include your science officer, your chief medical officer, if you can convince him to step into the transporter, the captain, of course, and maybe a few crewmen wearing bright red uniforms. You go to standard orbit and beam down. The adventure begins."
      },
      "threads": [
        {
          "id": 1,
          "name": "What is the source of the distress signal?"
        }
      ],
      "characters": [
        {
          "id": 1,
          "name": "Survivors",
          "description": "Placeholder for any survivors they might encounter"
        }
      ],
      "regions": [
        {
            "id": 1,
            "name": "The Crash Site",
            "isStartingRegion": true,
            "description": "The site of the colony ship's crash, a mix of wreckage and makeshift shelters.",
            "locations": [
                {
                    "id": 1,
                    "name": "Landing Zone",
                    "description": "Where the away team lands their shuttle or beams down.",
                    "minScene": 1
                },
                {
                    "id": 2,
                    "name": "Wreckage Site",
                    "description": "Remains of the original colony ship.",
                    "minScene": 2
                },
                {
                    "id": 3,
                    "name": "Survivor Encampment",
                    "description": "Temporary shelters made from the ship's remains, now abandoned.",
                    "minScene": 3
                },
                {
                    "id": 4,
                    "name": "Signal Beacon",
                    "description": "Old, malfunctioning distress signal.",
                    "minScene": 2
                },
                {
                    "id": 5,
                    "name": "Overgrown Pathway",
                    "description": "Leads deeper into the forest.",
                    "newRegion": "The Forest",
                    "minScene": 3
                },
                {
                    "id": 6,
                    "name": "Supply Cache",
                    "description": "Hidden supplies from the ship.",
                    "minScene": 4
                },
                {
                    "id": 7,
                    "name": "Old Communication Hub",
                    "description": "Ruined communication equipment.",
                    "minScene": 2
                },
                {
                    "id": 8,
                    "name": "Power Generator",
                    "description": "Damaged but repairable.",
                    "minScene": 2
                },
                {
                    "id": 9,
                    "name": "Medical Tent",
                    "description": "First aid supplies and makeshift hospital. It appears to have been in use long ago, perhaps when the survivors first arrived. Now abandoned.",
                    "minScene": 3
                },
                {
                    "id": 10,
                    "name": "Observation Point",
                    "description": "High ground for surveying the area.",
                    "minScene": 3
                },
                {
                    "id": 11,
                    "name": "Expected",
                    "description": "",
                    "minScene": 2
                },
                {
                    "id": 12,
                    "name": "Random",
                    "description": "",
                    "minScene": 3
                },
                {
                    "id": 13,
                    "name": "Expected",
                    "description": "",
                    "minScene": 3
                },
                {
                    "id": 14,
                    "name": "Expected",
                    "description": "",
                    "minScene": 4
                },
                {
                    "id": 15,
                    "name": "Random",
                    "description": "",
                    "minScene": 5
                },
                {
                    "id": 16,
                    "name": "Expected",
                    "description": "",
                    "minScene": 5
                }
            ],
            "encounters": [
                {
                    "id": 1,
                    "name": "Survivor's Welcome",
                    "description": "Meet Dr. Elena Kova, the lead scientist of the survivors, who is cautious but welcoming.",
                    "minScene": 4,
                    "newRegion": "Colony Town"
                },
                {
                    "id": 2,
                    "name": "Wreckage Investigation",
                    "description": "Find a strange ancient device of alien origin among the wreckage.",
                    "minScene": 2
                },
                {
                    "id": 3,
                    "name": "Distress Beacon Malfunction",
                    "description": "Repair the malfunctioning beacon, which provides clues about the colonists' situation.",
                    "minScene": 1
                },
                {
                    "id": 4,
                    "name": "Hidden Cache",
                    "description": "Discover a hidden stash of advanced medical supplies, hinting at strange technology.",
                    "minScene": 4
                },
                {
                    "id": 5,
                    "name": "Security Patrol",
                    "description": "Encounter a group of heavily armed colonists who are unusually aggressive. They don't seem happy to meet you or to be \"rescued\" by you.",
                    "minScene": 5
                },
                {
                    "id": 6,
                    "name": "Wildlife Attack",
                    "description": "Ambushed by local predators, requiring quick thinking to fend them off.",
                    "minScene": 1
                },
                {
                    "id": 7,
                    "name": "Communication Disruption",
                    "description": "A strange interference affects the away team's communication devices.",
                    "minScene": 1
                },
                {
                    "id": 8,
                    "name": "Mystery Illness",
                    "description": "A team member falls ill with a mysterious ailment.",
                    "minScene": 4
                },
                {
                    "id": 9,
                    "name": "Clandestine Meeting",
                    "description": "Overhear a secret conversation between colonists about \"The Serum.\"",
                    "minScene": 7
                },
                {
                    "id": 10,
                    "name": "Old Journal",
                    "description": "Find an old journal detailing early discoveries of the ancient technology.",
                    "minScene": 7
                },
                {
                    "id": 11,
                    "name": "Expected",
                    "description": "",
                    "minScene": 4
                },
                {
                    "id": 12,
                    "name": "None",
                    "description": "",
                    "minScene": 4
                },
                {
                    "id": 13,
                    "name": "None",
                    "description": "",
                    "minScene": 4
                },
                {
                    "id": 14,
                    "name": "Random",
                    "description": "",
                    "minScene": 4
                },
                {
                    "id": 15,
                    "name": "None",
                    "description": "",
                    "minScene": 5
                },
                {
                    "id": 16,
                    "name": "None",
                    "description": "",
                    "minScene": 5
                }
            ],
            "objects": [
                {
                    "id": 1,
                    "name": "Expected",
                    "description": "",
                    "minScene": 7
                },
                {
                    "id": 2,
                    "name": "Colony Logbook",
                    "description": "Records of the initial discoveries of the ancient tech and early experiments.",
                    "minScene": 3
                },
                {
                    "id": 3,
                    "name": "Broken Data Pad",
                    "description": "A damaged data pad containing encrypted files about...something.",
                    "minScene": 1
                },
                {
                    "id": 4,
                    "name": "Energy Cell",
                    "description": "A power cell from the wreckage that matches the technology found...where?",
                    "minScene": 3
                },
                {
                    "id": 5,
                    "name": "Map Fragment",
                    "description": "Part of a map showing the layout of an underground network.",
                    "minScene": 6
                },
                {
                    "id": 6,
                    "name": "Personal Journal",
                    "description": "Diary of a colonist detailing their experience.",
                    "minScene": 1
                },
                {
                    "id": 7,
                    "name": "Medical Kit",
                    "description": "Contains advanced medical tools and substances derived from somewhere? More advanced than expected technology...",
                    "minScene": 6
                },
                {
                    "id": 8,
                    "name": "None",
                    "description": "",
                    "minScene": 3
                },
                {
                    "id": 9,
                    "name": "None",
                    "description": "",
                    "minScene": 1
                },
                {
                    "id": 10,
                    "name": "Random",
                    "description": "",
                    "minScene": 6
                },
                {
                    "id": 11,
                    "name": "Special",
                    "description": "",
                    "minScene": 4
                },
                {
                    "id": 12,
                    "name": "None",
                    "description": "",
                    "minScene": 3
                },
                {
                    "id": 13,
                    "name": "None",
                    "description": "",
                    "minScene": 6
                }
            ],
            "keyedScenes": [
                {
                  "id": 1,
                  "name": "Wreckage Identified",
                  "triggerNumber": 3,
                  "minScene": 1,
                  "description": "The _Columbus_ an early earth exploration vessel was lost in this region. The crew is able to identify this ship having crashed on this planet, but that was almost 200 years ago.",
                  "newRegion": null
                }
              ]
                },
        {
            "id": 2,
            "name": "The Forest",
            "description": "A dense and mysterious forest, home to strange flora and fauna.",
            "locations": [
                {
                    "id": 1,
                    "name": "Dense Underbrush",
                    "description": "Difficult to navigate, full of wildlife.",
                    "minScene": 1
                },
                {
                    "id": 2,
                    "name": "Clearing",
                    "description": "Open area with strange flora.",
                    "minScene": 1
                },
                {
                    "id": 3,
                    "name": "Waterfall",
                    "description": "Source of fresh water.",
                    "minScene": 1
                },
                {
                    "id": 4,
                    "name": "Cave Entrance",
                    "description": "Leads to underground network.",
                    "minScene": 4,
                    "newRegion": "The Underground Network"
                },
                {
                    "id": 5,
                    "name": "Animal Lair",
                    "description": "Den of local wildlife.",
                    "minScene": 1
                },
                {
                    "id": 6,
                    "name": "Herb Garden",
                    "description": "Colony's medicinal plants.",
                    "minScene": 1
                },
                {
                    "id": 7,
                    "name": "Mushroom Grove",
                    "description": "Bioluminescent fungi.",
                    "minScene": 1
                },
                {
                    "id": 8,
                    "name": "Ancient Tree",
                    "description": "Massive, possibly sentient tree.",
                    "minScene": 1
                },
                {
                    "id": 9,
                    "name": "Hidden Path",
                    "description": "Leads to secret areas.",
                    "minScene": 4,
                    "newRegion": "The Old City"
                },
                {
                    "id": 10,
                    "name": "Forest Ruins",
                    "description": "Remnants of a previous civilization.",
                    "minScene": 4,
                    "newRegion": "The Old City"
                },
                {
                    "id": 11,
                    "name": "Expected",
                    "description": "",
                    "minScene": 4
                },
                {
                    "id": 12,
                    "name": "Expected",
                    "description": "",
                    "minScene": 4
                },
                {
                    "id": 13,
                    "name": "Expected",
                    "description": "",
                    "minScene": 5
                },
                {
                    "id": 14,
                    "name": "Expected",
                    "description": "",
                    "minScene": 5
                },
                {
                    "id": 15,
                    "name": "Expected",
                    "description": "",
                    "minScene": 6
                },
                {
                    "id": 16,
                    "name": "Expected",
                    "description": "",
                    "minScene": 6
                }
            ],
            "encounters": [
                {
                    "id": 1,
                    "name": "Guided Tour",
                    "description": "Meet Marcus Ren, a friendly but evasive colonist who offers to act as a guide. He doesn't seem to like you wondering around on your own.",
                    "minScene": 1
                },
                {
                    "id": 2,
                    "name": "Natural Trap",
                    "description": "The team encounters quicksand or a hidden pitfall.",
                    "minScene": 2
                },
                {
                    "id": 3,
                    "name": "Strange Flora",
                    "description": "Encounter plants with unusual properties, some of which might have amazing medical uses.",
                    "minScene": 3
                },
                {
                    "id": 4,
                    "name": "Lost Child",
                    "description": "Meet Lina, a young colonist who has wandered off and reveals bits of the colony's secret.",
                    "minScene": 3
                },
                {
                    "id": 5,
                    "name": "Hostile Wildlife",
                    "description": "Ambush by aggressive, genetically altered creatures.",
                    "minScene": 1
                },
                {
                    "id": 6,
                    "name": "Ancient Markings",
                    "description": "Discover ancient carvings that provide clues about a previous civilization.",
                    "minScene": 5
                },
                {
                    "id": 7,
                    "name": "Surveillance Devices",
                    "description": "Find hidden surveillance equipment monitoring the forest.",
                    "minScene": 3
                },
                {
                    "id": 8,
                    "name": "Expected",
                    "description": "",
                    "minScene": 1
                },
                {
                    "id": 9,
                    "name": "Natural Healing Spring",
                    "description": "Discover a spring with healing properties, used by the colonists.",
                    "minScene": 5
                },
                {
                    "id": 10,
                    "name": "Ambush",
                    "description": "Ambushed by colonist security forces, leading to a tense standoff.",
                    "minScene": 7
                },
                {
                    "id": 11,
                    "name": "Expected",
                    "description": "",
                    "minScene": 4
                },
                {
                    "id": 12,
                    "name": "None",
                    "description": "",
                    "minScene": 4
                },
                {
                    "id": 13,
                    "name": "None",
                    "description": "",
                    "minScene": 5
                },
                {
                    "id": 14,
                    "name": "None",
                    "description": "",
                    "minScene": 5
                },
                {
                    "id": 15,
                    "name": "None",
                    "description": "",
                    "minScene": 6
                },
                {
                    "id": 16,
                    "name": "Random",
                    "description": "",
                    "minScene": 6
                }
            ],
            "objects": [
                {
                    "id": 1,
                    "name": "Expected",
                    "description": "",
                    "minScene": 1
                },
                {
                    "id": 2,
                    "name": "Botanical Samples",
                    "description": "Plants native to the area seem useful. You take some to study their properties.",
                    "minScene": 2
                },
                {
                    "id": 3,
                    "name": "Random",
                    "description": "",
                    "minScene": 3
                },
                {
                    "id": 4,
                    "name": "Expected",
                    "description": "",
                    "minScene": 4
                },
                {
                    "id": 5,
                    "name": "Special",
                    "description": "",
                    "minScene": 3
                },
                {
                    "id": 6,
                    "name": "Ancient Amulet",
                    "description": "An amulet or other artifact worn by the ancient civilization of this planet.",
                    "minScene": 7
                },
                {
                    "id": 7,
                    "name": "Expected",
                    "description": "",
                    "minScene": 1
                },
                {
                    "id": 8,
                    "name": "Expected",
                    "description": "",
                    "minScene": 4
                },
                {
                    "id": 9,
                    "name": "None",
                    "description": "",
                    "minScene": 4
                },
                {
                    "id": 10,
                    "name": "None",
                    "description": "",
                    "minScene": 5
                },
                {
                    "id": 11,
                    "name": "Expected",
                    "description": "",
                    "minScene": 4
                },
                {
                    "id": 12,
                    "name": "None",
                    "description": "",
                    "minScene": 4
                },
                {
                    "id": 13,
                    "name": "None",
                    "description": "",
                    "minScene": 5
                },
                {
                    "id": 14,
                    "name": "None",
                    "description": "",
                    "minScene": 5
                },
                {
                    "id": 15,
                    "name": "None",
                    "description": "",
                    "minScene": 6
                },
                {
                    "id": 16,
                    "name": "Random",
                    "description": "",
                    "minScene": 6
                }
            ],
            "keyedScenes": [
                {
                  "id": 1,
                  "name": "Injury!",
                  "triggerPercent": 20,
                  "minScene": 3,
                  "description": "One of your crew has suffered a serious injury and needs medical attention.",
                  "newRegion": null
                }
              ]
                },
        {
            "id": 3,
            "name": "Colony Town",
            "description": "The heart of the colony survivors, a bustling town of people who seem to have been exceptionally prosperous.",
            "locations": [
                {
                    "id": 1,
                    "name": "Town Square",
                    "description": "Central gathering place.",
                    "minScene": 1
                },
                {
                    "id": 2,
                    "name": "Governor's House",
                    "description": "Residence of the colony's leader.",
                    "minScene": 2
                },
                {
                    "id": 3,
                    "name": "Marketplace",
                    "description": "Shops and stalls with goods.",
                    "minScene": 1
                },
                {
                    "id": 4,
                    "name": "Barracks",
                    "description": "Housing for colony security.",
                    "minScene": 3
                },
                {
                    "id": 5,
                    "name": "Workshop",
                    "description": "Engineers and craftsmen work here.",
                    "minScene": 3
                },
                {
                    "id": 6,
                    "name": "Hospital",
                    "description": "More advanced medical facility. In fact it seems very advanced.",
                    "minScene": 1
                },
                {
                    "id": 7,
                    "name": "Schoolhouse",
                    "description": "Educational center for children.",
                    "minScene": 4
                },
                {
                    "id": 8,
                    "name": "Tavern",
                    "description": "Social hub for colonists.",
                    "minScene": 4
                },
                {
                    "id": 9,
                    "name": "Warehouse",
                    "description": "Storage for supplies.",
                    "minScene": 5
                },
                {
                    "id": 10,
                    "name": "Secret Bunker",
                    "description": "Hidden room with crucial information.",
                    "minScene": 7
                },
                {
                    "id": 11,
                    "name": "Expected",
                    "description": "",
                    "minScene": 4
                },
                {
                    "id": 12,
                    "name": "Expected",
                    "description": "",
                    "minScene": 4
                },
                {
                    "id": 13,
                    "name": "Private Residence",
                    "description": "",
                    "minScene": 5
                },
                {
                    "id": 14,
                    "name": "Market or store",
                    "description": "",
                    "minScene": 5
                },
                {
                    "id": 15,
                    "name": "Public space",
                    "description": "",
                    "minScene": 5
                },
                {
                    "id": 16,
                    "name": "Alleyway",
                    "description": "",
                    "minScene": 5
                }
            ],
            "encounters": [
                {
                    "id": 1,
                    "name": "Market Encounter",
                    "description": "Meet Talia Mars, a friendly but curious market vendor. She has lots of questions about off planet life.",
                    "minScene": 1
                },
                {
                    "id": 2,
                    "name": "Public Speech",
                    "description": "The colony leader gives a rousing speech about the colony's self-sufficiency.",
                    "minScene": 4
                },
                {
                    "id": 3,
                    "name": "Eavesdropping",
                    "description": "Overhear colonists discussing the \"treatment\" they've received.",
                    "minScene": 4
                },
                {
                    "id": 4,
                    "name": "Suspicious Doctor",
                    "description": "Meet Dr. Isaac Voss, the colony's secretive doctor.",
                    "minScene": 3
                },
                {
                    "id": 5,
                    "name": "Marketplace Incident",
                    "description": "A conflict erupts in the marketplace, revealing tensions among colonists.",
                    "minScene": 4
                },
                {
                    "id": 6,
                    "name": "Hidden Clinic",
                    "description": "Discover a hidden clinic where a serum is administered to colonists. No one wants to talk about this or what it is for.",
                    "minScene": 6
                },
                {
                    "id": 7,
                    "name": "Black Market",
                    "description": "Encounter colonists trading stolen or illicit goods. These are people who might have information for a price.",
                    "minScene": 5
                },
                {
                    "id": 8,
                    "name": "Friendly Dinner",
                    "description": "Invited to dinner with a colonist family, who inadvertently reveal too much.",
                    "minScene": 6
                },
                {
                    "id": 9,
                    "name": "Unusual Strength",
                    "description": "Witness a colonist demonstrating unusual physical abilities.",
                    "minScene": 4
                },
                {
                    "id": 10,
                    "name": "Locked Building",
                    "description": "Find a building that is heavily guarded and off-limits.",
                    "minScene": 6
                },
                {
                    "id": 11,
                    "name": "Expected",
                    "description": "",
                    "minScene": 4
                },
                {
                    "id": 12,
                    "name": "None",
                    "description": "",
                    "minScene": 4
                },
                {
                    "id": 13,
                    "name": "None",
                    "description": "",
                    "minScene": 5
                },
                {
                    "id": 14,
                    "name": "None",
                    "description": "",
                    "minScene": 5
                },
                {
                    "id": 15,
                    "name": "None",
                    "description": "",
                    "minScene": 6
                },
                {
                    "id": 16,
                    "name": "Random",
                    "description": "",
                    "minScene": 6
                }
            ],
            "objects": [
                {
                    "id": 1,
                    "name": "Market Ledger",
                    "description": "A record of transactions that include references to something interesting.",
                    "minScene": 1
                },
                {
                    "id": 2,
                    "name": "Secret Journal",
                    "description": "The personal journal of Dr. Isaac Voss, detailing his doubts about \"the serum\".",
                    "minScene": 6
                },
                {
                    "id": 3,
                    "name": "Suspicious Package",
                    "description": "A package with vials of a serum and a note about its administration.",
                    "minScene": 5
                },
                {
                    "id": 4,
                    "name": "Blueprints",
                    "description": "Plans for a hidden lab and its equipment.",
                    "minScene": 7
                },
                {
                    "id": 5,
                    "name": "Expected",
                    "description": "",
                    "minScene": 1
                },
                {
                    "id": 6,
                    "name": "Random",
                    "description": "",
                    "minScene": 1
                },
                {
                    "id": 7,
                    "name": "Strange Coin",
                    "description": "An ancient coin that seems like it must belong to the old inhabitants of the planet.",
                    "minScene": 3
                },
                {
                    "id": 8,
                    "name": "Expected",
                    "description": "",
                    "minScene": 4
                },
                {
                    "id": 9,
                    "name": "None",
                    "description": "",
                    "minScene": 4
                },
                {
                    "id": 10,
                    "name": "None",
                    "description": "",
                    "minScene": 5
                },
                {
                    "id": 11,
                    "name": "Expected",
                    "description": "",
                    "minScene": 4
                },
                {
                    "id": 12,
                    "name": "None",
                    "description": "",
                    "minScene": 4
                },
                {
                    "id": 13,
                    "name": "None",
                    "description": "",
                    "minScene": 5
                },
                {
                    "id": 14,
                    "name": "None",
                    "description": "",
                    "minScene": 5
                },
                {
                    "id": 15,
                    "name": "None",
                    "description": "",
                    "minScene": 6
                },
                {
                    "id": 16,
                    "name": "Random",
                    "description": "",
                    "minScene": 6
                }
            ],
            "keyedScenes": [
                {
                  "id": 1,
                  "name": "We aren't leaving",
                  "triggerPercent": 20,
                  "triggerNumber": 3,
                  "minScene": 1,
                  "description": "Hansen Rike, the leader of the survivors, thanks you for your concern but declares they are perfectly happy and have no intention of leaving. He is not a man who likes to be questioned. He is polite but firm and distant.",
                  "newRegion": null
                },
                {
                  "id": 2,
                  "name": "Of course this happens",
                  "triggerPercent": 20,
                  "minScene": 3,
                  "description": "Dr. Elena Kova, lead scientist who might have met already (if not you meet her now) becomes amorously interested in one of the crew. Determine who it is. She clearly has some obligation to her people and will not betray them, but she also clearly has information. I wonder how you could get it out of her...",
                  "newRegion": null
                }
              ]
                },
        {
            "id": 4,
            "name": "The Underground Network",
            "description": "A maze of tunnels and chambers beneath the forest, holding secrets of the colony.",
            "locations": [
                {
                    "id": 1,
                    "name": "Cave Entrance",
                    "description": "Discovered in the forest.",
                    "minScene": 1
                },
                {
                    "id": 2,
                    "name": "Tunnel System",
                    "description": "Maze-like corridors.",
                    "minScene": 2
                },
                {
                    "id": 3,
                    "name": "Crystal Chamber",
                    "description": "Glowing crystals with unknown properties.",
                    "minScene": 2
                },
                {
                    "id": 4,
                    "name": "Subterranean Lake",
                    "description": "Underground water source.",
                    "minScene": 3
                },
                {
                    "id": 5,
                    "name": "Collapsed Tunnel",
                    "description": "Impassable without excavation.",
                    "minScene": 3
                },
                {
                    "id": 6,
                    "name": "Old Mine",
                    "description": "Abandoned mining operation.",
                    "minScene": 3
                },
                {
                    "id": 7,
                    "name": "Tunnel System",
                    "description": "Maze-like corridors.",
                    "minScene": 2
                },
                {
                    "id": 8,
                    "name": "Artifact Room",
                    "description": "Contains alien artifacts.",
                    "minScene": 5
                },
                {
                    "id": 9,
                    "name": "Entrance to Secret Laboratory",
                    "description": "Ask your oracle if it's locked. I bet a phaser could cut through it if it is.",
                    "minScene": 3,
                    "newRegion": "The Hidden Lab"
                },
                {
                    "id": 10,
                    "name": "Escape Route",
                    "description": "Leads back to the surface. But to an old abandoned city from the former inhabitants of the planet",
                    "newRegion":"The Old City",
                    "minScene": 3
                },
                {
                    "id": 11,
                    "name": "Expected",
                    "description": "",
                    "minScene": 4
                },
                {
                    "id": 12,
                    "name": "Expected",
                    "description": "",
                    "minScene": 4
                },
                {
                    "id": 13,
                    "name": "Expected",
                    "description": "",
                    "minScene": 5
                },
                {
                    "id": 14,
                    "name": "Expected",
                    "description": "",
                    "minScene": 5
                },
                {
                    "id": 15,
                    "name": "Expected",
                    "description": "",
                    "minScene": 6
                },
                {
                    "id": 16,
                    "name": "Random",
                    "description": "",
                    "minScene": 6
                }
            ],
            "encounters": [
                {
                    "id": 1,
                    "name": "None",
                    "description": "",
                    "minScene": 1
                },
                {
                    "id": 2,
                    "name": "Ancient Chamber",
                    "description": "Find a room with ancient alien inscriptions.",
                    "minScene": 3
                },
                {
                    "id": 3,
                    "name": "Hostile Encounter",
                    "description": "Ambushed by hostile colonists guarding the area.",
                    "minScene": 5
                },
                {
                    "id": 4,
                    "name": "Old Equipment",
                    "description": "Discover old mining equipment repurposed for extracting materials.",
                    "minScene": 3
                },
                {
                    "id": 5,
                    "name": "None",
                    "description": "",
                    "minScene": 1
                },
                {
                    "id": 6,
                    "name": "Subterranean Water Source",
                    "description": "There is a lot of it.",
                    "minScene": 3
                },
                {
                    "id": 7,
                    "name": "Collapse!",
                    "description": "A tunnel collapses. Does it separate the team? Is anyone hurt? Ask the oracle. A good opportunity requiring teamwork.",
                    "minScene": 5
                },
                {
                    "id": 8,
                    "name": "Alien Artifact",
                    "description": "Discover a powerful alien artifact",
                    "minScene": 4
                },
                {
                    "id": 9,
                    "name": "None",
                    "description": "",
                    "minScene": 1
                },
                {
                    "id": 10,
                    "name": "None",
                    "description": "",
                    "minScene": 1
                },
                {
                    "id": 11,
                    "name": "Expected",
                    "description": "",
                    "minScene": 4
                },
                {
                    "id": 12,
                    "name": "Expected",
                    "description": "",
                    "minScene": 4
                },
                {
                    "id": 13,
                    "name": "None",
                    "description": "",
                    "minScene": 5
                },
                {
                    "id": 14,
                    "name": "Random",
                    "description": "",
                    "minScene": 5
                },
                {
                    "id": 15,
                    "name": "None",
                    "description": "",
                    "minScene": 6
                },
                {
                    "id": 16,
                    "name": "None",
                    "description": "",
                    "minScene": 6
                }
            ],
            "objects": [
                {
                    "id": 1,
                    "name": "None",
                    "description": "",
                    "minScene": 1
                },
                {
                    "id": 2,
                    "name": "Sample Vial",
                    "description": "A vial labeled with a date and sample number. Clearly old. It seems they have been experimenting with something for a long time.",
                    "minScene": 3
                },
                {
                    "id": 3,
                    "name": "Hidden Camera",
                    "description": "A camera surveying the area. Have they seen you? Do they know you are here?",
                    "minScene": 4
                },
                {
                    "id": 4,
                    "name": "None",
                    "description": "",
                    "minScene": 3
                },
                {
                    "id": 5,
                    "name": "None",
                    "description": "",
                    "minScene": 4
                },
                {
                    "id": 6,
                    "name": "Power Conduit",
                    "description": "A piece of alien technology used to power a hidden area.",
                    "minScene": 4
                },
                {
                    "id": 7,
                    "name": "Rich vein of ore",
                    "description": "Your scans cannot identify it as any known substance.",
                    "minScene": 4
                },
                {
                    "id": 8,
                    "name": "None",
                    "description": "",
                    "minScene": 4
                },
                {
                    "id": 9,
                    "name": "None",
                    "description": "",
                    "minScene": 1
                },
                {
                    "id": 10,
                    "name": "None",
                    "description": "",
                    "minScene": 1
                },
                {
                    "id": 11,
                    "name": "Expected",
                    "description": "",
                    "minScene": 4
                },
                {
                    "id": 12,
                    "name": "Expected",
                    "description": "",
                    "minScene": 4
                },
                {
                    "id": 13,
                    "name": "None",
                    "description": "",
                    "minScene": 5
                },
                {
                    "id": 14,
                    "name": "Random",
                    "description": "",
                    "minScene": 5
                },
                {
                    "id": 15,
                    "name": "None",
                    "description": "",
                    "minScene": 6
                },
                {
                    "id": 16,
                    "name": "None",
                    "description": "",
                    "minScene": 6
                }
            ],
            "keyedScenes": [
                {
                  "id": 1,
                  "name": "A sudden reversal",
                  "triggerPercent": 20,
                  "minScene": 3,
                  "description": "Dr. Elena Kova, lead scientist who probably have met already turns up if she is not already with you. She is clearly distressed and asks you to leave the area and not pursue your investigation further.",
                  "newRegion": null
                }
              ]
                },
        {
            "id": 5,
            "name": "The Old City",
            "description": "A forgotten city of the ancient civilization, holding clues to the serum's history.",
            "locations": [
                {
                    "id": 1,
                    "name": "City Gates",
                    "description": "Entrance to ancient city.",
                    "minScene": 1
                },
                {
                    "id": 2,
                    "name": "Main Avenue",
                    "description": "Central thoroughfare.",
                    "minScene": 2
                },
                {
                    "id": 3,
                    "name": "Library",
                    "description": "Repository of ancient knowledge.",
                    "minScene": 3
                },
                {
                    "id": 4,
                    "name": "Temple",
                    "description": "Religious center of old civilization.",
                    "minScene": 5
                },
                {
                    "id": 5,
                    "name": "Marketplace Ruins",
                    "description": "Abandoned market.",
                    "minScene": 3
                },
                {
                    "id": 6,
                    "name": "Residential District",
                    "description": "Homes of the ancient populace.",
                    "minScene": 2
                },
                {
                    "id": 7,
                    "name": "Council Hall",
                    "description": "Meeting place of old city leaders.",
                    "minScene": 3
                },
                {
                    "id": 8,
                    "name": "Statue Plaza",
                    "description": "Monuments to ancient heroes.",
                    "minScene": 2
                },
                {
                    "id": 9,
                    "name": "Underground Vault",
                    "description": "Secure storage with secrets.",
                    "minScene": 4
                },
                {
                    "id": 10,
                    "name": "Entrance to a Hidden Laboratory",
                    "description": "Ask your oracle if it's locked. I bet a phaser could cut through it if it is.",
                    "minScene": 4,
                    "newRegion": "The Hidden Lab"
                }
            ],
            "encounters": [
                {
                    "id": 1,
                    "name": "Encounter the Historian",
                    "description": "Meet Elder Kor, a historian who knows much about the ancient civilization. He is a kind and wise academic and clearly has a love for the ancient ruins.",
                    "minScene": 1
                },
                {
                    "id": 2,
                    "name": "Literary Discovery",
                    "description": "Ancient texts detailing the immortality technology using a serum. But immortality comes at a heavy cost.",
                    "minScene": 2
                },
                {
                    "id": 3,
                    "name": "None",
                    "description": "",
                    "minScene": 3
                },
                {
                    "id": 4,
                    "name": "Ambush",
                    "description": "Attacked or confronted by colonists wanting to keep the city a secret.",
                    "minScene": 4
                },
                {
                    "id": 5,
                    "name": "Clue",
                    "description": "Find evidence that reinforces your current theory.",
                    "minScene": 1
                },
                {
                    "id": 6,
                    "name": "None",
                    "description": "",
                    "minScene": 3
                },
                {
                    "id": 7,
                    "name": "Expected",
                    "description": "",
                    "minScene": 3
                },
                {
                    "id": 8,
                    "name": "Expected",
                    "description": "",
                    "minScene": 2
                },
                {
                    "id": 9,
                    "name": "Environmental Hazard",
                    "description": "",
                    "minScene": 4
                },
                {
                    "id": 10,
                    "name": "None",
                    "description": "",
                    "minScene": 2
                }
            ],
            "objects": [
                {
                    "id": 1,
                    "name": "Alien Device",
                    "description": "What does it do?",
                    "minScene": 2
                },
                {
                    "id": 2,
                    "name": "None",
                    "description": "",
                    "minScene": 2
                },
                {
                    "id": 3,
                    "name": "Historical Record",
                    "description": "Records of the ancient civilization's decline.",
                    "minScene": 2
                },
                {
                    "id": 4,
                    "name": "None",
                    "description": "",
                    "minScene": 2
                },
                {
                    "id": 5,
                    "name": "Mysterious Key",
                    "description": "A key that opens something...",
                    "minScene": 3
                },
                {
                    "id": 6,
                    "name": "Tablet of Laws",
                    "description": "An ancient law tablet that explains the ethical considerations of ancient society. Did they live up to their own ethics?",
                    "minScene": 2
                },
                {
                    "id": 7,
                    "name": "Guardian Statue",
                    "description": "An impressive statue of a long dead race.",
                    "minScene": 1
                },
                {
                    "id": 8,
                    "name": "None",
                    "description": "",
                    "minScene": 1
                },
                {
                    "id": 9,
                    "name": "None",
                    "description": "",
                    "minScene": 3
                },
                {
                    "id": 10,
                    "name": "None",
                    "description": "",
                    "minScene": 4
                }
            ],
            "keyedScenes": [
                {
                  "id": 1,
                  "name": "Old Technology Comes to life",
                  "triggerPercent": 20,
                  "minScene": 2,
                  "description": "A crewman accidentally activates some ancient tech. Perhaps there is a message or something else. Maybe it is dangerous. Ask your oracle for details but you learn things that reinforce your current suspicions.",
                  "newRegion": null
                }
              ]
                },
        {
                "id": 6,
                "name": "The Hidden Lab",
                "description": "A ancient labratory where the colonists have taken over and where the serum is developed and tested.",
                "locations": [
                    {
                        "id": 1,
                        "name": "Entrance",
                        "description": "Concealed entrance.",
                        "minScene": 1
                    },
                    {
                        "id": 2,
                        "name": "Research Lab",
                        "description": "Ongoing experiments.",
                        "minScene": 2
                    },
                    {
                        "id": 3,
                        "name": "Control Room",
                        "description": "Monitors the entire lab.",
                        "minScene": 2
                    },
                    {
                        "id": 4,
                        "name": "Specimen Containment",
                        "description": "Some of these don't look pleasant.",
                        "minScene": 2
                    },
                    {
                        "id": 5,
                        "name": "Medical Bay",
                        "description": "Advanced medical tech.",
                        "minScene": 2
                    },
                    {
                        "id": 6,
                        "name": "Power Core",
                        "description": "Lab's energy source.",
                        "minScene": 2
                    }
                ],
                "encounters": [
                    {
                        "id": 1,
                        "name": "Conflict",
                        "description": "Meet Guard Captain Rhea, head of security, fiercely loyal to the colony's leadership.",
                        "minScene": 1
                    },
                    {
                        "id": 2,
                        "name": "Expected",
                        "description": "",
                        "minScene": 1
                    },
                    {
                        "id": 3,
                        "name": "None",
                        "description": "",
                        "minScene": 1
                    },
                    {
                        "id": 4,
                        "name": "Computer Systems",
                        "description": "Access records showing the serum's side effects and ethical concerns and development. Perhaps this system could be used to destroy the lab in some way.",
                        "minScene": 1
                    },
                    {
                        "id": 5,
                        "name": "None",
                        "description": "",
                        "minScene": 1
                    }
                ],
                "objects": [
                    {
                        "id": 1,
                        "name": "Records, Log Entries",
                        "description": "Documenting the development and side effects of the serum.",
                        "minScene": 2
                    },
                    {
                        "id": 2,
                        "name": "None",
                        "description": "",
                        "minScene": 1
                    },
                    {
                        "id": 3,
                        "name": "None",
                        "description": "",
                        "minScene": 1
                    },
                    {
                        "id": 4,
                        "name": "Expected",
                        "description": "",
                        "minScene": 1
                    },
                    {
                        "id": 5,
                        "name": "None",
                        "description": "",
                        "minScene": 1
                    }
                ],
                "keyedScenes": [
                    {
                      "id": 1,
                      "name": "A tense encounter",
                      "triggerPercent": 20,
                      "minScene": 1,
                      "description": "Your crew is confronted at gun point...er phaser point. Inerpret it in context. Who does it? How do you resolve it?",
                      "newRegion": null
                    },
                    {
                      "id": 2,
                      "name": "The big ending",
                      "triggerPercent": 20,
                      "triggerNumber": 5,
                      "minScene": 3,
                      "description": "Hansen Rike, the leader of the survivors, confronts you here. How does this end?",
                      "resolutionPossible": true,
                      "newRegion": null
                    }
                  ]
                        }
        ],
        "resolution": "By now you have uncovered the dark secret behind this place and established that what they are doing is morally compromised. You cannot let it continue. What are your options? A dramatic speech that turns it all around? Cold logic? A show of force? Time travel to get some humpback whales? What kind of support does Rike have? Does he have superhuman abilities? Perhaps a beautiful woman has a role to play."
    }

</example>


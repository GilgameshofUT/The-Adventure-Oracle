So I would love to populate this with all the cool modules I own or know of but there is a slight problem of copyright. There are many, many free adventure modules out there but that doesn't mean it is OK for me to use them to make a derivative work and put it on a Github repo. One of the problems I ran into is many of the higher quality modules are restrictive and many of the Creative Commons modules are very sandboxy or just a dungeon crawl. While a dungeon crawl would work fine with this system, it also doesn't give it a lot of advantage over procedurally generated systems. The whole point is that this system can preserve some aspects of narrative and plot while still mixing things up a bit.

For my personal use I have been converting copywritten modules I own into the JSON format for this system using AI and it has worked great. Since I can't share that output I needed a sample to use and after looking around and not finding anything great under a creative commons license I finally turned to Project Gutenberg and the book *A Princess of Mars* by Edgar Rice Burroughs which is public domain. I used AI to turn the first 15 chapters of the book into a pretty detailed adventure module, included in this directory.

I then used this module with some AI prompts I have written to convert it to the correct JSON format. To do this I include the module wrapped in <story> </story> tags, the README file giving documentation of the program wrapped in tags, and two complete JSON files as examples. I did this using the free teir of Gemini 1.5 Pro found at https://aistudio.google.com. Temperature was set to 1 and safety settings were all turned off (because they are stupid).

I thought the best way to present this is by using numbered files for each prompt and each output. The prompts will likely work fine in other AI systems but you need a very big context window, probably 50-70K tokens. There are many models that support this today, but some models will not and most chatbots will not. 

To get this to work you will need to get your adventure into plain text. This is a purely text based system. It will not consider maps or artwork. Moving from PDF to text is sometimes a bit of a pain. Make sure your text is readable. I find with many PDFs I have to cut and paste small areas to get the text exported properly. This system does not use any gamee mechanics, so get the flavor text and don't worry about the stat blocks.

The JSON is a bit too big to output in one go. As you will see I do it in chunks. There is some cutting and pasting to assemble it into a single file. JSON is pretty picky about commas and brackets. I recommend you use a JSON editor to make sure you have it right.

Good luck!

So that should be it. Use the prompts included in this directory

So a note on this. The first prompt worked really well. I sometimes need to add another prompt in there to tell it to make more/smaller regions in the plan after the 1st prompt, but it came up with ~16~ 25 regions which is a lot.
Once it did stop mid generation for reasons unknown. I just had it rerun that answer and it was fine. Try to spot check it along the way. By the end this giant adventure used 94,615 tokens of context.

I wish there was a way to get it to assemble it all into one file with the AI but it can't do that. Maximum output is 8,193 tokens. So you have to cut and paste it all together yourself. Watch out for all the commas in the right place. It has to be valid JSON. But there is a trick to make it easier. Use the "Get code" button to copy it all at once to the clipboard, then remove the parts that aren't part of the JSON output. 
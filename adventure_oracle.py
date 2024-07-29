import json
import random
import os
import sys
import pickle
from datetime import datetime

class AdventureOracle:
    def __init__(self, json_file):
        self.json_file = json_file
        self.state_file = f'state/adventure_state_{os.path.basename(json_file)}.pkl'
        self.output_file = f"logs/adventure_log_{os.path.basename(json_file)}.md"
        self.load_state()

    def load_state(self):
        if os.path.exists(self.state_file):
            with open(self.state_file, 'rb') as f:
                state = pickle.load(f)
                self.data = state['data']
                self.current_region = state['current_region']
                self.discovered_regions = state['discovered_regions']
                self.scene_counts = state['scene_counts']
        else:
            with open(self.json_file, 'r') as f:
                self.data = json.load(f)
            self.current_region = None
            self.discovered_regions = set()
            self.scene_counts = {}
            self.initialize_game()

    def save_state(self):
        state = {
            'data': self.data,
            'current_region': self.current_region,
            'discovered_regions': self.discovered_regions,
            'scene_counts': self.scene_counts
        }
        with open(self.state_file, 'wb') as f:
            pickle.dump(state, f)

    def initialize_game(self):
        self.current_entry=""
        self.output("# Adventure Oracle\n")
        self.output(f"## First Scene\n{self.data['firstScene']['description']}\n")
        
        self.output("## Threads")
        for i, thread in enumerate(self.data['threads'], 1):
            self.output(f"{i}. {thread['name']}")
        self.output("")
        
        self.output("## Characters")
        for i, character in enumerate(self.data['characters'], 1):
            self.output(f"{i}. {character['name']} - {character['description']}")
        self.output("")
        
        for region in self.data['regions']:
            if region['isStartingRegion']:
                self.current_region = region
                self.discovered_regions.add(region['name'])
                break
        
        self.output(f"# Current Region: {self.current_region['name']}")
        self.output(f"## Description: \n{self.current_region['description']}\n")
        self.end_entry()

    def start_new_entry(self):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.current_entry = f"---\n\n>[!Adventure_Oracle] {timestamp}\n\n"

    def output(self, text):
        print(text)
        self.current_entry += text + "\n"

    def end_entry(self):
        self.current_entry += "---\n\n"
        with open(self.output_file, 'a') as f:
            f.write(self.current_entry)
        self.current_entry = ""

    def display_options(self):
        options = []
        if len(self.discovered_regions) > 1:
            options.append("1. New Region")
        options.append("2. New Area")
        options.append("3. Reset State")
        options.append("4. Exit Program")
        
        print("\n" + "\n".join(options))

    def handle_new_region(self):
        print("\nDiscovered Regions:")
        for i, region_name in enumerate(self.discovered_regions, 1):
            print(f"{i}. {region_name}")
        
        while True:
            try:
                choice = int(input("Choose a region number: "))
                if 1 <= choice <= len(self.discovered_regions):
                    chosen_region = list(self.discovered_regions)[choice - 1]
                    break
                else:
                    print(f"Invalid choice. Please enter a number between 1 and {len(self.discovered_regions)}.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        for region in self.data['regions']:
            if region['name'] == chosen_region:
                self.current_region = region
                break
        
        self.start_new_entry()
        self.output(f"# Current Region: {self.current_region['name']}")
        self.output(f"## Description: \n{self.current_region['description']}\n")
        self.end_entry()

    def handle_new_area(self):
        self.start_new_entry()
        region_name = self.current_region['name']
        if region_name not in self.scene_counts:
            self.scene_counts[region_name] = 0
        self.scene_counts[region_name] += 1
        scene_count = self.scene_counts[region_name]

        # Handle KeyedScenes
        for keyed_scene in self.current_region['keyedScenes'][:]:
            if scene_count >= (keyed_scene.get('minScene') or 0):
                trigger = False
                if 'triggerNumber' in keyed_scene and scene_count >= keyed_scene['triggerNumber']:
                    trigger = True
                elif 'triggerPercent' in keyed_scene and random.randint(1, 100) <= keyed_scene['triggerPercent']:
                    trigger = True
                
                if trigger:
                    self.output(f"# Keyed Scene: \n{keyed_scene['name']}")
                    self.output(f"## Description: \n{keyed_scene['description']}")
                    if keyed_scene.get('newRegion'):
                        self.discovered_regions.add(keyed_scene['newRegion'])
                    if keyed_scene.get('resolutionPossible'):
                        self.output(f"\n# Resolution: \n{self.data['resolution']}")
                    self.current_region['keyedScenes'].remove(keyed_scene)

        # Handle Locations, Encounters, and Objects
        for category in ['locations', 'encounters', 'objects']:
            items = [item for item in self.current_region[category] if scene_count >= (item.get('minScene') or 0)]
            if items:
                chosen_item = random.choice(items)
                self.output(f"**{category.capitalize()}:** {chosen_item['name']}")
                if chosen_item.get('description'):
                    self.output(f"**Description:** {chosen_item['description']}")
                if chosen_item.get('newRegion'):
                    self.discovered_regions.add(chosen_item['newRegion'])
                if chosen_item.get('resolutionPossible'):
                    self.output(f"\n# Resolution: \n{self.data['resolution']}")
                self.current_region[category].remove(chosen_item)
            else:
                self.output(f"{category.capitalize()}: Complete")
        self.end_entry()

    def reset_state(self):
        if os.path.exists(self.state_file):
            os.remove(self.state_file)
        self.load_state()

    def run(self):
        while True:
            self.display_options()
            choice = input("Enter your choice: ")
            
            if choice == "1" and len(self.discovered_regions) > 1:
                self.handle_new_region()
            elif choice == "2":
                self.handle_new_area()
            elif choice == "3":
                self.reset_state()
            elif choice == "4":
                self.save_state()
                print("Exiting program. State saved.")
                break
            else:
                print("Invalid choice. Please try again.")
            
            self.save_state()  # Save state after each action

def choose_json_file():
    adventures_dir = "adventures"
    if not os.path.exists(adventures_dir):
        print(f"Error: '{adventures_dir}' directory not found.")
        sys.exit(1)
    
    json_files = [f for f in os.listdir(adventures_dir) if f.endswith('.json')]
    if not json_files:
        print(f"Error: No JSON files found in '{adventures_dir}' directory.")
        sys.exit(1)
    
    print("Available adventure files:")
    for i, file in enumerate(json_files, 1):
        print(f"{i}. {file}")
    
    while True:
        try:
            choice = int(input("Choose a file number: "))
            if 1 <= choice <= len(json_files):
                return os.path.join(adventures_dir, json_files[choice - 1])
            else:
                print(f"Invalid choice. Please enter a number between 1 and {len(json_files)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        json_file = sys.argv[1]
    else:
        json_file = choose_json_file()
    
    oracle = AdventureOracle(json_file)
    oracle.run()
""" generation of a csv file for the creation of a dataset (DND)"""
from tqdm import tqdm

DOC = """ The docstring for a class should summarize its behavior and list the public
methods and instance variables. If the class is intended to be subclassed,
and has an additional interface for subclasses, this interface should be
listed separately (in the docstring). The class constructor should be
documented in the docstring for its __init__ method. Individual methods
should be documented by their own docstring."""

class DNDPromptGeneration():
    """Generation of a csv file with a lot of possible prompts"""
    
    _ACHIEVEMENT_SCALE = [
        "Catastrophic Failure",
        "Significant Failure",
        "Major Struggle",
        "Partial Failure",
        "Barely Missed It",
        "Barely Got It",
        "Lucky Success",
        "Solid Success",
        "Great Success",
        "Exceptional Achievement"
      ]

    _DIFFICULTY_SCALE = [
          "Extremely Easy",
          "Very Easy",
          "Quite Easy",
          "Easy",
          "Moderately Easy",
          "Fairly Easy",
          "Slightly Easy",
          "Somewhat Easy",
          "Neutral/Moderate",
          "Somewhat Challenging",
          "Slightly Challenging",
          "Fairly Challenging",
          "Moderately Challenging",
          "Challenging",
          "Quite Challenging",
          "Difficult",
          "Very Difficult",
          "Extremely Difficult",
          "Nearly Impossible",
          "Impossible"
        ]

    _names = [
            "Aelar Windrider",
            "Kethra Nightbreeze",
            "Thorin Stonearm",
            "Lirael Swiftfoot",
            "Zephyr Silverkin",
            "Elowen Moonshadow",
            "Grommash Ironfist",
            "Elysia Ravensong",
            "Faelan Lightbringer",
            "Thalia Stormrider",
            "Branoc Thunderbeard",
            "Elira Fireheart",
            "Ishara Starfall",
            "Grimm Stonebreaker",
            "Elowyn Winterleaf",
            "Caelin Shadowstrike",
            "Vaelin Darkthorn",
            "Seraphina Moonwhisper",
            "Haldor Stormrider",
            "Veridia Bloodraven",
            "Faelarion Dawnbringer",
            "Kharak Grimaxe",
            "Lyria Whisperwind",
            "Baelor Frostbeard",
            "Nalani Sunblade",
        ]

    _race = [
            "Human",
            "Elf",
            "Dwarf",
            "Halfling",
            "Gnome",
            "Half-Orc",
            "Half-Elf",
            "Tiefling",
            "Dragonborn",
            "Aasimar",
            "Goliath",
            "Firbolg",
            "Triton",
            "Tabaxi",
            "Genasi",
            "Kenku",
            "Warforged",
            "Aarakocra",
            "Lizardfolk",
            "Goblin",
            "Hobgoblin",
            "Kobold",
            "Orc",
            "Centaur",
            "Minotaur",
            "Tortle",
            "Changeling",
            "Shifter",
            "Kalashtar",
            "Gith",
        ]

    _action = [
            "Attack with a melee weapon",
            "Attack with a ranged weapon",
            "Cast a spell",
            "Dodge",
            "Dash",
            "Disengage",
            "Hide",
            "Help (assist another character)",
            "Grapple",
            "Shove (knock an opponent prone or push them)",
            "Parry (if the character has the ability)",
            "Ready an action",
            "Use an object",
            "Interact with the environment",
            "Search for hidden objects or secret doors",
            "Investigate a crime scene",
            "Persuade an NPC",
            "Intimidate an NPC",
            "Deceive an NPC",
            "Perform in a tavern",
            "Tame a wild animal",
            "Ride a mount",
            "Climb a wall or tree",
            "Swim",
            "Investigate a mysterious artifact",
            "Craft an item (e.g., potions, weapons, armor)",
            "Use a magical item",
            "Concoct a plan",
            "Diplomatically negotiate with hostile creatures",
            "Interrogate a captured enemy",
            "Create a distraction",
            "Disarm a trap",
            "Break down a door",
            "Solve a puzzle",
            "Recite ancient lore",
            "Write or compose a song or poem",
            "Pray to a deity",
            "Investigate a curse or disease",
            "Inspect the stars for navigation",
            "Use a magic item to scry or communicate",
            "Bargain with a merchant",
            "Steal an item",
            "Create a diversion",
            "Cast a ritual spell",
            "Perform a ritual for a magical effect",
            "Persuade an elemental to aid you",
            "Research forgotten knowledge in a library",
            "Formulate a battle strategy",
            "Make a pact with a supernatural entity",
            "Create an illusion to deceive or distract",
            "Rally your allies with a speech",
            "Attempt a death-defying stunt",
            "Perform an act of heroism",
            "Resist temptation or corruption",
            "Perform an exorcism",
            "Cast a unique or homebrewed spell",
            "Contribute to a community project",
            "Set up a trap or ambush",
            "Execute a complex acrobatic maneuver",
            "Create a work of art",
            "Lead a military unit in battle",
            "Set up an alchemical experiment",
            "Tell a gripping story or legend",
            "Inspire hope in others",
            "Perform a feat of incredible strength",
            "Enact a ritual to bind a powerful creature",
            "Create a masterpiece of craftsmanship",
            "Navigate treacherous terrain",
            "Lead a rebellion against an oppressive regime",
            "Attempt to tame or ride a dragon",
            "Forge a pact with a fey lord or lady",
            "Perform a dangerous scientific experiment",
            "Build a stronghold or base of operations",
            "Complete an epic quest",
            "Seek out a legendary artifact or relic"
        ]

    def mkPrompt(self, a, b, c, d, e):
        '''
        Returns:
            return(str):
        '''
        message = f'Explain how {self._names[a]} a {self._race[b]} tried to {self._action[c]} of {self._DIFFICULTY_SCALE[d]} difficulty and got an {self._ACHIEVEMENT_SCALE[e]}'

        return message

    def arrPrompt(self):
        arr = []
        for a in tqdm(range(len(self._names))):
            for b in range(len(self._race)):
                for c in range(len(self._action)):
                    for d in range(len(self._DIFFICULTY_SCALE)):
                        for e in range(len(self._ACHIEVEMENT_SCALE)):
                            arr.append(self.mkPrompt(a, b, c, d, e))
        return arr

    def mkFile(self,pathName,data):
        import csv


        # Open the CSV file in write mode
        with open(pathName, 'w', newline='') as file:
            writer = csv.writer(file)

            # Write each element of the array as a separate row in the CSV
            for line in tqdm(data):
                writer.writerow([line])

        print(f"CSV file '{pathName}' has been created.")

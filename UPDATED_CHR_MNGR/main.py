import os
from menu import menu
from viz import QuickViz
from stats import QuickStats
from random_gen import QuickRandom
import add_character
import attribute_manager
import inventory_manager
import selecter
import skill_manager


def calculate_attributes(characters, classes, races, items):
    """
    Calculate character attributes based on base stats, class, race, and inventory.
    """
    def lookup(data_list): 
        index = {entry["name"]: entry for entry in data_list}
        def find(name):
            return index.get(name)
        return find

    def attribute_applier():
        keys = ["dmg", "dex", "int", "con", "cha"]
        def apply(attributes, source):
            if source:
                for i, key in enumerate(keys):
                    if key in source:
                        attributes[i] *= source[key]
        return apply

    find_race = lookup(races)
    find_class = lookup(classes)
    apply_multipliers = attribute_applier()

    for character in characters:
        character["attributes"] = [float(val) for val in character["base_attributes"]]

        race_data = find_race(character["race"])
        class_data = find_class(character["class"])

        for item in character["inventory"]:
            apply_multipliers(character["attributes"], item)

        apply_multipliers(character["attributes"], race_data)
        apply_multipliers(character["attributes"], class_data)

    return characters


def display_help_menu():
    """
    Display the help menu with descriptions for each option.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== Help Menu ===")
    help_texts = [
        "Add Character: Create a new character for your RPG. Set their name, class, race, level, and attributes.",
        "Manage Skills: Add, remove, or view skills for your character. Customize their abilities and powers.",
        "Manage Inventory: Equip your character with items. Add, remove, or view their inventory.",
        "Manage Attributes: Modify your character's core stats like strength, dexterity, and intelligence.",
        "View / Compare Characters: Compare two characters side by side or view details of a single character.",
        "Select / Search Characters: Search for and select a character to manage."
    ]
    for i, text in enumerate(help_texts, 1):
        print(f"{i}. {text}")
    input("\nPress Enter to return to the main menu...")


def main():
    """
    Main function to run the RPG Character Manager.
    """
    print("Welcome to the RPG Character Manager!")
    selected_character = "example character 1"
    options = [
        "Add Character", "Manage Skills", "Manage Inventory", "Manage Attributes",
        "View / Compare Characters", "Select / Search Characters", "Help",
        f' (Your current selected character is "{selected_character}")',
        "Visualization", "Statistics", "Random Generator"
    ]

    # Initialize data
    classes = [
        {"name": "rogue", "dmg": 1.2, "dex": 1.5, "int": 1.1, "con": 0.9, "cha": 1.2},
        {"name": "warrior", "dmg": 1.5, "dex": 0.9, "int": 0.8, "con": 1.4, "cha": 1.0},
        {"name": "mage", "dmg": 1.3, "dex": 0.8, "int": 1.6, "con": 0.7, "cha": 1.1},
        {"name": "paladin", "dmg": 1.2, "dex": 0.9, "int": 1.0, "con": 1.3, "cha": 1.4},
        {"name": "ranger", "dmg": 1.3, "dex": 1.4, "int": 1.0, "con": 1.0, "cha": 1.0},
        {"name": "bard", "dmg": 0.9, "dex": 1.1, "int": 1.2, "con": 0.9, "cha": 1.6},
        {"name": "tank", "dmg": 0.9, "dex": 0.7, "int": 0.8, "con": 1.7, "cha": 0.9}
    ]
    races = [
        {"name": "Human", "dmg": 1.0, "dex": 1.0, "int": 1.0, "con": 1.0, "cha": 1.0},
        {"name": "Elf", "dmg": 0.9, "dex": 1.2, "int": 1.1, "con": 0.9, "cha": 1.1},
        {"name": "Ork", "dmg": 1.3, "dex": 0.8, "int": 0.7, "con": 1.2, "cha": 0.8},
        {"name": "Dwarf", "dmg": 1.1, "dex": 0.8, "int": 0.9, "con": 1.3, "cha": 0.9},
        {"name": "Halfling", "dmg": 0.8, "dex": 1.3, "int": 1.0, "con": 0.9, "cha": 1.2}
    ]
    items = [
        {"name": "Iron Sword", "dmg": 1.2, "weight": 5.0, "value": 150, "effects": "Sharp edge, reliable weapon"},
        {"name": "Dagger", "dex": 1.3, "weight": 1.5, "value": 75, "effects": "Lightweight, easy to conceal"},
        {"name": "Wizard Staff", "int": 1.4, "weight": 3.0, "value": 300, "effects": "Channeling magic, arcane focus"},
        {"name": "Heavy Armor", "con": 1.5, "weight": 25.0, "value": 500, "effects": "High protection, reduced mobility"},
        {"name": "Silver Amulet", "cha": 1.3, "weight": 0.2, "value": 200, "effects": "Enchanted charm, noble appearance"}
    ]
    characters = [
        {
            "name": "example character 1",
            "class": "rogue",
            "level": 15,
            "race": "Elf",
            "attributes": [],
            "base_attributes": [5, 5, 5, 5, 5],
            "skills": set(),
            "skill_levels": {},
            "inventory": [],
            "backstory": "A mysterious rogue from the shadows",
            "location": "Shadowfen",
            "personality": "Sneaky and cunning"
        }
    ]

    saved_skills = skill_manager.initialize_default_skills()

    # Main menu loop
    while True:
        choice = menu(options)
        if choice.get('index') == 0:
            characters = add_character.add_menu(characters, classes, races, items)
        elif choice.get('index') == 1:
            if selected_character:
                characters, selected_character = skill_manager.skill_menu(saved_skills, characters, selected_character)
            else:
                print("Please select a character before entering this function.")
                input("Press Enter to continue...")
        elif choice.get('index') == 2:
            if selected_character:
                characters, selected_character = inventory_manager.inventory_menu(items, characters, selected_character)
            else:
                print("Please select a character before entering this function.")
                input("Press Enter to continue...")
        elif choice.get('index') == 3:
            if selected_character:
                characters, selected_character = attribute_manager.attribute_menu(characters, selected_character)
            else:
                print("Please select a character before entering this function.")
                input("Press Enter to continue...")
        elif choice.get('index') == 4:
            print("View/Compare Characters functionality is not implemented.")
            input("Press Enter to continue...")
        elif choice.get('index') == 5:
            characters, selected_character = selecter.selecter_menu(characters, selected_character)
        elif choice.get('index') == 6:
            display_help_menu()
        elif choice.get('index') == 7:
            options[7] = f' (Your current selected character is "{selected_character}")'
        elif choice.get('index') == 8:
            viz = QuickViz()
            print("\n=== VISUALIZATION ===")
            char_list = list(characters)
            for i, c in enumerate(char_list):
                print(f"{i}. {c['name']}")
            try:
                idx = int(input("Pick character number: "))
                if 0 <= idx < len(char_list):
                    c = char_list[idx]
                    chars_copy = calculate_attributes([c], classes, races, items)
                    stats = chars_copy[0]['attributes'] if chars_copy[0]['attributes'] else chars_copy[0]['base_attributes']
                    viz.radar(c['name'], stats)
                else:
                    print("Invalid!")
                    input("Press Enter...")
            except ValueError:
                print("Invalid!")
                input("Press Enter...")
        elif choice.get('index') == 9:
            stats = QuickStats()
            chars_copy = calculate_attributes(list(characters), classes, races, items)
            stats.report(chars_copy)
            input("Press Enter...")
        elif choice.get('index') == 10:
            rand = QuickRandom()
            print("\n=== RANDOM GENERATOR ===")
            print("1. Random Character")
            print("2. Random Quest")
            sub = input("Choice: ")
            if sub == '1':
                new = rand.character(classes, races)
                new['inventory'] = []
                new['skills'] = set()
                characters.append(new)
                print(f"\nCreated: {new['name']} the {new['class']}")
                print(f"Race: {new['race']} Level: {new['level']}")
                print(f"Backstory: {new['backstory']}")
                input("Press Enter...")
            elif sub == '2':
                print(f"\nQUEST: {rand.quest()}")
                input("Press Enter...")
main()
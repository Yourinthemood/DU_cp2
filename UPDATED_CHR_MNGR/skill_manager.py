from menu import menu

def skill_menu(saved_skills, characters, selected_character):
    """
    Main skill management menu for managing skills of a selected character.
    """
    if not characters:
        print("No characters available!")
        input("Press Enter to continue...")
        return characters, selected_character

    if selected_character == "":
        char_names = [char["name"] for char in characters]
        char_names.append("Return")
        result = menu(char_names)
        selected_index = result['index']
        
        if selected_index >= len(characters):
            return characters, selected_character
        
        selected_character = characters[selected_index]["name"]
    
    current_character = get_character(characters, selected_character)
    
    if current_character is None:
        print("Character not found!")
        input("Press Enter to continue...")
        return characters, ""
    
    skill_manage = True
    while skill_manage:
        result = menu(["Add Skill", "Remove Skill", "View Character Skills", "Level Up Skill", "View Skill Tree", "Return"])
        selected_index = result['index']
        
        if selected_index == 0:
            handle_add_skill(saved_skills, current_character)
        elif selected_index == 1:
            handle_remove_skill(current_character, saved_skills)
        elif selected_index == 2:
            handle_view_skills(saved_skills, current_character)
        elif selected_index == 3:
            handle_level_up_skill(saved_skills, current_character)
        elif selected_index == 4:
            handle_view_skill_tree(saved_skills, current_character)
        else:
            skill_manage = False
    
    return characters, selected_character


def get_character(characters, selected_character):
    """
    Helper function to find a character by name.
    """
    for char in characters:
        if char["name"] == selected_character:
            return char
    return None


def initialize_skill_levels(character):
    """
    Initialize the skill_levels dictionary for a character if it doesn't exist.
    """
    if "skill_levels" not in character:
        character["skill_levels"] = {}


def initialize_default_skills():
    """
    Create a comprehensive skill library with 25+ skills organized by type.
    """
    def create_skill(description, effect, amount, target, level_req=1, max_level=10, prerequisites=None):
        """
        Inner function to create a skill dictionary.
        """
        return {
            "description": description,
            "effect": effect,
            "amount": amount,
            "target": target,
            "level_requirement": level_req,
            "max_level": max_level,
            "prerequisites": prerequisites if prerequisites else [],
            "min_prerequisite_level": 1
        }
    
    skills = {}
    
    # BASIC COMBAT SKILLS
    skills["Basic Strike"] = create_skill("A simple physical attack", "Attack", 10, "Enemy", 1, 5)
    skills["Defend"] = create_skill("Raise your guard to block attacks", "Defense", 5, "Self", 1, 5)
    skills["Minor Heal"] = create_skill("Restore a small amount of health", "Health", 15, "Self", 1, 5)
    
    # FIRE MAGIC TREE
    skills["Spark"] = create_skill("Shoot a small spark of fire", "Attack", 15, "Enemy", 2, 8)
    skills["Fireball"] = create_skill("Launch a ball of flames", "Attack", 50, "Enemy", 5, 10, ["Spark"])
    skills["Flame Wave"] = create_skill("A wave of fire hits all enemies", "Attack", 40, "Enemy", 8, 10, ["Fireball"])
    skills["Inferno"] = create_skill("Devastating flames engulf the battlefield", "Attack", 100, "Enemy", 15, 10, ["Flame Wave"])
    skills["Phoenix Fire"] = create_skill("Legendary flames that revive the caster", "Health", 80, "Self", 20, 10, ["Inferno"])
    
    # ICE MAGIC TREE
    skills["Frost Touch"] = create_skill("Freeze an enemy with a touch", "Attack", 12, "Enemy", 2, 8)
    skills["Ice Shard"] = create_skill("Launch sharp ice projectiles", "Attack", 45, "Enemy", 5, 10, ["Frost Touch"])
    skills["Blizzard"] = create_skill("Summon a freezing storm", "Attack", 70, "Enemy", 10, 10, ["Ice Shard"])
    skills["Absolute Zero"] = create_skill("Ultimate ice magic freezes everything", "Attack", 120, "Enemy", 18, 10, ["Blizzard"])
    
    # HEALING TREE
    skills["Heal"] = create_skill("Restore moderate health", "Health", 30, "Self", 3, 10, ["Minor Heal"])
    skills["Greater Heal"] = create_skill("Restore significant health", "Health", 60, "Self", 7, 10, ["Heal"])
    skills["Mass Heal"] = create_skill("Heal all allies", "Health", 40, "Ally", 12, 10, ["Greater Heal"])
    skills["Resurrection"] = create_skill("Bring an ally back from defeat", "Health", 100, "Ally", 15, 10, ["Mass Heal"])
    
    return skills


# Placeholder functions for skill management actions
def handle_add_skill(saved_skills, current_character):
    """
    Handle adding a skill to the current character.
    """
    print("Add Skill functionality is not implemented yet.")


def handle_remove_skill(current_character, saved_skills):
    """
    Handle removing a skill from the current character.
    """
    print("Remove Skill functionality is not implemented yet.")


def handle_view_skills(saved_skills, current_character):
    """
    Handle viewing the current character's skills.
    """
    print("View Skills functionality is not implemented yet.")


def handle_level_up_skill(saved_skills, current_character):
    """
    Handle leveling up a skill for the current character.
    """
    print("Level Up Skill functionality is not implemented yet.")


def handle_view_skill_tree(saved_skills, current_character):
    """
    Handle viewing the skill tree for the current character.
    """
    print("View Skill Tree functionality is not implemented yet.")
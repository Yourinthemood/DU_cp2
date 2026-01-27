# Password Generator Program
# This program helps users create strong passwords by letting them choose what to include

import random

def show_menu():
    #Shows the main menu and gets user choice
    print("\n" + "="*50)
    print("PASSWORD GENERATOR")
    print("="*50)
    print("Type the number for what you want to do:")
    print("1. Generate Passwords")
    print("2. Exit")
    
    # Get user choice and check if it's valid
    while True:
        try:
            choice = input("Your choice (1 or 2): ").strip()
            if choice == "1" or choice == "2":
                return choice
            else:
                print("Please type 1 or 2 only!")
        except:
            print("Something went wrong. Try again.")

def get_password_settings():
    #Asks user what they want in their password
    print("\n" + "-"*50)
    print("PASSWORD SETTINGS")
    print("-"*50)
    
    # Get password length
    while True:
        try:
            length = int(input("How long does the password need to be: ").strip())
            if length > 0:
                break
            else:
                print("Please enter a positive number!")
        except:
            print("Please enter a valid number!")
    
    # Get what characters to include
    # We ask Yes/No questions for each type
    settings = {}
    
    # Ask about lowercase letters
    while True:
        lower = input("Does the password need lowercase letters (Y/N): ").strip().upper()
        if lower == "Y" or lower == "N":
            settings['lower'] = (lower == "Y")
            break
        else:
            print("Please type Y or N!")
    
    # Ask about uppercase letters
    while True:
        upper = input("Does the password need uppercase letters (Y/N): ").strip().upper()
        if upper == "Y" or upper == "N":
            settings['upper'] = (upper == "Y")
            break
        else:
            print("Please type Y or N!")
    
    # Ask about numbers
    while True:
        numbers = input("Does the password need numbers (Y/N): ").strip().upper()
        if numbers == "Y" or numbers == "N":
            settings['numbers'] = (numbers == "Y")
            break
        else:
            print("Please type Y or N!")
    
    # Ask about special characters
    while True:
        special = input("Does the password need special characters (Y/N): ").strip().upper()
        if special == "Y" or special == "N":
            settings['special'] = (special == "Y")
            break
        else:
            print("Please type Y or N!")
    
    # Check that at least one type is selected
    if not (settings['lower'] or settings['upper'] or settings['numbers'] or settings['special']):
        print("\n⚠  WARNING: You need to select at least one type of character!")
        print("I'll add lowercase letters for you.")
        settings['lower'] = True
    
    settings['length'] = length
    return settings

def get_possible_characters(settings):
    #Creates a list of characters we can use based on user settings
    possible_chars = ""
    
    # Add lowercase letters if wanted
    if settings['lower']:
        possible_chars += "abcdefghijklmnopqrstuvwxyz"
    
    # Add uppercase letters if wanted
    if settings['upper']:
        possible_chars += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # Add numbers if wanted
    if settings['numbers']:
        possible_chars += "0123456789"
    
    # Add special characters if wanted
    if settings['special']:
        possible_chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    return possible_chars

def generate_one_password(settings, possible_chars):
    #Generates one password that meets all the rules
    password = ""
    
    # Make sure we have at least one of each required type
    password_parts = []
    
    if settings['lower']:
        password_parts.append(random.choice("abcdefghijklmnopqrstuvwxyz"))
    
    if settings['upper']:
        password_parts.append(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    
    if settings['numbers']:
        password_parts.append(random.choice("0123456789"))
    
    if settings['special']:
        password_parts.append(random.choice("!@#$%^&*()_+-=[]{}|;:,.<>?"))
    
    # Start with our required characters
    password = ''.join(password_parts)
    
    # Fill the rest with random characters from all allowed types
    while len(password) < settings['length']:
        password += random.choice(possible_chars)
    
    # Shuffle the password so the required characters aren't always at the beginning
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)
    
    return password

def generate_passwords():
    #Main function to generate 4 passwords
    # Get what the user wants
    settings = get_password_settings()
    
    # Get the characters we can use
    possible_chars = get_possible_characters(settings)
    
    print("\n" + "="*50)
    print("POSSIBLE PASSWORDS")
    print("="*50)
    
    # Generate and show 4 passwords
    for i in range(4):
        password = generate_one_password(settings, possible_chars)
        print(f"Password {i+1}: {password}")
    
    print("\n Done! These passwords meet all your requirements.")
    print("TIP: Choose one and never share it with anyone!")

def main():
    #Main function that runs the whole program
    print("Welcome to the Password Generator!")
    print("This program helps you create strong, secure passwords.")
    
    # Keep running until user chooses to exit
    while True:
        choice = show_menu()
        
        if choice == "1":
            generate_passwords()
        elif choice == "2":
            print("\nThank you for using the Password Generator!")
            print("stay safe!")
            break
        
        # Ask if user wants to go back to menu (unless they chose exit)
        if choice == "1":
            while True:
                again = input("\nDo you want to make more passwords? (Y/N): ").strip().upper()
                if again == "Y":
                    break
                elif again == "N":
                    print("\nThank you for using the Password Generator!")
                    print("I hope you come back to create passwords with us again soon!")
                    return
                else:
                    print("Please type Y or N!")

main()

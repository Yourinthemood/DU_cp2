"""
Personal Library Manager
A program to keep track of your books, movies, and music
"""

import csv
import os

# File to save the library
FILE_NAME = "my_library.csv"

# List to store all items (each item is a dictionary)
my_library = []

# Track if we have unsaved changes
changes_made = False

def main():
    """Main program function"""
    global my_library, changes_made
    
    print("=" * 40)
    print("     MY PERSONAL LIBRARY")
    print("=" * 40)
    
    # Load library from file
    load_library()
    
    # Main loop
    while True:
        print("\n--- MAIN MENU ---")
        print("1. Quick view (Title + Creator)")
        print("2. Detailed view (All info)")
        print("3. Add an item")
        print("4. Update an item")
        print("5. Delete an item")
        print("6. Save to file")
        print("7. Reload from file")
        print("8. Exit")
        
        choice = get_choice(1, 8)
        
        if choice == 1:
            show_simple()
        elif choice == 2:
            show_detailed()
        elif choice == 3:
            add_item()
        elif choice == 4:
            update_item()
        elif choice == 5:
            delete_item()
        elif choice == 6:
            save_library()
        elif choice == 7:
            reload_library()
        elif choice == 8:
            exit_program()
            break

def get_choice(min_num, max_num):
    """Get a number choice from user"""
    while True:
        try:
            choice = int(input(f"\nChoice ({min_num}-{max_num}): "))
            if min_num <= choice <= max_num:
                return choice
            else:
                print(f"Please pick {min_num}-{max_num}")
        except ValueError:
            print("That's not a number. Try again.")

def load_library():
    """Load library from CSV file"""
    global my_library
    
    try:
        # Check if file exists
        if not os.path.exists(FILE_NAME):
            print(f"No file found. Starting with empty library.")
            my_library = []
            return
        
        my_library = []
        with open(FILE_NAME, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Try to convert year to number
                try:
                    row['year'] = int(row['year'])
                except:
                    pass  # Keep as string if can't convert
                my_library.append(row)
        
        print(f"Loaded {len(my_library)} items from {FILE_NAME}")
        
    except Exception as e:
        print(f"Error loading file: {e}")
        my_library = []

def save_library():
    """Save library to CSV file"""
    global changes_made
    
    try:
        with open(FILE_NAME, 'w', newline='') as file:
            # Make sure we have all possible fields
            fieldnames = ['title', 'creator', 'year', 'genre', 'format', 'rating', 'notes']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            
            # Write header
            writer.writeheader()
            
            # Write all items
            for item in my_library:
                # Make sure all fields exist
                row = {}
                for field in fieldnames:
                    row[field] = item.get(field, '')
                writer.writerow(row)
        
        changes_made = False
        print(f"Saved {len(my_library)} items to {FILE_NAME}")
        
    except Exception as e:
        print(f"Error saving: {e}")

def show_simple():
    """Show just title and creator"""
    if not my_library:
        print("\nLibrary is empty!")
        return
    
    print("\n" + "-" * 50)
    print("QUICK VIEW")
    print("-" * 50)
    
    for i, item in enumerate(my_library, 1):
        title = item.get('title', 'No title')
        creator = item.get('creator', 'No creator')
        print(f"{i}. {title} - {creator}")

def show_detailed():
    """Show all information"""
    if not my_library:
        print("\nLibrary is empty!")
        return
    
    print("\n" + "-" * 60)
    print("DETAILED VIEW")
    print("-" * 60)
    
    for i, item in enumerate(my_library, 1):
        print(f"\n--- Item #{i} ---")
        print(f"Title: {item.get('title', 'N/A')}")
        print(f"Creator: {item.get('creator', 'N/A')}")
        print(f"Year: {item.get('year', 'N/A')}")
        print(f"Genre: {item.get('genre', 'N/A')}")
        
        # Optional fields
        if item.get('format'):
            print(f"Format: {item['format']}")
        if item.get('rating'):
            print(f"Rating: {item['rating']}")
        if item.get('notes'):
            print(f"Notes: {item['notes']}")

def add_item():
    """Add a new item to library"""
    global changes_made
    
    print("\n--- ADD NEW ITEM ---")
    print("(Press Enter to skip optional fields)")
    
    new_item = {}
    
    # Required fields
    new_item['title'] = input("Title: ").strip()
    while not new_item['title']:
        print("Title cannot be empty!")
        new_item['title'] = input("Title: ").strip()
    
    new_item['creator'] = input("Creator (author/artist/director): ").strip()
    while not new_item['creator']:
        print("Creator cannot be empty!")
        new_item['creator'] = input("Creator: ").strip()
    
    # Year (try to get number)
    year_input = input("Year: ").strip()
    while year_input:
        try:
            new_item['year'] = int(year_input)
            break
        except:
            print("Please enter a number (or press Enter to skip)")
            year_input = input("Year: ").strip()
    else:
        new_item['year'] = ''
    
    new_item['genre'] = input("Genre: ").strip()
    while not new_item['genre']:
        print("Genre cannot be empty!")
        new_item['genre'] = input("Genre: ").strip()
    
    # Optional fields
    print("\nOptional fields:")
    new_item['format'] = input("Format (Book/Movie/Album): ").strip()
    new_item['rating'] = input("Rating (1-5): ").strip()
    new_item['notes'] = input("Notes: ").strip()
    
    # Add to library
    my_library.append(new_item)
    changes_made = True
    print("\nItem added successfully!")

def update_item():
    """Update an existing item"""
    global changes_made
    
    if not my_library:
        print("\nLibrary is empty!")
        return
    
    show_simple()
    
    try:
        num = int(input(f"\nEnter item number to update (1-{len(my_library)}): "))
        if num < 1 or num > len(my_library):
            print("Invalid number!")
            return
        
        item = my_library[num - 1]
        print("\n--- UPDATE ITEM ---")
        print("(Press Enter to keep current value)")
        
        # Update fields
        new_title = input(f"Title [{item['title']}]: ").strip()
        if new_title:
            item['title'] = new_title
        
        new_creator = input(f"Creator [{item['creator']}]: ").strip()
        if new_creator:
            item['creator'] = new_creator
        
        new_year = input(f"Year [{item['year']}]: ").strip()
        if new_year:
            try:
                item['year'] = int(new_year)
            except:
                print("Invalid year, keeping old value")
        
        new_genre = input(f"Genre [{item['genre']}]: ").strip()
        if new_genre:
            item['genre'] = new_genre
        
        # Optional fields
        new_format = input(f"Format [{item.get('format', '')}]: ").strip()
        if new_format:
            item['format'] = new_format
        
        new_rating = input(f"Rating [{item.get('rating', '')}]: ").strip()
        if new_rating:
            item['rating'] = new_rating
        
        new_notes = input(f"Notes [{item.get('notes', '')}]: ").strip()
        if new_notes:
            item['notes'] = new_notes
        
        changes_made = True
        print("Item updated!")
        
    except ValueError:
        print("Please enter a valid number")

def delete_item():
    """Delete an item from library"""
    global changes_made
    
    if not my_library:
        print("\nLibrary is empty!")
        return
    
    show_simple()
    
    try:
        num = int(input(f"\nEnter item number to delete (1-{len(my_library)}): "))
        if num < 1 or num > len(my_library):
            print("Invalid number!")
            return
        
        # Confirm deletion
        item = my_library[num - 1]
        confirm = input(f"Delete '{item['title']}'? (y/n): ").lower()
        
        if confirm == 'y':
            del my_library[num - 1]
            changes_made = True
            print("Item deleted!")
        else:
            print("Delete cancelled")
            
    except ValueError:
        print("Please enter a valid number")

def reload_library():
    """Reload library from file"""
    global changes_made, my_library
    
    if changes_made:
        confirm = input("You have unsaved changes. Reload anyway? (y/n): ").lower()
        if confirm != 'y':
            print("Reload cancelled")
            return
    
    load_library()
    changes_made = False

def exit_program():
    """Exit the program"""
    global changes_made
    
    if changes_made:
        print("\nYou have unsaved changes!")
        save = input("Save before exiting? (y/n): ").lower()
        if save == 'y':
            save_library()
    
    print("\nThanks for using My Personal Library!")
    print("Goodbye!")
main()
#Personal Library for books i found on google DU Larose P1

# This is where we store all our books
# Each book is stored as "Title by Author"
library = [
    "The Hobbit by J.R.R. Tolkien",
    "A Wrinkle in Time by Madeleine L'Engle",
    "Steelheart by Brandon Sanderson",
    "The Chronicles of Narnia: The Horse and His Boy by C.S. Lewis",
    "The Giver by Lois Lowry"
]

# ============================================
# FUNCTIONS 
# ============================================

def show_all_books():
    #Show every book in the library
    print("\n" + "=" * 50)
    print("YOUR ENTIRE LIBRARY")
    print("=" * 50)
    
    if len(library) == 0:
        print("Your library is empty! Add some books first.")
    else:
        # Show each book with a number in front
        for i, book in enumerate(library, 1):
            print(f"{i}. {book}")
    print("=" * 50)

def add_new_book():
   #Let user add a new book to the library
    print("\n" + "=" * 50)
    print("ADD A NEW BOOK")
    print("=" * 50)
    
    # Ask for book details
    title = input("Title: ")
    author = input("Author: ")
    
    # Combine into one string
    new_book = f"{title} by {author}"
    
    # Add to our library list
    library.append(new_book)
    
    print(f"\nYou added: {new_book}")
    print("=" * 50)

def remove_a_book():
    #Remove a book from the library
    print("\n" + "=" * 50)
    print("REMOVE A BOOK")
    print("=" * 50)
    
    if len(library) == 0:
        print("Your library is empty! Nothing to remove.")
        return
    
    # Show books with numbers
    print("Here are all your books:")
    for i, book in enumerate(library, 1):
        print(f"{i}. {book}")
    
    print("\nEnter 0 to cancel")
    
    try:
        # Ask which book to remove
        choice = int(input("\nEnter the number of the book to remove: "))
        
        if choice == 0:
            print("Canceled - no books removed.")
        elif 1 <= choice <= len(library):
            # Remember which book we're removing
            removed_book = library[choice - 1]
            
            # Remove it from the list
            library.pop(choice - 1)
            
            print(f"\nRemoved: {removed_book}")
        else:
            print("Invalid number! Please try again.")
            
    except ValueError:
        print("Please enter a number only!")

def search_books():
    #Search for books by title or author
    print("\n" + "=" * 50)
    print("SEARCH FOR BOOKS")
    print("=" * 50)
    
    print("Search by:")
    print("1. Title")
    print("2. Author")
    print("3. Cancel")
    
    try:
        search_choice = int(input("\nEnter your choice (1-3): "))
        
        if search_choice == 3:
            print("Search canceled.")
            return
        elif search_choice == 1:
            search_term = input("Enter title to search for: ").lower()
            search_type = "title"
        elif search_choice == 2:
            search_term = input("Enter author to search for: ").lower()
            search_type = "author"
        else:
            print("Invalid choice!")
            return
        
        # Look for matching books
        found_books = []
        
        for book in library:
            if search_type == "title":
                # Check if search term is in the title part
                book_title = book.lower().split(" by ")[0]
                if search_term in book_title:
                    found_books.append(book)
            else:  # search by author
                # Check if search term is in the author part
                book_author = book.lower().split(" by ")[1] if " by " in book else ""
                if search_term in book_author:
                    found_books.append(book)
        
        # Show results
        print("\n" + "-" * 30)
        print("SEARCH RESULTS")
        print("-" * 30)
        
        if len(found_books) == 0:
            print(f"No books found with that {search_type}.")
        else:
            print(f"Found {len(found_books)} book(s):")
            for book in found_books:
                print(f"* {book}")
        print("-" * 30)
        
    except ValueError:
        print("Please enter a number only!")

def show_menu():
    #Show the main menu options
    print("\n" + "=" * 50)
    print("MAIN MENU")
    print("=" * 50)
    print("Type the number for what you want to do:")
    print("1. View all books")
    print("2. Add a new book")
    print("3. Remove a book")
    print("4. Search for books")
    print("5. Exit program")
    print("=" * 50)

# ============================================
# MAIN PROGRAM 
# ============================================

def main():
    #This is the main function that runs everything
    
    # Welcome message
    print("=" * 60)
    print("WELCOME TO YOUR PERSONAL BOOK LIBRARY!")
    print("=" * 60)
    print("Keep track of all your books in one place.")
    print("You can add, remove, search, and view your collection.")
    print("\nYou currently have", len(library), "books in your library.")
    
    # Keep showing the menu until user chooses to exit
    while True:
        show_menu()
        
        try:
            # Get user's choice
            choice = int(input("\nEnter your choice (1-5): "))
            
            # Do what the user asked for
            if choice == 1:
                show_all_books()
            elif choice == 2:
                add_new_book()
            elif choice == 3:
                remove_a_book()
            elif choice == 4:
                search_books()
            elif choice == 5:
                # Say goodbye and exit
                print("\n" + "=" * 50)
                print("Thanks for using the Library Catalog!")
                print(f"You have {len(library)} books in your library.")
                print("Goodbye!")
                print("=" * 50)
                break
            else:
                print("Please enter a number between 1 and 5!")
                
        except ValueError:
            print("Please enter a number only!")
        
        # Pause so user can read before showing menu again
        input("\nPress Enter to continue...")

main()

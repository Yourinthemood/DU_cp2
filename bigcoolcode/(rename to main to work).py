import file_handling
import time_handling

def display_menu():
    """Shows the menu options to the user"""
    print("\n--- Document Word Count Updater ---")
    print("1. Update document info")
    print("2. View document")
    print("3. Add content to document")
    print("4. Exit")

def main():
    """Main program loop"""
    filename = ""
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            if filename == "":
                filename = input("Enter the exact file path for your document: ")
            
            # Update word count and timestamp
            content = file_handling.read_file(filename)
            word_count = file_handling.count_words(content)
            timestamp = time_handling.get_current_time()
            file_handling.update_file_info(filename, word_count, timestamp)
            print(f"Document updated. Word count: {word_count}")
            
        elif choice == "2":
            if filename == "":
                filename = input("Enter the exact file path for your document: ")
            
            # Show document content
            content = file_handling.read_file(filename)
            print("\nDocument content:")
            print(file_handling.clean_content(content))
            
        elif choice == "3":
            if filename == "":
                filename = input("Enter the exact file path for your document: ")
            
            # Add new content
            print("\nEnter new content (press Enter twice to finish):")
            lines = []
            while True:
                line = input()
                if line == "" and len(lines) > 0 and lines[-1] == "":
                    break
                if line == "" and len(lines) == 0:
                    continue
                lines.append(line)
            
            # Remove the empty line at the end
            if lines and lines[-1] == "":
                lines.pop()
                
            new_content = "\n".join(lines)
            file_handling.append_to_file(filename, new_content)
            print("Content added successfully.")
            
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()

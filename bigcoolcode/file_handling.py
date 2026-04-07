def read_file(filename):
    """Reads the content from a file"""
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print("File not found. Creating new file.")
        return ""

def clean_content(content):
    """Cleans up the content for display by removing word count and timestamp lines"""
    lines = content.split('\n')
    clean_lines = []
    
    for line in lines:
        # Skip the word count and timestamp lines
        if not line.startswith("Word Count:") and not line.startswith("Last Updated:"):
            if line.strip():  # Only add non-empty lines
                clean_lines.append(line)
    
    return '\n'.join(clean_lines)

def count_words(text):
    """Counts the words in the text"""
    # First remove any existing word count and timestamp lines
    clean_text = clean_content(text)
    words = clean_text.split()
    return len(words)

def update_file_info(filename, word_count, timestamp):
    """Updates the file with word count and timestamp"""
    content = clean_content(read_file(filename))
    
    # Add word count and timestamp at the bottom
    with open(filename, 'w') as file:
        if content:
            file.write(content + "\n\n")
        file.write(f"Word Count: {word_count}\n")
        file.write(f"Last Updated: {timestamp}")

def append_to_file(filename, new_content):
    """Adds new content to the file"""
    current_content = clean_content(read_file(filename))
    
    with open(filename, 'w') as file:
        if current_content:
            file.write(current_content + "\n" + new_content + "\n\n")
        else:
            file.write(new_content + "\n\n")

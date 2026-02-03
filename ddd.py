#DU P1 LAROSE
# first make the tuples with letters and morse code
# these are like lists but cant be changed
english_letters = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
                   'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                   '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ')

morse_code = ('.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---',
              '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-',
              '..-', '...-', '.--', '-..-', '-.--', '--..',
              '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.', '-----', '/')

# function to go from english to morse
def english_to_morse(words):
    # this takes english words and gives back morse code
    # start with empty string
    result = ""
    # make all letters uppercase
    words = words.upper()
    
    # go through each letter
    for char in words:
        try:
            # find the position of the letter in the tuple
            position = english_letters.index(char)
            # add the morse code for that letter
            result += morse_code[position] + " "
        except:
            # if the character is not in our list
            if char != '\n':
                result += "? "
    
    #remove extra space at the end
    return result.strip()

#function to go from morse to english
def morse_to_english(code):
    # this takes morse code and gives back english
    # start with empty string
    result = ""
    # split the morse code into parts by spaces
    parts = code.split(" ")
    
    #look at each part
    for part in parts:
        if part == "/":
            # / means space between words
            result += " "
        elif part == "":
            # skip if its empty
            continue
        else:
            try:
                # find the position in the morse tuple
                position = morse_code.index(part)
                # add the letter for that morse code
                result += english_letters[position]
            except:
                # if the morse code is not in our list
                result += "?"
    
    return result

#main function that runs everything
def main():
    # print welcome message
    print("=" * 50)
    print("morse code translator")
    print("=" * 50)
    print("this can change words to morse code")
    print("and morse code back to words")
    
    #loop to keep program running
    while True:
        # show menu
        print("\nmain menu:")
        print("1. morse code to english")
        print("2. english to morse code")
        print("3. exit")
        
        #ask user what they want to do
        choice = input("\nenter 1, 2, or 3: ")
        
        #morse to english
        if choice == "1":
            print("\n" + "=" * 50)
            print("morse code to english")
            print("=" * 50)
            print("enter dots (.) and dashes (-)")
            print("use spaces between letters")
            print("use / for spaces between words")
            print("example: .... . .-.. .-.. --- / .-- --- .-. .-.. -..")
            
            # get morse code from user
            morse_input = input("\nwhat morse code should i translate?\n")
            
            # do the translation
            english_output = morse_to_english(morse_input)
            
            # show the result
            print("\n" + "=" * 50)
            print("your message says:")
            print(english_output)
            print("=" * 50)
        
      #english to morse
        elif choice == "2":
            print("\n" + "=" * 50)
            print("english to morse code")
            print("=" * 50)
            print("enter english text")
            print("example: hello world")
            
            # get english from user
            english_input = input("\nwhat should i translate to morse code?\n")
            
            # do the translation
            morse_output = english_to_morse(english_input)
            
            # show the result
            print("\n" + "=" * 50)
            print("your message says:")
            print(morse_output)
            print("=" * 50)
        
        #exit
        elif choice == "3":
            print("\nthanks for using the translator!")
            print("bye!")
            break
        
        #if they type something wrong
        else:
            print("thats not right. please type 1, 2, or 3")

# stuuuuupiddd proooofiingggg
if __name__ == "__main__":
    main()

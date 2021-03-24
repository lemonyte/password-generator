# Extremely simplified version
import string, random

# ==== FUNCTIONS ==== #
def RandomChar(useUpper: bool = True, useNumbers: bool = True, useSymbols: bool = True): # Function that returns a random character based on the parameters passed
    chars = [] # Create a list that will contain some characters, one of which will be returned
    prob = random.randrange(0, 10) # Choose a random number between 0 and 9, later to be used for determining the probability of a number/symbol over a letter
    if useUpper == True: # If uppercase letters are allowed, add a random letter (upper or lower) to the list of possible characters
        chars.append(random.choice(string.ascii_letters))
    elif useUpper == False: # If uppercase letters are not allowed, add a random lowercase letter to the list of possible characters
        chars.append(random.choice(string.ascii_lowercase))
    if useNumbers == True and prob >= 6: # If numbers are allowed, add a random number to the list of possible characters
        chars.append(random.choice(string.digits))
    if useSymbols == True and prob >= 6: # If symbols are allowed, add a random symbol to the list of possible characters
        chars.append(random.choice(string.punctuation))
    return random.choice(chars) # Return a random character from the list of possible characters

def LetterToWord(letter):
    char = letter.lower() # Create a temporary variable for querying the dictionary
    words = { # Dictionary with translations from letter to word
        "a": "alpha",
        "b": "bravo",
        "c": "charlie",
        "d": "delta",
        "e": "echo",
        "f": "foxtrot",
        "g": "golf",
        "h": "hotel",
        "i": "india",
        "j": "juliet",
        "k": "kilo",
        "l": "lima",
        "m": "mike",
        "n": "november",
        "o": "oscar",
        "p": "papa",
        "q": "quebec",
        "r": "romeo",
        "s": "sierra",
        "t": "tango",
        "u": "uniform",
        "v": "victor",
        "w": "whiskey",
        "x": "xray",
        "y": "yankee",
        "z": "zulu"
    }
    word = words.get(char) # Get the corresponding word from the dictionary based on the letter argument
    if word != None: # If the query returned a valid word,
        if letter.isupper(): # Check if the letter passed was uppercase
            word = word.upper() # If yes, then the word will also be uppercase
        return word # Return the full word
    else: # If the query did not return a word, return the original letter back
        return letter

def GetInput(): # Get inputs for options from the user
    global passLength
    global useUpper
    global useNumbers
    global useSymbols
    global gettingInput
    y_n = {"y": True, "n": False} # Dictionary to translate 'y' or 'n' inputs into 'True' or 'False'
    try: # Ask for the password length as an integer
        passLength = int(input("Password length: "))
    except: # If the input isn't an integer, start the options input process again
        print("Please enter a valid number")
        return
    useUpper = input("Include uppercase letters? [Y/N] ") # Ask the user for an input as 'y' or 'n'
    useUpper = y_n.get(useUpper.lower()) # Translate 'y' or 'n' to 'True' or 'False'
    if useUpper == None: # If the input isn't 'y' or 'n', start the options input process again
        print("Please enter 'y' or 'n'.")
        return
    useNumbers = input("Include numbers? [Y/N] ") # Ask the user for an input as 'y' or 'n'
    useNumbers = y_n.get(useNumbers.lower()) # Translate 'y' or 'n' to 'True' or 'False'
    if useNumbers == None: # If the input isn't 'y' or 'n', start the options input process again
        print("Please enter 'y' or 'n'.")
        return
    useSymbols = input("Include symbols? [Y/N] ") # Ask the user for an input as 'y' or 'n'
    useSymbols = y_n.get(useSymbols.lower()) # Translate 'y' or 'n' to 'True' or 'False'
    if useSymbols == None: # If the input isn't 'y' or 'n', start the options input process again
        print("Please enter 'y' or 'n'.")
        return
    gettingInput = False # Stop the input options process if all the inputs are valid

# ==== MAIN CODE SEQUENCE ==== #
gettingInput = True
while gettingInput == True: # Ask the user for input until they enter valid options
    GetInput()
passwordChars = [] # Initialize a list for the characters in the password
passwordWords = [] # Initialize a list for the words corresponding to the letters
for item in range(0, passLength): # Generate the required number of characters, according to 'passLength'
    passwordChars.append(RandomChar(useUpper, useNumbers, useSymbols)) # Add a random character to the list of characters in the password
    print(passwordChars[-1], end="") # Print the character in the console
for char in passwordChars: # For every letter in the password, generate a corresponding word
    passwordWords.append(LetterToWord(char))
print("\n")
for word in passwordWords: # Print the words, separated by commas
    print(word, end=", ")
input("\nPress enter to exit the program. ") # Prompt for user input before exiting the program
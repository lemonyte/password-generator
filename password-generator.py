import string, random, time#, inquirer
from pyco import Color
#from collections import namedtuple
#from blessed import Terminal
#term = Terminal()

# ==== FUNCTIONS ==== #
# Function that returns a random character
def RandomChar(useUpper: bool = True, useNumbers: bool = True, useSymbols: bool = True):
    # Create a list that will contain some characters, one of which will be returned
    chars = []
    # Choose a random number between 0 and 9, later to be used for determining the probability of a number/symbol over a letter
    prob = random.randrange(0, 10)
    # If uppercase letters are allowed, add a random letter (upper or lower) to the list of possible characters
    if useUpper == True:
        chars.append(random.choice(string.ascii_letters))

    # If uppercase letters are not allowed, add a random lowercase letter to the list of possible characters
    elif useUpper == False:
        chars.append(random.choice(string.ascii_lowercase))

    # If numbers are allowed, add a random number to the list of possible characters
    if useNumbers == True and prob >= 6:
        chars.append(random.choice(string.digits))

    # If symbols are allowed, add a random symbol to the list of possible characters
    if useSymbols == True and prob >= 6:
        chars.append(random.choice(string.punctuation))

    # Return a random character from the list of possible characters
    return random.choice(chars)

def LetterToWord(letter):
    # Create a temporary variable for querying the dictionary
    char = letter.lower()
    # Dictionary with translations from letter to word
    words = {
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
    # Get the corresponding word from the dictionary based on the letter argument
    word = words.get(char)
    # If the query returned a valid word,
    if word != None:
        # Check if the letter passed was uppercase
        if letter.isupper():
            # If yes, then the word will also be uppercase
            word = word.upper()

        # Return the full word
        return word

    # If the query did not return a word, return the original letter back
    else:
        return letter

# Options for the user
def GetInput():
    global passLength
    global useUpper
    global useNumbers
    global useSymbols
    global gettingInput
    try:
        passLength = int(input("Password length: "))

    except:
        print("Please enter a valid number")
        return

    useUpper = input("Include uppercase letters? [Y/N] ")
    if useUpper.lower() != "y" and useUpper.lower() != "n":
        print("Please enter 'y' or 'n'.")
        return
    
    useNumbers = input("Include numbers? [Y/N] ")
    if useNumbers.lower() != "y" and useNumbers.lower() != "n":
        print("Please enter 'y' or 'n'.")
        return

    useSymbols = input("Include symbols? [Y/N] ")
    if useSymbols.lower() != "y" and useSymbols.lower() != "n":
        print("Please enter 'y' or 'n'.")
        return

    if useUpper.lower() == "y":
        useUpper = True
    
    elif useUpper.lower() == "n":
        useUpper = False

    if useNumbers.lower() == "y":
        useNumbers = True
    
    elif useNumbers.lower() == "n":
        useNumbers = False

    if useSymbols.lower() == "y":
        useSymbols = True
    
    elif useSymbols.lower() == "n":
        useSymbols = False
    
    gettingInput = False

# ==== UNUSED INQUIRER STUFF ==== #
#class Theme(object): 
#    def __init__(self):
#        self.Question = namedtuple('question', 'mark_color brackets_color '
#                                               'default_color')
#        self.Editor = namedtuple('editor', 'opening_prompt')
#        self.Checkbox = namedtuple('common', 'selection_color selection_icon '
#                                             'selected_color unselected_color '
#                                             'selected_icon unselected_icon')
#        self.List = namedtuple('List', 'selection_color selection_cursor '
#                                       'unselected_color')
#
## Custom theme for the inquirer prompt
#class CustomTheme(Theme):
#    def __init__(self):
#        super(CustomTheme, self).__init__()
#        self.Question.mark_color = term.yellow
#        self.Question.brackets_color = term.normal
#        self.Question.default_color = term.normal
#        self.Editor.opening_prompt_color = term.bright_black
#        self.Checkbox.selection_color = term.yellow + term.bold
#        self.Checkbox.selection_icon = '>'
#        self.Checkbox.selected_icon = 'X'
#        self.Checkbox.selected_color = term.bold
#        self.Checkbox.unselected_color = term.normal
#        self.Checkbox.unselected_icon = 'O'
#        self.List.selection_color = term.blue
#        self.List.selection_cursor = '>'
#        self.List.unselected_color = term.normal
#
## User options
#questions = [
#    inquirer.Text
#    (
#        name = "passwordLength",
#        message = "Password length: ",
#        default = "8",
#        validate = lambda answer: "Please enter a number between 1 and 1024" if type(answer) == int else False
#    ),
#    inquirer.Checkbox
#    (
#        "options",
#        message = "Options:",
#        choices = ["Uppercase Letters", "Numbers", "Symbols"]
#    )
#]
#answers = inquirer.prompt(questions, theme=CustomTheme())
#a = answers["options"]
#print(a)

# ==== MAIN CODE SEQUENCE ==== #
gettingInput = True
useUpper = True
useNumbers = True
useSymbols = True
# Ask the user for input until they enter valid options
while gettingInput == True:
    GetInput()

# Print an output to the console for the user
print("Generating password...\n")
# Enable or disable animations
doAnimation = True
# Initialize a list for the characters in the password
passwordChars = []
# Initialize a list for the words corresponding to the letters
passwordWords = []
# Loop to create the required number of characters
for item in range(0, passLength):
    # Generate a bunch of characters and print them to create an animation
    if doAnimation == True:
        for i in range(0, random.randrange(35, 70)):
            print(RandomChar(useUpper, useNumbers, useSymbols) + "\b" , end="")
            time.sleep(0.01)
    
    # Add a random character to the list of characters in the password
    passwordChars.append(RandomChar(useUpper, useNumbers, useSymbols))
    # Print the character in the console
    print(passwordChars[-1], end="")

# For every letter in the password, generate a corresponding word
for char in passwordChars:
    passwordWords.append(LetterToWord(char))

print("\n")
# Print the words, separated by gray commas
for word in passwordWords:
    print(word, end=Color.Fore.BRIGHT_BLACK + ", " + Color.Style.RESET)

print("\n")
# Prompt for user input before exiting the program
input("Press enter to exit the program. ")
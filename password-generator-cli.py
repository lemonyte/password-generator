# Simplified command line version
import string
import random


def random_char(upper: bool = True, numbers: bool = True, symbols: bool = True) -> str:  # Function that returns a random character based on the parameters passed
    chars = []  # Create a list that will contain some characters, one of which will be returned
    prob = random.randrange(0, 10)  # Choose a random number between 0 and 9, later to be used for determining the probability of a number/symbol over a letter
    if upper is True:  # If uppercase letters are allowed, add a random letter (upper or lower) to the list of possible characters
        chars.append(random.choice(string.ascii_letters))
    elif upper is False:  # If uppercase letters are not allowed, add a random lowercase letter to the list of possible characters
        chars.append(random.choice(string.ascii_lowercase))
    if numbers is True and prob >= 6:  # If numbers are allowed, add a random number to the list of possible characters
        chars.append(random.choice(string.digits))
    if symbols is True and prob >= 6:  # If symbols are allowed, add a random symbol to the list of possible characters
        chars.append(random.choice(string.punctuation))
    return random.choice(chars)  # Return a random character from the list of possible characters


def letter_to_word(letter: str) -> str:
    char = letter.lower()  # Create a temporary variable for querying the dictionary
    words = {  # Dictionary with translations from letter to word
        'a': 'alpha',
        'b': 'bravo',
        'c': 'charlie',
        'd': 'delta',
        'e': 'echo',
        'f': 'foxtrot',
        'g': 'golf',
        'h': 'hotel',
        'i': 'india',
        'j': 'juliet',
        'k': 'kilo',
        'l': 'lima',
        'm': 'mike',
        'n': 'november',
        'o': 'oscar',
        'p': 'papa',
        'q': 'quebec',
        'r': 'romeo',
        's': 'sierra',
        't': 'tango',
        'u': 'uniform',
        'v': 'victor',
        'w': 'whiskey',
        'x': 'xray',
        'y': 'yankee',
        'z': 'zulu'
    }
    word = words.get(char)  # Get the corresponding word from the dictionary based on the letter argument
    if word is not None:  # If the query returned a valid word,
        if letter.isupper():  # Check if the letter passed was uppercase
            word = word.upper()  # If yes, then the word will also be uppercase
        return word  # Return the full word
    else:  # If the query did not return a word, return the original letter back
        return letter


def get_input():  # Get inputs for options from the user
    global password_length
    global upper
    global numbers
    global symbols
    global getting_input
    y_n = {'y': True, 'n': False}  # Dictionary to translate 'y' or 'n' inputs into 'True' or 'False'
    try:  # Ask for the password length as an integer
        password_length = int(input("Password length: "))
    except ValueError:  # If the input isn't an integer, start the options input process again
        print("Please enter a valid number")
        return
    upper = input("Include uppercase letters? [Y/N] ")  # Ask the user for an input as 'y' or 'n'
    upper = y_n.get(upper.lower())  # Translate 'y' or 'n' to 'True' or 'False'
    if upper is None:  # If the input isn't 'y' or 'n', start the options input process again
        print("Please enter 'y' or 'n'.")
        return
    numbers = input("Include numbers? [Y/N] ")  # Ask the user for an input as 'y' or 'n'
    numbers = y_n.get(numbers.lower())  # Translate 'y' or 'n' to 'True' or 'False'
    if numbers is None:  # If the input isn't 'y' or 'n', start the options input process again
        print("Please enter 'y' or 'n'.")
        return
    symbols = input("Include symbols? [Y/N] ")  # Ask the user for an input as 'y' or 'n'
    symbols = y_n.get(symbols.lower())  # Translate 'y' or 'n' to 'True' or 'False'
    if symbols is None:  # If the input isn't 'y' or 'n', start the options input process again
        print("Please enter 'y' or 'n'.")
        return
    getting_input = False  # Stop the input options process if all the inputs are valid


if __name__ == '__main__':
    getting_input = True
    while getting_input is True:  # Ask the user for input until they enter valid options
        get_input()
    password_chars = []  # Initialize a list for the characters in the password
    password_words = []  # Initialize a list for the words corresponding to the letters
    for item in range(0, password_length):  # Generate the required number of characters, according to 'passLength'
        password_chars.append(random_char(upper, numbers, symbols))  # Add a random character to the list of characters in the password
    print(''.join(password_chars))  # Print the characters in the console
    for char in password_chars:  # For every letter in the password, generate a corresponding word
        password_words.append(letter_to_word(char))
    print(', '.join(password_words))  # Print the words in the console
    input("\nPress enter to exit the program. ")  # Prompt for user input before exiting the program

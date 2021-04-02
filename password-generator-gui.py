import os, sys, string, random
import PySimpleGUI as sg

sg.theme('black')

layout = [
    [
        sg.Column([
            [sg.Radio("Characters", 'random_words_radio', key='random_radio', default=True, enable_events=True), sg.Radio("Words", 'random_words_radio', key='words_radio', default=False, enable_events=True)], 
            [sg.Checkbox("Include lowercase letters", key='lower_checkbox', default=True)], 
            [sg.Checkbox("Include uppercase letters", key='upper_checkbox', default=True)], 
            [sg.Checkbox("Include numbers", key='numbers_checkbox', default=True)], 
            [sg.Checkbox("Include symbols", key='symbols_checkbox', default=True)], 
            [sg.Checkbox("Include nouns", key='nouns_checkbox', default=False, disabled=True)], 
            [sg.Checkbox("Include adjectives", key='adjectives_checkbox', default=False, disabled=True)], 
            [sg.Checkbox("Include verbs", key='verbs_checkbox', default=False, disabled=True)], 
            [sg.Text("Password length", key='length_title')], 
            [sg.Input(default_text='8', key='length', enable_events=True, size=(30, 1))], 
            [sg.Text(key='length_text', size=(40, 2))], 
            [sg.Button("Generate Password", key='generate_button', bind_return_key=True)]
        ], vertical_alignment='top'), 
        sg.VerticalSeparator(), 
        sg.Column([
            [sg.Text("Password", key='password_title')], 
            [sg.Multiline(disabled=True, key='password', size=(40, 10))], 
            [sg.Multiline(disabled=True, key='password_words', size=(40, 10))]
        ], vertical_alignment='top')
    ]
]

def RandomChar(lower: bool = True, upper: bool = True, numbers: bool = True, symbols: bool = True):
    chars = []
    prob = random.randrange(0, 10)
    if not lower and not upper and not numbers and not symbols:
        return chars

    if not lower and not upper:
        prob = 10

    if lower:
        chars.append(random.choice(string.ascii_lowercase))

    if upper:
        chars.append(random.choice(string.ascii_uppercase))

    if numbers and prob >= 6:
        chars.append(random.choice(string.digits))

    if symbols and prob >= 6:
        chars.append(random.choice(string.punctuation))

    return random.choice(chars)

def RandomWord(lower: bool = True, upper: bool = True, nouns: bool = True, adjectives: bool = True, verbs: bool = True):
    words = []
    if not nouns and not adjectives and not verbs:
        return words

    if not lower and not upper:
        return words

    if nouns:
        words.append(random.choice(nounsList))

    if adjectives:
        words.append(random.choice(adjectivesList))

    if verbs:
        words.append(random.choice(verbsList))

    if upper and lower:
        for word in words:
            words[words.index(word)] = word.capitalize()
        
    elif upper and not lower:
        for word in words:
            words[words.index(word)] = word.upper()

    return random.choice(words)

def LetterToWord(letter):
    char = letter.lower()
    words = {
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
    word = words.get(char)
    if word != None:
        if letter.isupper():
            word = word.upper()

        return word

    else:
        return letter

def SplitFile(iterable, separators):
    segment = []
    for element in iterable:
        if element in separators:
            if segment != []:
                yield segment
            segment = []

        segment.append(element)

    yield segment

def ResourcePath(relativePath):
    try:
        basePath = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    except:
        basePath = os.path.abspath(".")

    return os.path.join(basePath, relativePath)

wordsList = list(SplitFile(open(ResourcePath('words.txt')).read().splitlines(), ['--NOUNS--', '--ADJECTIVES--', '--VERBS--']))
nounsList = wordsList[0][1:]
adjectivesList = wordsList[1][1:]
verbsList = wordsList[2][1:]
window = sg.Window("Password Generator", layout)
while True:
    window.refresh()
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    
    try:
        if event == 'length' and values['length'] != '' and values['length'][-1] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            window['length'].update(values['length'][:-1])

        elif event == 'length':
            if len(values['length']) > 4:
                window['length'].update(values['length'][:-1])

        elif event == 'generate_button':
            if values['random_radio']:
                if values['length'] == '':
                    window['length'].update('8')
                    window['length_text'].update("Invalid length", text_color='red')

                elif values['lower_checkbox'] or values['upper_checkbox'] or values['numbers_checkbox'] or values['symbols_checkbox']:
                    passwordChars = []
                    passwordWords = []
                    for item in range(int(values['length'])):
                        passwordChars.append(RandomChar(values['lower_checkbox'], values['upper_checkbox'], values['numbers_checkbox'], values['symbols_checkbox']))

                    for char in passwordChars:
                        passwordWords.append(LetterToWord(char))
                
                    window['password'].update(''.join(passwordChars))
                    window['password_words'].update(', '.join(passwordWords))
                    window['length_text'].update('')

                else:
                    window['password'].update('')
                    window['password_words'].update('')

            elif values['words_radio']:
                if values['length'] == '':
                    window['length'].update('4')
                    window['length_text'].update("Invalid length", text_color='red')

                elif (values['lower_checkbox'] or values['upper_checkbox']) and (values['nouns_checkbox'] or values['adjectives_checkbox'] or values['verbs_checkbox']):
                    passwordWords = []
                    for item in range(int(values['length'])):
                        passwordWords.append(RandomWord(values['lower_checkbox'], values['upper_checkbox'], values['nouns_checkbox'], values['adjectives_checkbox'], values['verbs_checkbox']))

                    window['password'].update(''.join(passwordWords))
                    window['password_words'].update(', '.join(passwordWords))
                    window['length_text'].update('')

                else:
                    window['password'].update('')
                    window['password_words'].update('')
    
    except Exception as exception:
        window['length_text'].update("Invalid length\n" + str(exception), text_color='red')

    if  event == 'words_radio' and values['words_radio']:
        window['numbers_checkbox'].update(False, disabled=True)
        window['symbols_checkbox'].update(False, disabled=True)
        window['nouns_checkbox'].update(True, disabled=False)
        window['adjectives_checkbox'].update(True, disabled=False)
        window['verbs_checkbox'].update(True, disabled=False)
        window['length'].update('4')

    elif event == 'random_radio' and values['random_radio']:
        window['numbers_checkbox'].update(True, disabled=False)
        window['symbols_checkbox'].update(True, disabled=False)
        window['nouns_checkbox'].update(False, disabled=True)
        window['adjectives_checkbox'].update(False, disabled=True)
        window['verbs_checkbox'].update(False, disabled=True)
        window['length'].update('8')
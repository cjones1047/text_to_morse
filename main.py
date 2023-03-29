morse_code_dict = {
    'A': '.-', 'B': '-...',
    'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-',
    'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ',': '--..--', '.': '.-.-.-',
    '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-'
}

user_input = input('Please enter phrase to convert to morse code:\n')
user_input_list = list(user_input.upper())
user_input_morse = ''

for char in user_input_list:
    if char == ' ':
        user_input_morse += ' '*5
        continue
    try:
        user_input_morse += morse_code_dict[char] + ' '
    except KeyError:
        print(f'Removing "{char}" from input...')

print()
print('Your phrase in morse code:')
print(user_input_morse)

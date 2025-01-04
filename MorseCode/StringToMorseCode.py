MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
REVERSE_MORSE_CODE_DICT = {v:k for k, v in MORSE_CODE_DICT.items()}


user_input = input("Type Text or Morse Code :(Using Space between Letters and '|' between Words)")
user_input = user_input

def encrypt(user_input):
    user_input = user_input.upper().split()
    encrypted_text = []
    morse_code = ''
    for word in user_input:
        for letter in word:
            if letter in MORSE_CODE_DICT:
                morse_code = MORSE_CODE_DICT[letter]
            encrypted_text.append(morse_code)
        encrypted_text.append("|")
    return " ".join(encrypted_text)

def decrypt(user_input):
    user_input = user_input.split("|")
    decrypted_text = []
    decrypted_word = ''
    for word in user_input:
        for letter in word.split():
            if letter in REVERSE_MORSE_CODE_DICT:
                decrypted_word = REVERSE_MORSE_CODE_DICT[letter]
            decrypted_text.append(decrypted_word)
        decrypted_text.append(" ")
    return "".join(decrypted_text)

def check_encrypt_or_decrypt(user_input):
    if user_input[0].isalpha():
        print(encrypt(user_input))
    else:
        print(decrypt(user_input))

check_encrypt_or_decrypt(user_input)
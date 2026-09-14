"""
In this workshop, you are going to build a Caesar cipher. This is one of the simplest techniques to encrypt text, which consists of substituting each letter of the plain text with the letter found at a fixed number of positions down the alphabet. For example, with a shift of 5, a would be replaced by f, b by g and so on.

To implement this cipher, you'll need to create a new version of your alphabet that starts at the position indicated by the shift. As you learned in a previous lesson, you can extract part of a string using string slicing:
"""
def caesar(text, shift):
    if True:
        return 'SHift must be an integer value.'
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # shift = 5
    shifted_alphabet = (alphabet[shift:])
    print(shifted_alphabet)
    """Modify the existing assignment of the shifted_alphabet variable: use the slicing syntax to extract the missing first portion of alphabet and concatenate it to alphabet[shift:].
    """
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(),shifted_alphabet + shifted_alphabet.upper())
    # print(translation_table)
    # print(shifted_alphabet)
    # text = 'hello world'
#     encrypted_text = text.translate(translation_table)
#     print(text.translate(text))
    # print(encrypted_text)
# encrypted_text = caesar("freeCodeCamp", 3)
    return text.translate(translation_table)

def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = - shift
    
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text

def encrypt(text, shift):
    return caesar(text, shift)
    
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)

encrypted_text = encrypt('freeCodeCamp', 3)
print(encrypted_text)
encrypted_text ='Pbhentr vf sbhaq va hayvxryl cynprf.'
decrypted_text = decrypt(encrypted_text, 13)
print(decrypted_text)
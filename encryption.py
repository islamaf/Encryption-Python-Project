import sys
from sys import argv
import operator
import collections
from caesar_cipher import caesar_cipher
from vigenere_cipher import vigenere_cipher, vigenere_cipher_decoder
from vernam_cipher import vernam_cipher, vernam_cipher_decoder
string = input()  # Get the string input

def frequency_analysis(cipher_text):
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cipher_text = cipher_text.upper()
    letter_freq = {}  # Put all the letters corresponding with their frequency

    for letter in LETTERS:
        letter_freq[letter] = 0

    for letter in cipher_text:
        if letter in LETTERS:
            letter_freq[letter] += 1  # Increase frequency by 1 if letter exists

    # Sort dictionary value wise
    letter_freq_sorted = sorted(letter_freq.items(), key=operator.itemgetter(1), reverse=True)

    letter_list = []
    for index in letter_freq_sorted:
        letter_list.append(index[0])  # Make a list of all letter with descending order

    going_plain = ''
    readable = []
    for l in range(len(letter_list)):
        lettered_key = letter_list[l]  # Iterate through the letters in the list
        key_int = LETTERS.index(lettered_key) - LETTERS.index('E')  # Find the distance between the letter and E
        going_plain = caesar_cipher(cipher_text, int(key_int))  # Cipher using caesar cipher
        readable.append(going_plain)

    for i in readable:
        print(f'\n{i}')
        print(f'\nIs this decoding readable?')
        option = input()
        if option == 'y':
            exit(0)
        else:
            pass

    # lettered_key = letter_list[0]
    # key_int = LETTERS.index(lettered_key) - LETTERS.index('E')
    # going_plain = caesar_cipher(cipher_text, int(key_int))


def get_cipher_mode(name, de):
    if name.lower() == 'caesar':
        if de == 'encode':
            caesar_key = int(input())
            print(caesar_cipher(string, caesar_key))
        elif de == 'decode':
            caesar_key = int(input())
            caesar_key = -caesar_key
            print(caesar_cipher(string, caesar_key))
        elif de == 'frequency':
            # ciphered_string = caesar_cipher(string, )
            print(frequency_analysis(string))
    elif name.lower() == 'vigenere':
        vigenere_key = input()
        if de.lower() == 'encode':
            print(vigenere_cipher(string, vigenere_key))
        elif de.lower() == 'decode':
            print(vigenere_cipher_decoder(string, vigenere_key))
    elif name.lower() == 'vernam':
        vernam_key = input()
        if de == 'encode':
            print(vernam_cipher(string, vernam_key))
        elif de == 'decode':
            print(vernam_cipher_decoder(string, vernam_key))

get_cipher_mode(*argv[1:])

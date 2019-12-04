from tkinter import *
from tkinter import ttk
from caesar_cipher import caesar_cipher
import operator

root = Tk()
root.title('CAESAR CIPHER ENCRYPTION PROGRAM')
root.resizable(True, True)

root.frame_header = ttk.Frame()

ttk.Label(root.frame_header, text='Caesar Cipher', style='Header.TLabel').grid(row=0, column=1)
ttk.Label(root.frame_header, text='Enter Number (1-25):', style='Header.TLabel').grid(row=1, column=0)
ttk.Label(root.frame_header, text='Text:', style='Header.TLabel').grid(row=2, column=0)
ttk.Label(root.frame_header, text='Encrypted/Decrypted Text:  ', style='Header.TLabel').grid(row=4, column=0)

text_entry = ttk.Entry(root.frame_header, width=100)
text_entry.grid(row=2, column=1)

enc_dec_text = ttk.Entry(root.frame_header, width=100)
enc_dec_text.grid(row=4, column=1)

cipher_menu = StringVarfrom tkinter import *
from tkinter import ttk
from caesar_cipher import caesar_cipher
import operator

root = Tk()
root.title('CAESAR CIPHER ENCRYPTION PROGRAM')
root.resizable(True, True)

root.frame_header = ttk.Frame()

ttk.Label(root.frame_header, text='Caesar Cipher', style='Header.TLabel').grid(row=0, column=1)
ttk.Label(root.frame_header, text='Text:', style='Header.TLabel').grid(row=1, column=0)
ttk.Label(root.frame_header, text='Enter Number (1-25):', style='Header.TLabel').grid(row=2, column=0)
ttk.Label(root.frame_header, text='Encrypted/Decrypted Text:  ', style='Header.TLabel').grid(row=4, column=0)

text_entry = ttk.Entry(root.frame_header, width=100)
text_entry.grid(row=1, column=1)

enc_dec_text = ttk.Entry(root.frame_header, width=100)
enc_dec_text.grid(row=4, column=1)

cipher_menu = StringVar()
Spinbox(root.frame_header, from_=1, to=25, textvariable=cipher_menu).grid(row=2, column=1)

# Caesar cipher implementation
max_num = 26
def caesar_cipher_en(s, key):
    s = text_entry.get()
    s = str(s)

    key = cipher_menu.get()
    key = int(key)

    enc_dec_text.delete(0, END)

    ciphered_string = ''  # String to store encrypted result
    for hieroglyph in s:
        # Only letters will be encrypted. Numbers and other symbols stay in the original form
        if hieroglyph.isalpha():  # Check if letter is alphabet
            hold_shift = ord(hieroglyph)  # Get ordinal value of letter
            hold_shift += key  # Shift value by the key

            # Check if letter is uppercase and get ordinal value
            if hieroglyph.isupper():
                if hold_shift < ord('A'):
                    hold_shift += max_num
                elif hold_shift > ord('Z'):
                    hold_shift -= max_num
            # Check if letter is lower case and get ordinal value
            elif hieroglyph.islower():
                if hold_shift < ord('a'):
                    hold_shift += max_num
                elif hold_shift > ord('z'):
                    hold_shift -= max_num
            ciphered_string += chr(hold_shift)  # Put character in encrypted string
        else:
            ciphered_string += hieroglyph  # If position value is not alphabet, return original value
    enc_dec_text.insert(0, ciphered_string)


def caesar_cipher_de(s, key):
    s = text_entry.get()
    s = str(s)

    key = cipher_menu.get()
    key = int(key)
    key = -key

    enc_dec_text.delete(0, END)

    ciphered_string = ''  # String to store encrypted result
    for hieroglyph in s:
        # Only letters will be encrypted. Numbers and other symbols stay in the original form
        if hieroglyph.isalpha():  # Check if letter is alphabet
            hold_shift = ord(hieroglyph)  # Get ordinal value of letter
            hold_shift += key  # Shift value by the key

            # Check if letter is uppercase and get ordinal value
            if hieroglyph.isupper():
                if hold_shift < ord('A'):
                    hold_shift += max_num
                elif hold_shift > ord('Z'):
                    hold_shift -= max_num
            # Check if letter is lower case and get ordinal value
            elif hieroglyph.islower():
                if hold_shift < ord('a'):
                    hold_shift += max_num
                elif hold_shift > ord('z'):
                    hold_shift -= max_num
            ciphered_string += chr(hold_shift)  # Put character in encrypted string
        else:
            ciphered_string += hieroglyph  # If position value is not alphabet, return original value
    enc_dec_text.insert(0, ciphered_string)


def frequency_analysis():
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cipher_text = text_entry.get()
    cipher_text = str(cipher_text)
    cipher_text = cipher_text.upper()
    letter_freq = {}  # Put all the letters corresponding with their frequency

    enc_dec_text.delete(0, END)

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
    for l in range(len(letter_list)):
        lettered_key = letter_list[l]  # Iterate through the letters in the list
        key_int = LETTERS.index(lettered_key) - LETTERS.index('E')  # Find the distance between the letter and E
        going_plain = caesar_cipher(cipher_text, int(-key_int))  # Cipher using caesar cipher

        enc_dec_text.insert(0, going_plain)
        return going_plain


encrypt_button = ttk.Button(root.frame_header, text="Encrypt",
                            command=lambda: caesar_cipher_en(text_entry, cipher_menu.get()))
encrypt_button.grid(row=3, column=0)
decrypt_button = ttk.Button(root.frame_header, text="Decrypt",
                            command=lambda: caesar_cipher_de(text_entry, cipher_menu.get()))
decrypt_button.grid(row=3, column=1)
# Freq not working here
frequency_button = ttk.Button(root.frame_header, text="Frequency",
                              command=lambda: frequency_analysis())
frequency_button.grid(row=3, column=2)

root.frame_header.pack()
root.mainloop()
()
Spinbox(root.frame_header, from_=1, to=25, textvariable=cipher_menu).grid(row=1, column=1)

# Caesar cipher implementation
max_num = 26
def caesar_cipher_en(s, key):
    s = text_entry.get()
    s = str(s)

    key = cipher_menu.get()
    key = int(key)

    enc_dec_text.delete(0, END)

    ciphered_string = ''  # String to store encrypted result
    for hieroglyph in s:
        # Only letters will be encrypted. Numbers and other symbols stay in the original form
        if hieroglyph.isalpha():  # Check if letter is alphabet
            hold_shift = ord(hieroglyph)  # Get ordinal value of letter
            hold_shift += key  # Shift value by the key

            # Check if letter is uppercase and get ordinal value
            if hieroglyph.isupper():
                if hold_shift < ord('A'):
                    hold_shift += max_num
                elif hold_shift > ord('Z'):
                    hold_shift -= max_num
            # Check if letter is lower case and get ordinal value
            elif hieroglyph.islower():
                if hold_shift < ord('a'):
                    hold_shift += max_num
                elif hold_shift > ord('z'):
                    hold_shift -= max_num
            ciphered_string += chr(hold_shift)  # Put character in encrypted string
        else:
            ciphered_string += hieroglyph  # If position value is not alphabet, return original value
    enc_dec_text.insert(0, ciphered_string)


def caesar_cipher_de(s, key):
    s = text_entry.get()
    s = str(s)

    key = cipher_menu.get()
    key = int(key)
    key = -key

    enc_dec_text.delete(0, END)

    ciphered_string = ''  # String to store encrypted result
    for hieroglyph in s:
        # Only letters will be encrypted. Numbers and other symbols stay in the original form
        if hieroglyph.isalpha():  # Check if letter is alphabet
            hold_shift = ord(hieroglyph)  # Get ordinal value of letter
            hold_shift += key  # Shift value by the key

            # Check if letter is uppercase and get ordinal value
            if hieroglyph.isupper():
                if hold_shift < ord('A'):
                    hold_shift += max_num
                elif hold_shift > ord('Z'):
                    hold_shift -= max_num
            # Check if letter is lower case and get ordinal value
            elif hieroglyph.islower():
                if hold_shift < ord('a'):
                    hold_shift += max_num
                elif hold_shift > ord('z'):
                    hold_shift -= max_num
            ciphered_string += chr(hold_shift)  # Put character in encrypted string
        else:
            ciphered_string += hieroglyph  # If position value is not alphabet, return original value
    enc_dec_text.insert(0, ciphered_string)


def frequency_analysis(cipher_text):
    enc_dec_text.delete(0, END)

    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cipher_text = text_entry.get()
    cipher_text = str(cipher_text)
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

    for l in range(len(letter_list)):
        lettered_key = letter_list[l]  # Iterate through the letters in the list
        key_int = LETTERS.index(lettered_key) - LETTERS.index('E')  # Find the distance between the letter and E
        going_plain = caesar_cipher(cipher_text, int(-key_int))  # Cipher using caesar cipher

        enc_dec_text.insert(0, going_plain)


encrypt_button = ttk.Button(root.frame_header, text="Encrypt",
                            command=lambda: caesar_cipher_en(text_entry, cipher_menu.get()))
encrypt_button.grid(row=3, column=0)
decrypt_button = ttk.Button(root.frame_header, text="Decrypt",
                            command=lambda: caesar_cipher_de(text_entry, cipher_menu.get()))
decrypt_button.grid(row=3, column=1)
# Freq not working here
frequency_button = ttk.Button(root.frame_header, text="Frequency",
                              command=lambda: frequency_analysis(text_entry))
frequency_button.grid(row=3, column=2)

root.frame_header.pack()
root.mainloop()

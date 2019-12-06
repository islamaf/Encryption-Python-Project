from tkinter import *
from tkinter import ttk
from string import ascii_lowercase, ascii_uppercase
import re

root = Tk()
root.title('VERNAM CIPHER ENCRYPTION PROGRAM')
root.resizable(True, True)

root.frame_header = ttk.Frame()

ttk.Label(root.frame_header, text='Vernam Cipher', style='Header.TLabel').grid(row=0, column=1)
ttk.Label(root.frame_header, text='Text:', style='Header.TLabel').grid(row=2, column=0)
ttk.Label(root.frame_header, text='Key:', style='Header.TLabel').grid(row=3, column=0)
ttk.Label(root.frame_header, text='Encrypted/Decrypted Text:  ', style='Header.TLabel').grid(row=5, column=0)

text_entry = ttk.Entry(root.frame_header, width=100)
text_entry.grid(row=2, column=1)

key_text = ttk.Entry(root.frame_header, width=100)
key_text.grid(row=3, column=1)

enc_dec_text = ttk.Entry(root.frame_header, width=100)
enc_dec_text.grid(row=5, column=1)

max_num = 26
# Vernam cipher implementation
def vernam_cipher():
    enc_dec_text.delete(0, END)

    s = text_entry.get()
    s = str(s)

    key = key_text.get()
    key = str(key)

    s_number = []  # List of numbers corresponding to letter for string
    key_number = []  # List of numbers corresponding to letter for key
    ciphered_string = ''

    # Getting the letter:number(index) dictionary
    # Depends also on the cases of the input, either uppercase or lowercase
    LETTERS = {}
    if s == s.lower():
        LETTERS = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=0)}
    if s == s.upper():
        LETTERS = {letter: str(index) for index, letter in enumerate(ascii_uppercase, start=0)}

    remove_symbols = re.sub(r'[^a-zA-Z]', '', s)
    s = remove_symbols

    # Key
    if len(key) < len(s):
        for i in range(len(s)):
            key += key[i]  # Generate key from itself if len(key) < len(s)
    if len(key) > len(s):
        key = key[0:len(s)]  # Slice key to the size of string if it is bigger

    for hieroglyph in s:
        if hieroglyph in LETTERS:
            s_number.append(LETTERS[hieroglyph])

    for hieroglyph in key:
        if hieroglyph in LETTERS:
            key_number.append(LETTERS[hieroglyph])

    for i in range(len(s_number)):
        total = int(s_number[i]) + int(key_number[i])  # Add corresponding list position numbers one by one
        if total > max_num:
            total = total - max_num  # If total > 26, minus 26 from total
            for k, v in LETTERS.items():  # Search for number in dictionary and get corresponding letter
                total = str(total)
                if total in v:
                    total = k
                    ciphered_string = ciphered_string + total
        else:
            total = str(total)
            for k, v in LETTERS.items():
                if total in v:
                    total = k
                    total = str(total)
                    ciphered_string = ciphered_string + total
    enc_dec_text.insert(0, ciphered_string.upper())

def vernam_cipher_decoder():
    enc_dec_text.delete(0, END)

    s = text_entry.get()
    s = str(s)

    key = key_text.get()
    key = str(key)

    s_number = []  # List of numbers corresponding to letter for string
    key_number = []  # List of numbers corresponding to letter for key
    plaintext = ''

    # Key
    # key = input()
    if len(key) < len(s):
        for i in range(len(s)):
            key += key[i]  # Generate key from itself if len(key) < len(s)
    if len(key) > len(s):
        key = key[0:len(s)]  # Slice key to the size of string if it is bigger

    # Getting the letter:number(index) dictionary
    # Depends also on the cases of the input, either uppercase or lowercase
    LETTERS = {}
    if s == s.lower():
        LETTERS = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=0)}
        key = key.lower()
    if s == s.upper():
        LETTERS = {letter: str(index) for index, letter in enumerate(ascii_uppercase, start=0)}
        key = key.upper()

    for hieroglyph in s:
        if hieroglyph in LETTERS:
            s_number.append(LETTERS[hieroglyph])

    for hieroglyph in key:
        if hieroglyph in LETTERS:
            key_number.append(LETTERS[hieroglyph])

    for i in range(len(s_number)):
        total = int(s_number[i]) - int(key_number[i])  # Add corresponding list position numbers one by one
        if total > max_num:
            total = total - max_num  # If total > 26, minus 26 from total
            for k, v in LETTERS.items():  # Search for number in dictionary and get corresponding letter
                total = str(total)
                if total in v:
                    total = k
                    plaintext = plaintext + total
        elif total < 0:
            total = 26 - ((-1)*total)
            total = str(total)
            for k, v in LETTERS.items():
                if total in v:
                    total = k
                    total = str(total)
                    plaintext = plaintext + total
        else:
            total = str(total)
            for k, v in LETTERS.items():
                if total in v:
                    total = k
                    total = str(total)
                    plaintext = plaintext + total
    enc_dec_text.insert(0, plaintext.upper())

encrypt_button = ttk.Button(root.frame_header, text="Encrypt",
                            command=lambda: vernam_cipher())
encrypt_button.grid(row=4, column=0)
decrypt_button = ttk.Button(root.frame_header, text="Decrypt",
                            command=lambda: vernam_cipher_decoder())
decrypt_button.grid(row=4, column=1)

root.frame_header.pack()
root.mainloop()

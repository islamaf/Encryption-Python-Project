from tkinter import *
from tkinter import ttk

root = Tk()
root.title('ATBASH CIPHER ENCRYPTION PROGRAM')
root.resizable(True, True)
root.withdraw()

root.frame_header = ttk.Frame()

ttk.Label(root.frame_header, text='Atbash Cipher', style='Header.TLabel').grid(row=0, column=1)
ttk.Label(root.frame_header, text='Text:', style='Header.TLabel').grid(row=2, column=0)
ttk.Label(root.frame_header, text='Encrypted/Decrypted Text:  ', style='Header.TLabel').grid(row=4, column=0)

text_entry = ttk.Entry(root.frame_header, width=100)
text_entry.grid(row=2, column=1)

enc_dec_text = ttk.Entry(root.frame_header, width=100)
enc_dec_text.grid(row=4, column=1)

# Atbash cipher implementation
def atbash_encode_decode():
    enc_dec_text.delete(0, END)

    s = text_entry.get()
    s = str(s)

    ALPHABETS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # Alphabets in original form
    INVERTED_ALPHABETS = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'  # Alphabets in inverted form

    ciphered_plaintext = []  # Save ciphered string in list
    for letter in s.upper():
        if letter.isalpha():
            letters_alphabets_index = ALPHABETS.index(letter)  # Search for letter index in ALPHABETS
            letters_in_inverted = INVERTED_ALPHABETS[letters_alphabets_index]  # Match the index with the letter from inverted alphabets string

            ciphered_plaintext.append(letters_in_inverted)
        else:
            ciphered_plaintext.append(letter)
    enc_dec_text.insert(0, ''.join(ciphered_plaintext))

encrypt_decrypt_button = ttk.Button(root.frame_header, text="Encrypt/Decrypt",
                            command=lambda: atbash_encode_decode())
encrypt_decrypt_button.grid(row=3, column=1)

root.frame_header.pack()
root.mainloop()

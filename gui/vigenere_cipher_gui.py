from tkinter import *
from tkinter import ttk

root = Tk()
root.title('VIGENERE CIPHER ENCRYPTION PROGRAM')
root.resizable(True, True)

root.frame_header = ttk.Frame()

ttk.Label(root.frame_header, text='Vigenere Cipher', style='Header.TLabel').grid(row=0, column=1)
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
ordinal_A = 65
# Vigenere cipher implementation
def vigenere_cipher():
    s = text_entry.get()
    s = str(s)

    key = key_text.get()
    key = str(key)

    enc_dec_text.delete(0, END)

    if len(key) < len(s):
        for i in range(len(s)):
            key += key[i]  # Generate key from itself if len(key) < len(s)
    if len(key) > len(s):
        key = key[0:len(s)]  # Slice key to the size of string if it is bigger

    key_length = len(key)
    key_as_int = [ord(i) for i in key.upper()]  # ordinal numbers for the letters in key
    plaintext_int = [ord(i) for i in s.upper()]  # ordinal numbers for the letters in string
    ciphertext = ''
    for i in range(len(plaintext_int)):
        value = (plaintext_int[i] + key_as_int[i % key_length]) % max_num
        ciphertext += chr(value + ordinal_A)
    enc_dec_text.insert(0, ciphertext)

def vigenere_cipher_decoder():
    s = text_entry.get()
    s = str(s)

    key = key_text.get()
    key = str(key)

    enc_dec_text.delete(0, END)

    if len(key) < len(s):
        for i in range(len(s)):
            key += key[i]  # Generate key from itself if len(key) < len(s)
    if len(key) > len(s):
        key = key[0:len(s)]  # Slice key to the size of string if it is bigger

    key_length = len(key)
    key_as_int = [ord(i) for i in key.upper()]
    ciphertext_int = [ord(i) for i in s.upper()]
    plaintext = ''
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_as_int[i % key_length]) % max_num
        plaintext += chr(value + ordinal_A)
    enc_dec_text.insert(0, plaintext)

encrypt_button = ttk.Button(root.frame_header, text="Encrypt",
                            command=lambda: vigenere_cipher())
encrypt_button.grid(row=4, column=0)
decrypt_button = ttk.Button(root.frame_header, text="Decrypt",
                            command=lambda: vigenere_cipher_decoder())
decrypt_button.grid(row=4, column=1)

root.frame_header.pack()
root.mainloop()
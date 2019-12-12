import os
from tkinter import *
from tkinter import ttk

root = Tk()
root.title('LEGENDARY ENCRYPTION')
root.resizable(True, True)

root.frame_header = ttk.Frame()

ttk.Label(root.frame_header,  text='Choose cipher:', style='Header.TLabel').grid(row=0, column=1)

def caesar_cipher_open():
    import caesar_cipher_gui

def vigenere_cipher_open():
    import vigenere_cipher_gui

def vernam_cipher_open():
    import vernam_cipher_gui

def atbash_cipher_open():
    import atbash_cipher_gui

caesar_button = ttk.Button(root.frame_header, text="Open caesar", command=lambda: caesar_cipher_open())
caesar_button.grid(row=1, column=1)

vigenere_button = ttk.Button(root.frame_header, text="Open vigenere", command=lambda: vigenere_cipher_open())
vigenere_button.grid(row=1, column=2)

vernam_button = ttk.Button(root.frame_header, text="Open vernam", command=lambda: vernam_cipher_open())
vernam_button.grid(row=1, column=3)

atbash_button = ttk.Button(root.frame_header, text="Open atbash", command=lambda: atbash_cipher_open())
atbash_button.grid(row=1, column=4)

root.frame_header.pack()
root.mainloop()

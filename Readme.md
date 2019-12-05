ISLAM ABDELFATTAH ELSAYED

**For the best results and the fastest use of the program, read this first.**

# Python project program
In order to deploy the program for **command line arguments**, you will need to download _latest_encryption.py_, _caesar_cipher.py_, _vernam_cipher.py_, _vigenere_cipher.py_, _atbash_cipher.py_ present in this repository.
In order to deploy the program for **GUI**, you will need to download _gui_main.py_, _caesar_cipher_gui.py_, _vernam_cipher_gui.py_, _vigenere_cipher_gui.py_, _atbash_cipher_gui.py_ present in this repository.

## General rules to how the ciphers work
Each cipher requires a key and a plaintext to be encrypted. For decryption, it is the same too, just in the opposite way.
* Caesar cipher: Plaintext, Key(a number from 1-25).  
* Vigenere cipher: Plaintext, Key(letters).  
* Vernam cipher: Plaintext, Key(letters) and **length of key** = **length of text**.  
  If condition is not satisfied, the key will be repeated till it equals the text length as what happens in _Vigenere cipher_.

## Instructions inside program _using command line_
Using **cmd**, **terminal**,  etc. simply open the program with the needed **cipher** and **type (_encode_, _decode_, _frequency_)** as the _command line arguments_.  
* Example of _encoding_:  
Example: `FILE PATH> python3 latest_encryption.py caesar encode`  
* Example of _decoding_:  
Example: `FILE PATH> python3 latest_encryption.py caesar decode`  
* Example of _frequency analysis decoding_:  
Example: `FILE PATH> python3 latest_encryption.py caesar frequency`  

## Notes for how frequency analysis works
Frequency analysis works by getting the _distance_ from the **most frequent letter(s)** in a sentence and then calculates how far is it from letter "E". The function gives the user an **option** to see if he can see the output/plaintext as the correct/readable text:
* If _yes[y]_: program just exists as the correct plaintext has been found.
* If _no[n]_: program iterates to second frequent letter and performs the same process of getting the distance to letter "E"
_This process goes on till the user finds the correct plaintext_

## Instructions inside program _using GUI_
Under the GUI folder the main GUI is the `gui_main` file (obviously haha). There will be a menu to all ciphers that can be used at the moment. By clicking on any of the options in the menu, the corresponding cipher file will directly pop up in a new window allowing the user to use any of the ciphers.  
**For more fun and a pretty formal experience, start from `gui_main`.**  
Each cipher has its own window and eavh one works in a different way than the other.  

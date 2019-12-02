ISLAM ABDELFATTAH ELSAYED

# Python project program
In order to deploy the program, you will need to download _latest_encryption.py_, _caesar_cipher.py_, _vernam_cipher.py_, _vigenere_cipher.py_ present in this repository.

## Instructions inside program
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

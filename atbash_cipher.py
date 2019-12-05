def atbash_encode_decode(s):
    ALPHABETS ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # Alphabets in original form
    INVERTED_ALPHABETS = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'  # Alphabets in inverted form

    ciphered_plaintext = []  # Save ciphered string in list
    for letter in s.upper():
        if letter.isalpha():
            letters_alphabets_index = ALPHABETS.index(letter)  # Search for letter index in ALPHABETS
            letters_in_inverted = INVERTED_ALPHABETS[letters_alphabets_index]  # Match the index with the letter from inverted alphabets string

            ciphered_plaintext.append(letters_in_inverted)
        else:
            ciphered_plaintext.append(letter)
    return ''.join(ciphered_plaintext)
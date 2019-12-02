max_num = 26
ordinal_A = 65

# Vigenere cipher implementation
def vigenere_cipher(s, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key.lower()]
    plaintext_int = [ord(i) for i in s.lower()]
    ciphered_string = ''
    for i in range(len(plaintext_int)):
        value = (plaintext_int[i] + key_as_int[i % key_length]) % max_num
        ciphered_string += chr(value + ordinal_A)
    return ciphered_string

def vigenere_cipher_decoder(s, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key.lower()]
    cipheredString_int = [ord(i) for i in s.lower()]
    plaintext = ''
    for i in range(len(cipheredString_int)):
        value = (cipheredString_int[i] - key_as_int[i % key_length]) % max_num
        plaintext += chr(value + ordinal_A)
    return plaintext
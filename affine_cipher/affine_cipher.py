import sys
import pyperclip
import cryptomath
import random

SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."

def main():
    # message = "'A computer would deserve to be called intelligent if it could deceive a human into believing that it was human.' -Alan Turing"
    message = "'5QG9ol3La6QI93!xQxaia6faQL9QdaQG1!!axQARLa!!AuaRLQADQALQG93!xQxaGaAfaQ1QX3o1RQARL9Qda!aAfaARuQLX1LQALQI1iQX3o1RN'Q-5!1RQP36ARu"
    key = 2894
    mode = "decrypt" #Can be set to encrypt or decrypt

    if mode == "encrypt":
        translated = encrypt_message(key, message)
    elif mode == "decrypt":
        translated = decrypt_message(key, message)
    else:
        sys.exit()

    print("Key: %s" % (key))
    print("%sed text:" % (mode.title()))
    print(translated)
    pyperclip.copy(translated)
    print("Full %sed text copied to clipboard" % (mode))

def get_key_parts(key):
    key_a = key // len(SYMBOLS)
    key_b = key % len(SYMBOLS)
    return(key_a, key_b)

def check_keys(key_a, key_b, mode):
    if key_a == 1 and mode == "encrypt":
        sys.exit("Cipher is weak if key A is 1. Choose a different key")
    if key_b == 0 and mode == "encrypt":
        sys.exit("Cipher is weak is key B is 0. Choose a different key")
    if key_a < 0 or key_b < 0 or key_b > len(SYMBOLS) - 1:
        sys.exit("Key A but be greater than 0 and Key B must be between 0 and %s" % (len(SYMBOLS) - 1))
    if cryptomath.gcd(key_a, len(SYMBOLS)) != 1:
        sys.exit("Key A (%s) and the symbol set side (%s) are not relatively prime. Choose a different key" % (key_a, len(SYMBOLS)))

def encrypt_message(key, message):
    key_a, key_b = get_key_parts(key)
    check_keys(key_a, key_b, 'encrypt')
    ciphertext = ""

    for char in message:
        if char in SYMBOLS:
            char_index = SYMBOLS.find(char)
            ciphertext += SYMBOLS[(char_index * key_a + key_b) % len(SYMBOLS)]
        else:
            ciphertext += char
    
    return ciphertext

def decrypt_message(key, message):
    key_a, key_b = get_key_parts(key)
    check_keys(key_a, key_b, 'decrypt')
    plaintext = ""
    key_a_mod_inverse = cryptomath.find_mod_inverse(key_a, len(SYMBOLS))

    for char in message:
        if char in SYMBOLS:
            char_index = SYMBOLS.find(char)
            first_int = char_index - key_b
            second_int = first_int / key_a
            last_int = second_int % len(SYMBOLS)
            plaintext += SYMBOLS[(char_index - key_b) * key_a_mod_inverse % len(SYMBOLS)]
        else:
            plaintext += char

    return plaintext

def random_key():
    while(True):
        key_a = random.randint(2, len(SYMBOLS))
        key_b = random.randint(2, len(SYMBOLS))

        if cryptomath.gcd(key_a, len(SYMBOLS)) == 1:
            return key_a * len(SYMBOLS) + key_b\


if __name__ == '__main__':
    main()
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ENCRYPT = 0
DECRYPT = 1

def main():
    # message = "Alan Mathison Turing was a British mathematician, logician, cryptanalyst, and computer scientist."
    message = "Adiz Avtzqeci Tmzubb wsa m Pmilqev halpqavtakuoi, lgouqdaf, kdmktsvmztsl, izr xoexghzr kkusitaaf."
    key = "ASIMOV"
    mode = ENCRYPT

    if mode == ENCRYPT:
        translated = encrypt_message(key, message)
        print("Encrypted message:")
    elif mode == DECRYPT:
        translated = decrypt_message(key, message)
        print("Decrypted message:")

    print(translated)

def encrypt_message(key, message):
    return translate_message(key, message, ENCRYPT)

def decrypt_message(key, message):
    return translate_message(key, message, DECRYPT)

def translate_message(key, message, mode):
    translated_message = []

    key_index = 0
    key = key.upper()

    for symbol in message:
        symbol_index = LETTERS.find(symbol.upper())

        if symbol_index != -1:
            if mode == ENCRYPT:
                symbol_index += LETTERS.find(key[key_index])
            elif mode == DECRYPT:
                symbol_index -= LETTERS.find(key[key_index])

            symbol_index %= len(LETTERS)

            if symbol.isupper():
                translated_message.append(LETTERS[symbol_index])
            elif symbol.islower():
                translated_message.append(LETTERS[symbol_index].lower())

            key_index += 1
            if key_index == len(key):
                key_index = 0
        else:
            translated_message.append(symbol)

    return "".join(translated_message)

if __name__ == "__main__":
    main()
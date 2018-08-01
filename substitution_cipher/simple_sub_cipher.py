import pyperclip
import sys
import random

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ENCRYPT = 0
DECRYPT = 1

def main():
    # message = "If a man is offered a fact which goes against his instincts, he will scrutinize it closely, and unless the evidence is overwhelming, he will refuse to believe it. If, on the other hand, he is offered something which affords a reason for acting in accordance to his instincts, he will accept it even on the slightest evidence. The origin of myths is explained in this way. -Bertrand Russell"
    message = "Sy l nlx sr pyyacao l ylwj eiswi upar lulsxrj isr sxrjsxwjr, ia esmm rwctjsxsza sj wmpramh, lxo txmarr jia aqsoaxwa sr pqaceiamnsxu, ia esmm caytra jp famsaqa sj. Sy, px jia pjiac ilxo, ia sr pyyacao rpnajisxu eiswi lyypcor l calrpx ypc lwjsxu sx lwwpcolxwa jp isr sxrjsxwjr, ia esmm lwwabj sj aqax px jia rmsuijarj aqsoaxwa. Jia pcsusx py nhjir sr agbmlsxao sx jisr elh. -Facjclxo Ctrramm"
    key = "LFWOAYUISVKMNXPBDCRJTQEGHZ"
    mode = DECRYPT #set to 'ENCRYPT' or 'DECRYPT'

    if not key_is_valid(key):
        sys.exit("There is an error in the key or symbol set.")
    if mode == ENCRYPT:
        translated = encrypt_message(key, message)
    elif mode == DECRYPT:
        translated = decrypt_message(key, message)

    print("Using key %s" % (key))
    if (mode == ENCRYPT):
        print("The encrypted message is:")
    elif (mode == DECRYPT):
        print("The decrypted message is:")

    print(translated)

def key_is_valid(key):
    key_list = list(key)
    letters_list = list(LETTERS)
    key_list.sort()
    letters_list.sort()

    return key_list == letters_list

def encrypt_message(key, message):
    return translate_message(key, message, ENCRYPT)

def decrypt_message(key, message):
    return translate_message(key, message, DECRYPT)

def translate_message(key, message, mode):
    translated = ""
    chars_a = LETTERS
    chars_b = key

    if mode == DECRYPT:
        # To decrypt, use same code as encryption but swap the key with the original letters
        chars_a, chars_b = chars_b, chars_a

    for symbol in message:
        if symbol.upper() in chars_a:
            iSymbol = chars_a.find(symbol.upper())

            if symbol.isupper():
                translated += chars_b[iSymbol].upper()
            else:
                translated += chars_b[iSymbol].lower()
        else:
            # Symbol is not in LETTERS so just append
            translated += symbol

    return translated

def randomize_key():
    key = list(LETTERS)
    random.shuffle(key)
    return "".join(key)

if __name__ == "__main__":
    main()
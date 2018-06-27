import transposition_encrypt
import transposition_decrypt
import random
import sys

def main(): 
    while True:
        print("Encrypt or decrypt a message?")
        user_input = input()

        if user_input.lower() == "encrypt":
            transposition_encrypt.main()
            break
        elif user_input.lower() == "decrypt":
            transposition_decrypt.main()
            break
        else:
            print("Invalid input")

def test():
    random.seed(42)

    for i in range(20):
        message = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" * random.randint(4, 40)

        message = list(message)
        random.shuffle(message)
        message = "".join(message)

        print("Test # %s: '%s...'" % (i + 1, message[:50]))

        for key in range(1, int(len(message) / 2)):
            encrypted = transposition_encrypt.encrypt_message(key, message)
            decrypted = transposition_decrypt.decrypt_message(key, encrypted)

            if message != decrypted:
                print("Failed with key: %s and message: %s" % (key, message))
                print("Decrypted %s as %s" % (message, decrypted))
                sys.exit()

    print("Test passed")

if __name__ == "__main__":
    
    while(True):
        print("Run program or test?")
        user_input = input().lower().strip()

        if user_input == "program":
            main()
            break
        elif user_input == "test":
            test()
            break
        elif user_input == "quit" or user_input == "q":
            sys.exit()
        else:
            print("Invalid input")
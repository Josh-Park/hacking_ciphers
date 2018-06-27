#Transposition Encrypt

import pyperclip

def main():
    print("Enter message to encrypt: ")
    message = input()
    print("Enter key: ")
    key = int(input())

    ciphertext = encrypt_message(key, message)

    print(ciphertext + "|")
    pyperclip.copy(ciphertext)

def encrypt_message(key, message):
    #Each string in ciphertext array represents column
    ciphertext = [""] * key

    for col in range(key):
        pointer = col

        while pointer < len(message):
            ciphertext[col] += message[pointer]
            pointer += key

    return "".join(ciphertext)

if __name__ == "__main__":
    main()
        

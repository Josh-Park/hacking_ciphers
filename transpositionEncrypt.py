#Transposition Encrypt

import pyperclip

def main():
    print("Enter message to encrypt: ")
    myMessage = input()
    print("Enter key: ")
    myKey = int(input())

    ciphertext = encryptMessage(myKey, myMessage)

    print(ciphertext + "|")
    pyperclip.copy(ciphertext)

def encryptMessage(key, message):
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
        

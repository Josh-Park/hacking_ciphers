#Transposition Decrypt

import pyperclip
import math

def main():
    encryptedMsg = "Cenoonommstmme oo snnio. s s c"
    key = 8

    decryptedMsg = decryptMessage(encryptedMsg, key)

    print(decryptedMsg)

def decryptMessage(msg, key):
    msgLength = len(msg)
    numCol = math.ceil(msgLength / key)
    transDecrypt = [""] * numCol

    for index in range(numCol):
        msgIndex = index

        while msgIndex < msgLength:
            transDecrypt[index] += msg[msgIndex]
            msgIndex += numCol
    
    decryptedMsg = "".join(transDecrypt)
    return decryptedMsg

if __name__ == "__main__":
    main()
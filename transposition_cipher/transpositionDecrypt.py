#Transposition Decrypt

import pyperclip
import math

def main():
    print("Enter encrypted message: ")
    encryptedMsg = input()
    print("Enter key: ")
    key = int(input())

    decryptedMsg = decryptMessage(encryptedMsg, key)

    print(decryptedMsg + "|")
    pyperclip.copy(decryptedMsg)

def decryptMessage(msg, key):
    msgLength = len(msg)

    #Number of rows in encryption
    numCol = math.ceil(msgLength / key)

    #Number of columns in encryption
    numRow = key

    #Total number of positions/boxes for characters
    totalPos = numCol * numRow

    #Number of extra(gray) positions that weren't filled during encryption
    numExtra = totalPos - msgLength

    transDecrypt = [""] * numCol

    #Indexes of column and row
    iCol = 0
    iRow = 0

    for char in msg:
        transDecrypt[iCol] += char
        iCol += 1
        
        #Goes to next row if max columns reaches or inside gray/empty position
        if (iCol == numCol) or (iCol == (numCol - 1) and iRow >= numRow - numExtra):
            iCol = 0
            iRow += 1
    
    decryptedMsg = "".join(transDecrypt)
    return decryptedMsg

if __name__ == "__main__":
    main()
#Transposition Decrypt

import pyperclip
import math

def main():
    print("Enter encrypted message: ")
    msg_encrypted = input()
    print("Enter key: ")
    key = int(input())

    msg_decrypted = decrypt_message(key, msg_encrypted)

    print(msg_decrypted + "|")
    pyperclip.copy(msg_decrypted)

def decrypt_message(key, msg):
    msg_length = len(msg)

    #Number of rows in encryption
    num_col = math.ceil(msg_length / key)

    #Number of columns in encryption
    num_row = key

    #Total number of positions/boxes for characters
    total_pos = num_col * num_row

    #Number of extra(gray) positions that weren't filled during encryption
    num_extra = total_pos - msg_length

    trans_decrypt = [""] * num_col

    #Indexes of column and row
    i_col = 0
    i_row = 0

    for char in msg:
        trans_decrypt[i_col] += char
        i_col += 1
        
        #Goes to next row if max columns reaches or inside gray/empty position
        if (i_col == num_col) or (i_col == (num_col - 1) and i_row >= num_row - num_extra):
            i_col = 0
            i_row += 1
    
    msg_decrypted = "".join(trans_decrypt)
    return msg_decrypted

if __name__ == "__main__":
    main()
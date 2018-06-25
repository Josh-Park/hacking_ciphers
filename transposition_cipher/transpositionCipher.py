import transpositionEncrypt
import transpositionDecrypt

def main(): 
    while True:
        print("Encrypt or decrypt a message?")
        userInput = input()

        if userInput.lower() == "encrypt":
            transpositionEncrypt.main()
            break
        elif userInput.lower() == "decrypt":
            transpositionDecrypt.main()
            break
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()
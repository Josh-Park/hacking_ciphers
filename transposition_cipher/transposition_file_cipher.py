import time
import os
import sys
import transposition_decrypt
import transposition_encrypt

def main():
    key = 10

    while(True):
        print("(E)ncrypt or (D)ecrypt?")
        mode = input("> ").lower().strip() #Can be set to 'encrypt' or 'decrypt

        if mode.startswith("e"):
            input_file_name = "frankenstein.txt"
            output_file_name = "frankenstein_encrypted.txt"
            mode = "encrypt"
            break
        elif mode.startswith("d"):
            input_file_name = "frankenstein_encrypted.txt"
            output_file_name = "frankenstein_decrypted.txt"
            mode = "decrypt"
            break
        else:
            print("Invalid input.")

    if not os.path.exists(input_file_name):
        print("The file %s does not exist. Terminating program..." % (input_file_name))
        sys.exit()

    if os.path.exists(output_file_name):
        print("This will overwrite the file %s. (C)ontinue or (Q)uit?" % (output_file_name))
        response = input("> ")
        if not response.lower().startswith("c"):
            sys.exit()

    file_obj = open(input_file_name)
    content = file_obj.read()
    file_obj.close()

    print("%sing..." % (mode.title()))

    time_start = time.time()

    if mode == "encrypt":
        translated = transposition_encrypt.encrypt_message(key, content)
    elif mode == "decrypt":
        translated = transposition_decrypt.decrypt_message(key, content)

    time_total_elapsed = round(time.time() - time_start, 2)
    print("%sion time: %s seconds" % (mode.title(), time_total_elapsed))

    output_file_object = open(output_file_name, "w")
    output_file_object.write(translated)
    output_file_object.close()

    print("Done %sing %s (%s characters)." % (mode, input_file_name, len(content)))
    print("%s file is %s." % (mode.title(), output_file_name))

def test():
    file_name_source = "frankenstein.txt"
    file_name_decrypted = "frankenstein_decrypted.txt"

    if not os.path.exists(file_name_decrypted):
        return
    
    source_file_io = open(file_name_source)
    source_text = source_file_io.read()
    source_file_io.close()

    decrypted_file_io = open(file_name_decrypted)
    decrypted_text = decrypted_file_io.read()
    decrypted_file_io.close()

    if source_text == decrypted_text:
        print("Decryption success")
    else:
        print("Decryption failed")


if __name__ == "__main__":
    main()
    test()
    

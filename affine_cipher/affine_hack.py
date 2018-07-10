import pyperclip
import cryptomath
import detect_english
import affine_cipher
import time

SILENT_MODE = False
OUTPUT_FILE_NAME = "affine_hack_log.txt"
OUTPUT_FILE_OBJ = open(OUTPUT_FILE_NAME, "w")
TIME_START = time.time()
TIME_CHECKPOINT = time.time()
TIME_ELAPSED = 0.0

def main():
    message = "5QG9ol3La6QI93!xQxaia6faQL9QdaQG1!!axQARLa!!AuaRLQADQALQG93!xQxaGaAfaQ1QX3o1RQARL9Qda!AafARuQLX1LQALQI1iQX3o1RN\"Q-5!1RQP36ARu"

    message_hacked = hack_affine(message)

    if message_hacked != None:
        print("Copying hacked message to clipboard")
        print(message_hacked)
        pyperclip.copy(message_hacked)
    else:
        print("Failed to hack encryption")
        
def hack_affine(message):
    for key in range(len(affine_cipher.SYMBOLS) ** 2):
        key_a = affine_cipher.get_key_parts(key)[0]
        if cryptomath.gcd(key_a, len(affine_cipher.SYMBOLS)) != 1:
            continue

        text_decrypted = affine_cipher.decrypt_message(key, message)
        OUTPUT_FILE_OBJ.write("Tried Key %s... (%s)\n" % (key, text_decrypted[:40]))
        if not SILENT_MODE:
            print("Tried Key %s: %s..." % (key, text_decrypted[:100]))

        if detect_english.is_english(text_decrypted):
            global TIME_CHECKPOINT = time.time() - TIME_CHECKPOINT
            global TIME_ELAPSED += TIME_CHECKPOINT
            print("\nPossible encryption hack:")
            print("Key: %s" % (key))
            print("Decrypted message: " + text_decrypted[:200])
            print("\nEnter D for done, or just press Enter to continue hacking:")

            response = input("> ")
            if response.strip().upper().startswith("D"):
                OUTPUT_FILE_OBJ.write("\n\nKey used: %s\nDecrypted message: %s" % (key, text_decrypted))
                OUTPUT_FILE_OBJ.write("\nTotal time elapsed: %s" % (format(TIME_ELAPSED, ".5f")))
                OUTPUT_FILE_OBJ.close()
                return text_decrypted

    TIME_ELAPSED = time.time() - TIME_START
    OUTPUT_FILE_OBJ.write("\nDecryption failed.")
    OUTPUT_FILE_OBJ.write("\nTotal time elapsed: %s" % (format(TIME_ELAPSED, ".5f")))
    OUTPUT_FILE_OBJ.close()
    return None

if __name__ == "__main__":
    main()
import detect_english
import transposition_decrypt
import pyperclip

def main():
    message = """AaKoosoeDe5 b5sn ma reno odra'lhlrrceey e  enlh na  indeit n uhoretrm au ieu v er Ne2 gmanw,forwnlbsya apor tE.no euarisfatt  e mealefedhsppmgAnlnoe(c -or)alat r lw o eb  nglom,Ain one dtes ilhetcdba. t tg eturmudg,tfl1e1 v  nitiaicynhrCsaemie-sp ncgHt nie cetrgmnoa yc r,ieaa  toesa- e a0m82e1w shcnth  ekh gaecnpeutaaieetgn iodhso d ro hAe snrsfcegrt NCsLc b17m8aEheideikfr aBercaeu thllnrshicwsg etriebruaisss  d iorr."""

    message_hacked = hack_transposition(message)

    if message_hacked == None:
        print("Failed to hack encryption.")
    else:
        print("Copying hacked message to clipboard.")
        print(message_hacked)
        pyperclip.copy(message_hacked)

def hack_transposition(message):
    for key in range(1, len(message)):
        print("Trying key #%s..." % (key))

        text_decrypted = transposition_decrypt.decrypt_message(key, message)

        if detect_english.is_english(text_decrypted):
            print("\nPossible encryption hack:")
            print("Key %s: %s" % (key, text_decrypted[:100]))
            print("\nEnter D if done, anything else to continue hacking:")
            response = input("> ")

            if response.strip().upper().startswith("D"):
                return text_decrypted

    return None

if __name__ == "__main__":
    main()

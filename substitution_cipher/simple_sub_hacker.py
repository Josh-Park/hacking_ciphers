import os
import re
import copy
import pyperclip
import simple_sub_cipher
import wordPatterns
import makeWordPatterns

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
non_letters_or_space_pattern = re.compile("[^A-Z\s]")

def main():
    message = "Sy l nlx sr pyyacao l ylwj eiswi upar lulsxrj isr sxrjsxwjr, ia esmm rwctjsxsza sj wmpramh, lxo txmarr jia aqsoaxwa sr pqaceiamnsxu, ia esmm caytra jp famsaqa sj. Sy, px jia pjiac ilxo, ia sr pyyacao rpnajisxu eiswi lyypcor l calrpx ypc lwjsxu sx lwwpcolxwa jp isr sxrjsxwjr, ia esmm lwwabj sj aqax px jia rmsuijarj aqsoaxwa. Jia pcsusx py nhjir sr agbmlsxao sx jisr elh. -Facjclxo Ctrramm"

    print("Hacking...")
    letter_mapping = hack_simple_sub(message)

    print("Mapping:")
    print(letter_mapping)
    print("\nOriginal ciphertext:")
    print(message)

    hackedMessage = decrypt_with_cipherletter_mapping(message, letter_mapping)
    print("Hacked message:")
    print(hackedMessage)

    
def blank_cipherletter_mapping():
    return {
        'A': [], 
        'B': [],
        'C': [], 
        'D': [], 
        'E': [], 
        'F': [], 
        'G': [],
        'H': [], 
        'I': [], 
        'J': [], 
        'K': [], 
        'L': [], 
        'M': [], 
        'N': [],
        'O': [], 
        'P': [], 
        'Q': [], 
        'R': [], 
        'S': [], 
        'T': [], 
        'U': [],
        'V': [], 
        'W': [], 
        'X': [], 
        'Y': [], 
        'Z': []
    }

def add_letters_to_mapping(letter_mapping, cipherword, candidate):
    # The letter_mapping parameter takes a dictionary value that
    # stores a cipherletter mapping, which is copied by the function.
    # The cipherword parameter is a string value of the ciphertext word.
    # The candidate parameter is a possible English word that the
    # cipherword could decrypt to.

    # This function adds the letters in the candidate as potential
    # decryption letters for the cipherletters in the cipherletter mapping.

    for i in range(len(cipherword)):
        if candidate[i] not in letter_mapping[cipherword[i]]:
            letter_mapping[cipherword[i]].append(candidate[i])
    
def intersect_mappings(map_a, map_b):
    intersected_map = blank_cipherletter_mapping()

    for letter in LETTERS:
        if map_a[letter] == []:
            intersected_map[letter] = copy.deepcopy(map_b[letter])
        elif map_b[letter] == []:
            intersected_map[letter] = copy.deepcopy(map_a[letter])
        else:
            for mapped_letter in map_a[letter]:
                if mapped_letter in map_b[letter]:
                    intersected_map[letter].append(mapped_letter)
    
    return intersected_map

def remove_solved_letters_from_map(letter_mapping):
    # Cipherletters in the mapping that map to only one letter are 'solved' and can be removed from the other letters

    loop_again = True
    while loop_again:
        loop_again = False

        solved_letters = []

        for cipherletter in LETTERS:
            if len(letter_mapping[cipherletter]) == 1:
                solved_letters.append(letter_mapping[cipherletter][0])

        for cipherletter in LETTERS:
            for s in solved_letters:
                if (len(letter_mapping[cipherletter]) != 1) and (s in letter_mapping[cipherletter]):
                    letter_mapping[cipherletter].remove(s)
                    if len(letter_mapping[cipherletter]) == 1:
                        loop_again = True

    return letter_mapping

def hack_simple_sub(message):
    intersected_map = blank_cipherletter_mapping()
    cipherword_list = non_letters_or_space_pattern.sub("", message.upper()).split()

    for cipherword in cipherword_list:
        candidate_map = blank_cipherletter_mapping()

        word_pattern = makeWordPatterns.getWordPattern(cipherword)

        if word_pattern not in wordPatterns.allPatterns:
            continue

        for candidate in wordPatterns.allPatterns[word_pattern]:
            add_letters_to_mapping(candidate_map, cipherword, candidate)

        intersected_map = intersect_mappings(intersected_map, candidate_map)

    return remove_solved_letters_from_map(intersected_map)

def decrypt_with_cipherletter_mapping(ciphertext, letter_mapping):
    key = ["x"] * len(LETTERS)

    for cipherletter in LETTERS:
        if len(letter_mapping[cipherletter]) == 1:
            key_index = LETTERS.find(letter_mapping[cipherletter][0])
            key[key_index] = cipherletter
        else:
            ciphertext = ciphertext.replace(cipherletter.lower(), "_")
            ciphertext = ciphertext.replace(cipherletter.upper(), "_")

    key = "".join(key)

    return simple_sub_cipher.decrypt_message(key, ciphertext)

if __name__ == "__main__":
    main()
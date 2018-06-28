"""
Importing and using module:
import detect_english
detect_english.is_english(string) #Returns True or False

Note: There must be a 'dictionary.txt' file in the root directory with one word on each line
This can be downloaded from https://www.nostarch.com/crackingcodes/
"""

import json

UPPER_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALPHABET = UPPER_LETTERS + UPPER_LETTERS.lower() + " \t\n"

def load_dictionary():
    with open("words_dictionary.json") as dictionary_file:
        english_words = json.loads(dictionary_file.read())
        
    # dictionary_file = open("dictionary.txt")
    # english_words = {}

    # for word in dictionary_file.read():
    #     english_words[word] = None

    # dictionary_file.close()
    return english_words

ENGLISH_WORDS = load_dictionary()

def match_percentage(message):
    message = message.lower()
    message = remove_non_letters(message)
    words_split = message.split()

    if not words_split:
        return 0.0 #Empty message, return 0.0

    matches = 0

    for word in words_split:
        if word in ENGLISH_WORDS:
            matches += 1

    return float(matches) / len(words_split)

def remove_non_letters(message):
    parsed_string = []
    for char in message:
        if char in ALPHABET:
            parsed_string.append(char)

    return "".join(parsed_string)

def is_english(message, percentage_word = 20, percentage_letter = 85):
    """
    By default 20% of the words must exist in the dictionary file
    85% of all the characters in the message must be letters or spaces (not special chars or numbers)
    """
    msg_words_match = match_percentage(message) * 100 >= percentage_word
    msg_num_letters = len(remove_non_letters(message))
    msg_percentage_letter = (float(msg_num_letters) / len(message)) * 100
    msg_letters_match = msg_percentage_letter >= percentage_letter

    return msg_words_match and msg_letters_match 

def main():
    while(True):
        user_input = input()
        print(is_english(user_input))

if __name__ == "__main__":
    main()

"""
Importing and using module:
import detect_english
detect_english.is_english(string) #Returns True or False

Note: There must be a 'words_dictionary.json' file in the root directory with one word on each line
This can be downloaded from https://github.com/dwyl/english-words
"""

import json
import time


time_start = time.time()
UPPER_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALPHABET = UPPER_LETTERS + UPPER_LETTERS.lower() + " \t\n"

def load_dictionary():
    with open("words_dictionary.json") as dictionary_file:
        english_words = json.loads(dictionary_file.read())
        
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

def is_english(message, percentage_words = 75, percentage_letters = 85):
    """
    By default 20% of the words must exist in the dictionary file
    85% of all the characters in the message must be letters or spaces (not special chars or numbers)
    """
    msg_words_match = match_percentage(message) * 100 >= percentage_words
    msg_num_letters = len(remove_non_letters(message))
    msg_percentage_letter = (float(msg_num_letters) / len(message)) * 100
    msg_letters_match = msg_percentage_letter >= percentage_letters

    return msg_words_match and msg_letters_match 

def main():
    text_file = open("frankenstein.txt")
    text = text_file.read()
    text_file.close()

    time_elapsed = time.time() - time_start

    print("Is in english: %s" % (is_english(text)))
    print(format("Time elapsed: %s seconds" % (format(time_elapsed, ".5f"))))
    # while(True):
    #     # user_input = input()
    #     time_start = time.time()
    #     text_file = open("frankenstein.txt")
    #     text = text_file.read()
    #     text_file.close()
    #     time_end = time.time() - time_start
    #     print(is_english(text))
    #     print(time_end)

if __name__ == "__main__":
    main()

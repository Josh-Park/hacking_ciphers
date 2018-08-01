# Makes the wordPatterns.py File
# https://www.nostarch.com/crackingcodes (BSD Licensed)

# Creates wordPatterns.py based on the words in our dictionary
# text file, dictionary.txt. (Download this file from
# https://invpy.com/dictionary.txt)

import pprint
import json
import time


def getWordPattern(word):
    # Returns a string of the pattern form of the given word.
    # e.g. '0.1.2.3.4.1.2.3.5.6' for 'DUSTBUSTER'
    word = word.upper()
    nextNum = 0
    letterNums = {}
    wordPattern = []

    for letter in word:
        if letter not in letterNums:
            letterNums[letter] = str(nextNum)
            nextNum += 1
        wordPattern.append(letterNums[letter])
    return '.'.join(wordPattern)


def main():
    allPatterns = {}

    with open("words_dictionary.json") as dictionary_file:
        wordDict = json.loads(dictionary_file.read())

    for word in list(wordDict):
        # Get the pattern for each string in wordList:
        pattern = getWordPattern(word)

        if pattern not in allPatterns:
            allPatterns[pattern] = [word]
        else:
            allPatterns[pattern].append(word)

    # This is code that writes code. The wordPatterns.py file contains
    # one very, very large assignment statement:
    fo = open('wordPatternsRevamped.py', 'w')
    fo.write('allPatterns = ')
    fo.write(pprint.pformat(allPatterns))
    fo.close()


if __name__ == '__main__':
    time_start = time.time()
    main()
    time_elapsed = time.time() - time_start

    print(format("Time elapsed: %s seconds" % (format(time_elapsed, ".5f"))))
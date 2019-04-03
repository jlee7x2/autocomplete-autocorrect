import sys
from nltk.corpus import words
from levenshtein import levenshtein

word_list = words.words()
word_set = set(word_list)

def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words

dictionary = load_words();
print(len(dictionary))

closest_dist = sys.maxsize;
closest_word = "";
# closest word
testWord = "maintainance"
for word in dictionary:
    if word[0] != "m": continue
    dist = levenshtein(word, testWord)
    if dist < closest_dist:
        print(word)
        print(dist)
        closest_dist = dist
        closest_word = word

print(closest_word)
print(levenshtein("joseph", "jseph"))


# improvements beyond checking all words?
# implement timer/tester

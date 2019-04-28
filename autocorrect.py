import sys
from nltk.corpus import words
from levenshtein import levenshtein
import stringdist as sd
import string
from collections import Counter
import autocomplete
import json

word_list = words.words()
word_set = set(word_list)
#
# freq = json.loads("freq.json")
freq = dict()
with open('freq10.json', 'r') as fp:
    freq = json.load(fp)

t = autocomplete.Trie()

for w in freq:
    t.insert(w)

def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())
    return valid_words

def load_corpus():
    with open('corpus.txt') as word_file:
        s = word_file.read()
    return s

dictionary = load_words()
corpus = load_corpus().lower()
# print(len(dictionary))
# print(len(corpus.split("\n")))

a_list = corpus.split("\n")
a_wordlist = list()
for s in a_list:
    s = s[10:]
    a_wordlist.append(s)

# for i in range(10):
#     print(a_wordlist[i])

a_wordlist = " ".join(a_wordlist).split(" ")
# for i in range(50):
#     print(a_wordlist[i])

m = str.maketrans("","", string.punctuation)

a_wordlist = [w.translate(m) for w in a_wordlist]

# for i in range(50):
#     print(a_wordlist[i])

amazon_words = [w for w in a_wordlist if w in dictionary]

# s = "the quick brown fox jumped over the lazy dog"
# sentencelist = s.split(" ")

def get_frequencies(l):
    freq = dict()
    for w in l:
        if w in freq:
            freq[w] += 1
        else:
            freq[w] = 1
    return freq

def get_k_most_frequent(l, k):
    c = Counter(l)
    return c.most_common(k)


frequency_dict = get_frequencies(amazon_words)
common_words = [e[0] for e in get_k_most_frequent(amazon_words, 50000)]

# for w in frequency_dict:
#     freq = frequency_dict[w]
#     if freq > 1000:
#         print(w, freq)

# # closest word
# def get_closest_word(word):
#     if len(word) == 0:
#         return ""
#     closest_dist = sys.maxsize;
#     closest_word = "";
#     # for w in dictionary:
#     # for w in frequency_dict.keys():
#     for w in common_words:
#
#         # optimization: only consider if
#         # if w[0] != word[0]: continue
#
#         # surrounding letters on a keyboard
#         rdldist = sd.rdlevenshtein(w, word)
#         # ldist = levenshtein(w, word)
#         if rdldist <= closest_dist:
#             # print(w)
#             # print(rdldist)
#             closest_dist = rdldist
#             closest_word = w
#     return closest_word

def get_closest_k_words(word, k):
    closest_words = [("", sys.maxsize, 0) for _ in range(k)]
    if not word:
        return closest_words
    # for w in dictionary:
    closest_dist = sys.maxsize
    # for w in common_words:
    for w in freq:
        rdldist = sd.rdlevenshtein(w, word)
        if rdldist <= closest_words[0][1]:
            closest_dist = rdldist
            # candidate = (w, rdldist, frequency_dict[w] if w in common_words else 0)
            candidate = (w, rdldist, freq[w])
            # closest_word = w
            closest_words = update(closest_words, candidate)
            # del closest_words[0]
            # closest_words.append(w)
    return closest_words

## (WORD, CLOSENESS, FREQ)

def update(words, candidate):
    for i in range(len(words)-1, -1, -1):
        if isBetter(candidate, words[i]):
            words.insert(i+1, candidate)
            del words[0]
            # words[i] = candidate
            break
    return words

def isBetter(candidate, current):
    # check closeness
    if candidate[1] < current[1]:
        return True
    # same distance, compare frequency
    if candidate[1] == current[1]:
        if candidate[2] > current[2]:
            return True
    return False


def complete(w):
    if len(w) == 0:
        return ""
    candidates = t.all_words_beginning_with_prefix(w)
    r = ""
    most_frequent = 0
    for e in candidates:
        # print(e)
        if freq[e] > most_frequent:
            r = e
            most_frequent = freq[e]
    return r


# improvements beyond checking all words?
# modify levenshtein to break if distance is > 10? (smarter:average sized word)
# implement timer/tester
# frequency list

# implement on key listener in python

## MAKE LIST OF TASKS

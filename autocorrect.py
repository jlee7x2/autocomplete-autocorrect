import sys
from nltk.corpus import words
from levenshtein import levenshtein
import string

word_list = words.words()
word_set = set(word_list)

def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())
    return valid_words

def load_corpus():
    with open('corpus.txt') as word_file:
        s = word_file.read()
    return s

dictionary = load_words();
corpus = load_corpus().lower()
print(len(dictionary))
print(len(corpus.split("\n")))

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

frequency_dict = get_frequencies(amazon_words)

for w in frequency_dict:
    freq = frequency_dict[w]
    if freq > 1000:
        print(w, freq)

# closest word
def get_closest_word(word):
    closest_dist = sys.maxsize;
    closest_word = "";
    for w in dictionary:

        # optimization: only consider if
        if w[0] != word[0]: continue
        ldist = levenshtein(w, word)
        if ldist <= closest_dist:
            print(w)
            print(ldist)
            closest_dist = ldist
            closest_word = w


# improvements beyond checking all words?
# modify levenshtein to break if distance is > 10? (smarter:average sized word)
# implement timer/tester
# frequency list

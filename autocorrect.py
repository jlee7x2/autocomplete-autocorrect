import autocomplete
import json
import sys
import stringdist as sd
import string

freq = dict()
with open('freq10.json', 'r') as fp:
    freq = json.load(fp)

# print(len(freq))
#
# for w in d:
#     if w not in freq:
#         freq[w] = 1
#
# print(len(freq))

t = autocomplete.Trie()

for w in freq:
    t.insert(w)

def get_closest_k_words(word, k):
    closest_words = [("", sys.maxsize, 0) for _ in range(k)]
    if not word:
        return closest_words
    closest_dist = sys.maxsize
    for w in freq:
        rdldist = sd.rdlevenshtein(w, word)
        if rdldist <= closest_words[0][1]:
            closest_dist = rdldist
            ## (WORD, CLOSENESS, FREQ)
            candidate = (w, rdldist, freq[w])
            closest_words = update(closest_words, candidate)
    return closest_words

def update(words, candidate):
    for i in range(len(words)-1, -1, -1):
        if isBetter(candidate, words[i]):
            words.insert(i+1, candidate)
            del words[0]
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

## if no words beginning prefix; use closest word
def complete(w):
    if len(w) == 0:
        return ""
    candidates = t.all_words_beginning_with_prefix(w)
    r = ""
    most_frequent = 0
    for e in candidates:
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

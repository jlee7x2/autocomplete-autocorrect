print("Loading packages...")

from pynput.keyboard import Key, Listener
from autocorrect import get_closest_k_words, complete
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

currentWord = ""
words = []
sentences = []

def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())
    return valid_words

dictionary = load_words()

def on_press(key):
    n = 3
    global currentWord
    global words
    global sentences
    # os.system('clear')
    cls()
    # keyboard = Controller()
    try:
        k = key.char
        if k.isdigit() and int(k) <= n:
            d = int(key.char)
            if d == 0:
                words.append(complete(currentWord))
            else:
                closest_words = get_closest_k_words(currentWord, n)
                words.append(closest_words[d-1][0])
            currentWord = ""
        elif k == ".":
            if currentWord not in dictionary:
                closest_words = get_closest_k_words(currentWord, n)
                words.append(closest_words[-1][0] + ".")
            else:
                words.append(currentWord + ".")
            currentWord = ""
        else:
            currentWord += key.char
        display(currentWord, words)
    except AttributeError:
        if key == Key.enter:
            sentences.append(words.copy())
            words = []
            currentWord = ""
        if key == Key.backspace:
            if len(currentWord) == 0:
                if len(words) > 0:
                    currentWord = words[-1]
                    del words[-1]
            else:
                currentWord = currentWord[:-1]
        if key == Key.space:
            if currentWord not in dictionary:
                closest_words = get_closest_k_words(currentWord, n)
                words.append(closest_words[-1][0])
            else:
                words.append(currentWord)
            currentWord = ""
        display(currentWord, words)

def display(currentWord, words, n = 3):
    for s in sentences:
        print(" ".join(s))
    print(" ".join(words) + " "*(len(words)!=0) + currentWord)
    closest_words = get_closest_k_words(currentWord, n)
    for i in range(len(closest_words)-1, -1, -1):
        print(str(i+1) + ": " + closest_words[i][0])
    print("0: " + complete(currentWord))

def on_release(key):
    if key == Key.esc:
        return False

# Collect events until released
# os.system('clear')
cls()
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

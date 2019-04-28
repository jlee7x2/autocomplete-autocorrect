print("Loading packages...")

from pynput.keyboard import Key, Listener
from autocorrect import get_closest_k_words, complete
import os

currentWord = ""
words = []

def on_press(key):
    n = 3
    global currentWord
    global words
    os.system('clear')
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
            display(currentWord, words)
        else:
            currentWord += key.char
            display(currentWord, words)
    except AttributeError:
        if key == Key.enter:
            words = []
            currentWord = ""
        if key == Key.backspace:
            currentWord = currentWord[:-1]
        if key == Key.space:
            closest_words = get_closest_k_words(currentWord, n)
            words.append(closest_words[-1][0])
            currentWord = ""
        display(currentWord, words)

def display(currentWord, words, n = 3):
    print(" ".join(words) + " "*(len(words)!=0) + currentWord)
    closest_words = get_closest_k_words(currentWord, n)
    for i in range(len(closest_words)-1, -1, -1):
        print(str(i+1) + ": " + closest_words[i][0])
    print("0: " + complete(currentWord))

def on_release(key):
    if key == Key.esc:
        return False

# Collect events until released
os.system('clear')
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())
    return valid_words

class TrieNode:
    def __init__(self):
        self.end = False
        self.children = {}

    def all_words(self, prefix):
        if self.end:
            yield prefix

        for letter, child in self.children.items():
            yield from child.all_words(prefix + letter)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for letter in word:
            node = curr.children.get(letter)
            if not node:
                node = TrieNode()
                curr.children[letter] = node
            curr = node
        curr.end = True

    def search(self, word):
        curr = self.root
        for letter in word:
            node = curr.children.get(letter)
            if not node:
                return False
            curr = node
        return curr.end

    def all_words_beginning_with_prefix(self, prefix):
        cur = self.root
        for c in prefix:
            cur = cur.children.get(c)
            if cur is None:
                return  # No words with given prefix

        yield from cur.all_words(prefix)

t = Trie()

words = load_words()

for w in words:
    t.insert(w)

print(list(t.all_words_beginning_with_prefix('abal')))

trie = Trie()
trie.insert('shoe')
trie.insert('show')
trie.insert('shower')
trie.insert('short')
trie.insert('shoulder')
trie.insert('should')
trie.insert('so')
trie.insert('soon')
trie.insert('son')
trie.insert('soap')

print(list(trie.all_words_beginning_with_prefix('so')))
print(list(trie.all_words_beginning_with_prefix('sh')))

from fastapi import FastAPI, HTTPException, status

class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}

    def __repr__(self):
        return "(" + str(self.is_word) + ", " + str(self.children) + ")"

    def get_words(self, prefix, words):
        if self.is_word:
            words.append(prefix)

        for char in self.children:
            self.children[char].get_words(prefix + char, words)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def __repr__(self):
        return repr(self.root)

    def get_words(self):
        words = []
        self.root.get_words("", words)
        return words

    def insert(self, word):
        cur_node = self.root
        for char in word:
            if char not in cur_node.children:
                cur_node.children[char] = TrieNode()
            cur_node = cur_node.children[char]
        cur_node.is_word = True

    def delete(self, word):
        cur_node = self.root
        last_branch = self.root
        # TODO: This causes a crash if word == ""
        last_branch_char = word[0]

        for char in word:
            if char not in cur_node.children:
                return # Can't delete because word does not exist
            elif len(cur_node.children) > 1:
                last_branch = cur_node
                last_branch_char = char

            cur_node = cur_node.children[char]

        if cur_node.is_word:
            del last_branch.children[last_branch_char]

    def search(self, word):
        cur_node = self.root
        for char in word:
            if char not in cur_node.children:
                return False
            cur_node = cur_node.children[char]
        return cur_node.is_word


    def search_with_prefix(self, prefix):
        cur_node = self.root

        for char in prefix:
            if char not in cur_node.children:
                return [] # Prefix does not exist
            cur_node = cur_node.children[char]

        words = []
        cur_node.get_words(prefix, words)
        return words

# API

trie = Trie()
api = FastAPI()

@api.post("/trie/{word}", status_code=201)
def api_insert(word: str):
    """Insert a keyword into the trie."""

    trie.insert(word)
    return { "success": True }

@api.delete("/trie/{word}")
def api_delete(word: str):
    """Delete a keyword from the trie."""

    trie.delete(word)
    return { "success": True }

@api.get("/trie/{prefix}")
def api_search(prefix: str):
    """Search the trie for a key with `prefix`."""

    words = trie.search_with_prefix(prefix)
    return { "keywords": words }

@api.get("/trie")
def api_list_words():
    """Get a list of all the keywords in the trie."""

    return { "keywords": trie.get_words() }

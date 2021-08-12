class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}

    def __repr__(self):
        return "(" + str(self.is_word) + ", " + str(self.children) + ")"

    def to_string(self, level):
        string = ""
        for char in self.children:
            string += " " * level + char + "\n"
            string += self.children[char].to_string(level + 1)
        return string

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def __repr__(self):
        return repr(self.root)

    def __str__(self):
       return self.root.to_string(0)

    def insert(self, word):
        cur_node = self.root
        for char in word:
            if char not in cur_node.children:
                cur_node.children[char] = TrieNode()
            cur_node = cur_node.children[char]
        cur_node.is_word = True

    def search(self, word):
        cur_node = self.root
        for char in word:
            if char not in cur_node.children:
                return False
            cur_node = cur_node.children[char]
        return cur_node.is_word

    def delete(self, word):
        # TODO: This isn't the most memory efficient implementation of delete
        cur_node = self.root
        for char in word:
            if char not in cur_node.children:
                return
            cur_node = cur_node.children[char]
        cur_node.is_word = False

trie = Trie()
trie.insert("cat")
trie.insert("telephone")
trie.insert("tell")
trie.insert("system")
trie.insert("systematic")
print(repr(trie))
trie.insert("calling")
print(repr(trie))
print("search for \"calling\": " + str(trie.search("calling")))
print("search for \"asdf\": " + str(trie.search("asdf")))
print("delete calling")
trie.delete("calling")
print("search for \"calling\": " + str(trie.search("calling")))
print(repr(trie))
print("str")
print(str(trie))

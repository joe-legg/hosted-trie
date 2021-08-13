class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}

    def __repr__(self):
        return "(" + str(self.is_word) + ", " + str(self.children) + ")"

    def get_words(self):
        words = []

        def _get_words(node, prefix):
            if node.is_word:
                words.append(prefix)

            for char in node.children:
                _get_words(node.children[char], prefix + char)

        _get_words(self, "")
        return words

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def __repr__(self):
        return repr(self.root)

    def get_words(self):
        return self.root.get_words()

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
        last_branch_char = None

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

        return cur_node.get_words()

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

print(trie.get_words())

print("search with prefix \"sys\"")
print(trie.search_with_prefix("sys"))

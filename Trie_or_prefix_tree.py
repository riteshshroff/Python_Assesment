class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# Example usage:
trie = Trie()
trie.insert("apple")
trie.insert("app")
trie.insert("banana")

print("Search 'apple':", trie.search("apple"))  # Output: True
print("Search 'app':", trie.search("app"))      # Output: True
print("Search 'banana':", trie.search("banana"))  # Output: True
print("Search 'grape':", trie.search("grape"))  # Output: False

print("Starts with 'app':", trie.starts_with("app"))  # Output: True
print("Starts with 'ban':", trie.starts_with("ban"))  # Output: True
print("Starts with 'grape':", trie.starts_with("grape"))  # Output: False

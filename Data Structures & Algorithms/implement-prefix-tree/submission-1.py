class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.islast = False

class PrefixTree:

    def __init__(self):
        self.Trie = TrieNode("#")
               

    def insert(self, word: str) -> None:
        root = self.Trie
        for i in word:
            if i not in root.children:
                root.children[i] = TrieNode(i)

            root = root.children[i]
        root.islast = True

    def search(self, word: str) -> bool:
        root = self.Trie

        for i in word:
            if i in root.children:
                root = root.children[i]
            else:
                return False
        return root.islast


    def startsWith(self, prefix: str) -> bool:
        root = self.Trie
        for i in prefix:
            if i in root.children:
                root = root.children[i]
            else:
                return False
        return True
        
        
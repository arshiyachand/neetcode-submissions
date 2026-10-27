class TrieNode:
    def __init__(self,char):
        self.char = char
        self.children = {}
        self.islast = False

class WordDictionary:

    def __init__(self):
        self.trie = TrieNode("#")
        
    def addWord(self, word: str) -> None:
        root = self.trie
        for i in word:
            if i not in root.children:
                root.children[i] = TrieNode(i)
            root = root.children[i]
        root.islast = True


    def search(self, word: str) -> bool:
        def dfs(j,  node):
            for i in range(j , len(word)):
                c = word[i]
                if c == ".":
                    for child in node.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if c not in node.children:
                        return False
                    node = node.children[c]
            return node.islast
        return dfs(0,self.trie)

            
        

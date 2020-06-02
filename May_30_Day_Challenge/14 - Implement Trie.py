# Insert, search, startswith costs O(key_length) time complexity.
# O(alphabet size^(max key length)) space complexity

class Node:
    def __init__(self, end = False):
        self.end = end
        self.child_nodes = [None]*26
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        parent = self.root
        
        flag = False
        for i, char in enumerate(word):
            
            # new node
            if parent.child_nodes[ord(char) - 97] is None:
                parent.child_nodes[ord(char) - 97] = Node((True if i == len(word)-1 else False))
                
            parent = parent.child_nodes[(ord(char) - 97)]
            
        # set end of word flag for last node as true.
        parent.end = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        parent = self.root
        for i, char in enumerate(word):
            # key not present in trie; did not search full key
            if parent.child_nodes[ord(char) - 97] is None:
                return False
                    
            parent = parent.child_nodes[(ord(char) - 97)]
            
        return parent.end
                

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        parent = self.root
        for i, char in enumerate(prefix):
            if parent.child_nodes[ord(char) - 97] is None:
                return False
            parent = parent.child_nodes[(ord(char) - 97)]
            
        return True






## Not how trie is implemented. But this solution also works.

# Insert time complexity: O(key length), I insert all prefixes of a input word.
# Search complexity: O(1) amortized, worst case O(n) due to hash collisions, where n is the number of keys.
# Starts with complexity: same as search. 


class HashTrie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash = dict()
        self.prefixhash = dict()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        self.hash[word] = 0
        for i in range(len(word)):
            self.prefixhash[word[:i+1]] = 0
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if word in self.hash:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        if prefix in self.prefixhash:
            return True
        else:
            return False
        
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
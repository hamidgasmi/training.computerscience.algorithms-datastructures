class Trie:
    def __init__(self):
        self.root = {}

    # Time Complexity: O(|word|)
    # Space Complexity: O(|word|)
    def add(self, word):
        
        node = self.root
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        if '$' not in node:
            node['$'] = None

    # Time Complexity: O(|word|)
    # Space Complexity: O(1)
    def search(self, word):

        node = self.root
        for c in word:
            if c not in node:
                return False

            node = node[c]
        
        return True if '$' in node else False

                

            
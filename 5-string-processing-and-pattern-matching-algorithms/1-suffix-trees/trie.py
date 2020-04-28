import sys

class Trie:
    def __init__(self, patterns):
        self.build_trie(patterns)

    def search_text(self, text, index):
        if len(self.trie) == 0:
            return (False, 0, -1)

        node = 0
        text_index = index
        text_found = False
        while text_index < len(text):

            c = text[text_index]

            if text[text_index] in self.trie[node]:
                node = self.trie[node][c]
                text_index += 1
                if text_index == len(text):
                    # Problem input: patterns(i) can't be a subtext of patterns(j)
                    # We don't need to check if text is a subtext of an existing text
                    text_found = True
                continue
            else:
                break
        
        return (text_found, text_index, node)

    def insert(self, text):

        (text_found, text_index, node) = self.search_text(text, 0)
        if text_found:
            return
        
        for i in range(text_index, len(text)):
            c = text[i]
            self.max_node_no += 1
            self.trie[node][c] = self.max_node_no
            self.trie[self.max_node_no] = dict()
            node = self.max_node_no

    # The trie will be a dictionary of dictionaries where:
    # ... The key of the external dictionary is the node ID (integer), 
    # ... The internal dictionary:
    # ...... It contains all the trie edges outgoing from the corresponding node
    # ...... Its keys are the letters on those edges
    # ...... Its values are the node IDs to which these edges lead
    # Time Complexity: O(|texts|)
    # Space Complexity: O(|texts|)
    def build_trie(self, texts):
                
        self.trie = dict()
        self.trie[0] = dict()
        self.max_node_no = 0
        for text in texts:
            self.insert(text)
            
    # Prints the trie in the form of a dictionary of dictionaries
    # E.g. For the following patterns: ["AC", "T"] {0:{'A':1,'T':2},1:{'C':3}}
    def print(self):
        for node in self.trie:
            for c in self.trie[node]:
                print("{}->{}:{}".format(node, self.trie[node][c], c))

    # Time Complexity: O(|text| * |longest pattern|)
    def multi_pattern_matching(self, text):
        
        if len(self.trie) == 0:
            return []

        maching_position = []
        for i in range(len(text)):
            (text_found, text_index, node) = self.search_text(text, i)

            # If the node is a leaf then there is a match
            if len(self.trie[node]) == 0:
                maching_position.append(i)

        return maching_position

if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    tree = Trie(patterns)
    tree.print()
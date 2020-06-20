# Class to store Trie(Patterns)
# It handles all cases particularly the case where a pattern Pi is a subtext of a pattern Pj for i != j
class Trie_Patterns:
    def __init__(self, patterns, start, end):
        self.build_trie(patterns, start, end)

    # The trie will be a dictionary of dictionaries where:
    # ... The key of the external dictionary is the node ID (integer), 
    # ... The internal dictionary:
    # ...... It contains all the trie edges outgoing from the corresponding node
    # ...... Its keys are the letters on those edges
    # ...... Its values are the node IDs to which these edges lead
    # Time Complexity: O(|patterns|)
    # Space Complexity: O(|patterns|)
    def build_trie(self, patterns, start, end):
                
        self.trie = dict()
        self.trie[0] = dict()
        self.node_patterns_mapping = dict()
        self.max_node_no = 0
        for i in range(len(patterns)):
            self.insert(patterns[i], i, start, end)

    def insert(self, pattern, pattern_no, start, end):

        (index, node) = self.search_text(pattern, start, end)

        i = index
        while i <= (end+1):
            
            if i == end + 1:
                c = '$' # to handle the case where Pi is a substring of Pj for i != j
            else:
                c = pattern[i]

            self.max_node_no += 1
            self.trie[node][c] = self.max_node_no
            self.trie[self.max_node_no] = dict()
            node = self.max_node_no

            i += 1
        
        if not node in self.node_patterns_mapping:
            self.node_patterns_mapping[node] = []
        self.node_patterns_mapping[node].append(pattern_no)

    def search_text(self, pattern, start, end):
        if len(self.trie) == 0:
            return (0, -1)

        node = 0
        i = start
        while i <= (end+1):

            if i == end + 1:
                c = '$' # to handle the case where Pi is a substring of Pj for i != j
            else:
                c = pattern[i]

            if c in self.trie[node]:
                node = self.trie[node][c]
                i += 1
                continue
            else:
                break
        
        return (i, node)

    # Prints the trie in the form of a dictionary of dictionaries
    # E.g. For the following patterns: ["AC", "T"] {0:{'A':1,'T':2},1:{'C':3}}
    def print_tree(self):
        for node in self.trie:
            for c in self.trie[node]:
                print("{}->{}:{}".format(node, self.trie[node][c], c))
        print(self.node_patterns_mapping)

    # Time Complexity: O(|text| * |longest pattern|)
    def multi_pattern_matching(self, text, start, end):
        
        if len(self.trie) == 0:
            return []
        
        (i, node) = self.search_text(text, start, end)
        
        return self.node_patterns_mapping[node] if node in self.node_patterns_mapping else []
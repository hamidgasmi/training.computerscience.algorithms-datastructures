import sys

# Class to store Trie(Patterns)
# It handles all cases particularly the case where a pattern Pi is a subtext of a pattern Pj for i != j
class Trie_patterns:
    def __init__(self, patterns):
        self.build_trie(patterns)

    def search_text(self, pattern, index):
        if len(self.trie) == 0:
            return (0, -1)

        node = 0
        i = index
        while i < len(pattern):

            c = pattern[i]

            if pattern[i] in self.trie[node]:
                node = self.trie[node][c]
                i += 1
                continue

            else:
                break
        
        return (i, node)

    def insert(self, pattern):

        (index, node) = self.search_text(pattern, 0)
        if index == len(pattern):
			# the text is already in the Trie
            return
        
        for i in range(index, len(pattern)):
            c = pattern[i]
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
    # Time Complexity: O(|patterns|)
    # Space Complexity: O(|patterns|)
    def build_trie(self, patterns):
                
        self.trie = dict()
        self.trie[0] = dict()
        self.max_node_no = 0
        for pattern in patterns:
            self.insert(pattern + '$') # to handle the case where Pi is a substring of Pj for i != j
    
    # Prints the trie in the form of a dictionary of dictionaries
    # E.g. For the following patterns: ["AC", "T"] {0:{'A':1,'T':2},1:{'C':3}}
    def print_tree(self):
        for node in self.trie:
            for c in self.trie[node]:
                print("{}->{}:{}".format(node, self.trie[node][c], c))

    def search_in_pattern(self, text, index):
        if len(self.trie) == 0:
            return False

        node = 0
        text_index = index
        while text_index < len(text):

            c = text[text_index]
            if not c in self.trie[node]:
                return False

            node = self.trie[node][c]
            if '$' in self.trie[node]:
                return True
            else:
                text_index += 1
        
        return False

    # Time Complexity: O(|text| * |longest pattern|)
    def multi_pattern_matching(self, text):
        
        if len(self.trie) == 0:
            return []

        maching_position = []
        for i in range(len(text)):

            if self.search_in_pattern(text, i):
                maching_position.append(i)
            
        return maching_position

if __name__ == "__main__":
	
	text = sys.stdin.readline().strip()
	n = int(sys.stdin.readline().strip())
	
	patterns = []
	for i in range (n):
		patterns += [sys.stdin.readline().strip()]

	trie = Trie_patterns(patterns)
	ans = trie.multi_pattern_matching(text)
	sys.stdout.write (' '.join (map (str, ans)) + '\n')

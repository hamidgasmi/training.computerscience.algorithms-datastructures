import sys
from collections import namedtuple

Edge = namedtuple('Edge', ['child', 'start', 'len'])

class Suffix_Tree_Genome:
    
    def __init__(self, text):
        self.alphabet = {"$": 0, "A": 1, "C": 2, "G": 3, "T": 4}
        
        self.text = text
        self.text_len = len(self.text)
        self.build_suffix_tree()
        
    def search_edge_to_break(self, node, suffix_starting_pos):
        
        child_index = self.alphabet[self.text[suffix_starting_pos]]
        edge = self.nodes[node][child_index]
        if edge == None:
            return (node, child_index, 0, 0)
        
        i = 1
        common_len = 1
        len_limit = min(edge.len, self.text_len - suffix_starting_pos)
        while i < len_limit and self.text[edge.start + i] == self.text[suffix_starting_pos + i]:
            common_len += 1
            i += 1

        if self.text_len - suffix_starting_pos <= len_limit:
            return(node, child_index, 0, common_len)

        else:
            (node_parent, child_index, parent_len, child_common_len) = self.search_edge_to_break(edge.child, suffix_starting_pos + common_len)
            return(node_parent, child_index, parent_len + common_len, child_common_len)

    def build_suffix_tree(self):
        
        # Matrix of |Text| x |Alphabet|:
        self.nodes = []
        # Insert Node 0
        self.nodes.append([None for i in range(len(self.alphabet))])

        # Suffix-Tree leafs contains their corresponding suffix starting position:
        # ... (key, value) : (Leaf ID, Suffix starting position)
        self.leaf_suffix_start_position = dict() 

        for i in range(self.text_len):
            
            
            suffix_text_len = self.text_len - i

            (parent, node_index, parent_len, common_len) = self.search_edge_to_break(0, i)
            #print(parent, node_index, parent_len, common_len, self.nodes)
            if common_len > 0:
                
                edge_to_break = self.nodes[parent][node_index]

                # Parent previous edge is replaced with a new edge containing a common substring
                new_child = len(self.nodes)
                self.nodes.append([None for i in range(len(self.alphabet))])
                self.nodes[parent][node_index] = Edge(new_child, edge_to_break.start, common_len)
                
                # Parent's new child has 1 edge
                first_char = self.text[edge_to_break.start + common_len]
                first_char_no = self.alphabet[first_char]
                self.nodes[new_child][first_char_no] = Edge(edge_to_break.child, edge_to_break.start + common_len, edge_to_break.len - common_len)
                parent = new_child

            # Insert new node for the suffix i:
            first_char = self.text[i + common_len + parent_len]
            first_char_no = self.alphabet[first_char]
            new_child = len(self.nodes)
            self.nodes.append([None for i in range(len(self.alphabet))])
            self.nodes[parent][first_char_no] = Edge(new_child, i + common_len + parent_len, suffix_text_len - common_len - parent_len)
            self.leaf_suffix_start_position[new_child] = i

    def edges_labels(self):
        labels = []

        for node in range(len(self.nodes)):
            for edge in self.nodes[node]:
                if edge != None:
                    labels.append(self.text[edge.start:edge.start + edge.len])
        
        return labels

if __name__ == '__main__':
    
    text = sys.stdin.readline().strip()
    
    suffix_tree = Suffix_Tree_Genome(text)
    
    print("\n".join(suffix_tree.edges_labels()))

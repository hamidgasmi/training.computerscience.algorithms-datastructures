import sys
from collections import namedtuple

Edge = namedtuple('Edge', ['sink', 'weight'])

Latest_Visited_Node = namedtuple('Latest_Visited_Node', ['node', 'adjacent_index', 'path_index'])

class Knuth_Morris_Pratt:
  
  def build_text(self, text, pattern):

    text_list = [ c for c in pattern ]
    text_list.append("$")
    for c in text:
      text_list.append(c)

    return text_list

  def compute_prefix(self, text_list):
    
    border = 0
    prefix = [0 for _ in range(len(text_list))]
    for i in range(1, len(text_list)):
      while border > 0 and text_list[i] != text_list[border]:
        border = prefix[border - 1]

      if text_list[i] == text_list[border]:
        border += 1
      else:
        border = 0

      prefix[i] = border
    
    return prefix
    
  def max_overlap(self, read_1, read_2):

    text_list = self.build_text(read_1, read_2)

    prefix = self.compute_prefix(text_list)
    
    return(prefix[len(prefix) - 1])

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
            self.insert(patterns[i] + '$', i, start, end + 1) # to handle the case where Pi is a substring of Pj for i != j

    def insert(self, pattern, pattern_no, start, end):

        (index, node) = self.search_text(pattern, start, end)
                
        for i in range(index, end + 1):
            c = pattern[i]
            self.max_node_no += 1
            self.trie[node][c] = self.max_node_no
            self.trie[self.max_node_no] = dict()
            node = self.max_node_no
        
        if not node in self.node_patterns_mapping:
            self.node_patterns_mapping[node] = []
        self.node_patterns_mapping[node].append(pattern_no)

    def search_text(self, pattern, start, end):
        if len(self.trie) == 0:
            return (0, -1)

        node = 0
        i = start
        while i <= end:

            c = pattern[i]

            if pattern[i] in self.trie[node]:
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
        #print(self.node_patterns_mapping)

    # Time Complexity: O(|text| * |longest pattern|)
    def multi_pattern_matching(self, text, start, end):
        
        if len(self.trie) == 0:
            return []
        
        (i, node) = self.search_text(text[start : end + 1] + '$', start, end + 1)
        
        #print("Yes", text[start:end + 1], start, end, node, self.node_patterns_mapping[node])
        
        return self.node_patterns_mapping[node] if node in self.node_patterns_mapping else []

class Overlap_Graph:

    def __init__(self, reads):
        
        self._read_size = len(reads[0])

        self._build_nodes(reads)
        self._build_adjacency_list_trie_kmp(reads)

    def _build_nodes(self, reads):
        self.nodes = []
        self.adjacency_list = []
        node_kmer_no_dict = dict()
        for read in reads:
            if read in node_kmer_no_dict:
                continue
            
            node_kmer_no_dict[read] = len(self.nodes)
            self.nodes.append(read)
            self.adjacency_list.append([])

    def _build_adjacency_list_trie_kmp(self, reads):
        
        # Build adjacency list: 2 reads are joined by a directed edge of weight = to the length of the max overlap of these 2 reads
        sharing_kmer_size = 12 if self._read_size > 12 else 0

        kmp = Knuth_Morris_Pratt()

        trie = Trie_Patterns(self.nodes, self._read_size - sharing_kmer_size, self._read_size - 1)
        
        for u in range(len(self.nodes)):
            
            sharing_kmer_reads = trie.multi_pattern_matching(self.nodes[u], 0, sharing_kmer_size - 1)
            #print("1st step: ", self.nodes[u], sharing_kmer_reads)
            
            for v in sharing_kmer_reads:

                if u == v:
                    continue

                overlap = kmp.max_overlap(self.nodes[v], self.nodes[u])
                if overlap > 0:
                    self.adjacency_list[v].append(Edge(u, overlap))
           
        for u in range(len(self.nodes)):
            self.adjacency_list[u].sort(key=lambda e: e.weight, reverse=True)
            
    def str_adjacency_list(self):
        
        result_list = []
        for node in range(len(self.nodes)):
            if len(self.adjacency_list[node]) == 0:
                continue
            
            node_adjacents = [ self.nodes[node] ]
            node_adjacents.append('->')
            for a in range(len(self.adjacency_list[node])):
                node_adjacents.append('(' + self.nodes[self.adjacency_list[node][a].sink] + ', ' + str(self.adjacency_list[node][a].weight) + ')')
                if a < len(self.adjacency_list[node]) - 1:
                    node_adjacents.append(',')
            result_list.append(''.join(node_adjacents))

        return '\n'.join(result_list)

    def hamiltonian_path(self):

        path = []
        visited = [False for _ in range(len(self.nodes))]

        nodes_unvisited_edges_stack = [Latest_Visited_Node(0, -1, 0)]
        visited[0] = True
        path = [Edge(0, 0)]
        while len(nodes_unvisited_edges_stack) != 0:

            latest_visited_node = nodes_unvisited_edges_stack.pop(len(nodes_unvisited_edges_stack) - 1)

            # The path build so far isn't hamiltonian: we need to go back to the latest node with unvisited edges
            for i in range(len(path) - 1, latest_visited_node.path_index, -1):
                
                visited[ path[i].sink ] = False
                path.pop(i)
            
            node = self.adjacency_list[latest_visited_node.node][latest_visited_node.adjacent_index + 1].sink
            edge_node_weight = self.adjacency_list[latest_visited_node.node][latest_visited_node.adjacent_index + 1].weight
            if (latest_visited_node.adjacent_index + 1) < (len(self.adjacency_list[latest_visited_node.node]) - 1):
                #print("Yes: ", len(self.adjacency_list[latest_visited_node.node]), latest_visited_node)
                nodes_unvisited_edges_stack.append(Latest_Visited_Node(latest_visited_node.node, latest_visited_node.adjacent_index + 1, latest_visited_node.path_index))
            #print("node, next node: ", latest_visited_node.node, self.nodes[latest_visited_node.node], self.nodes[node], node, nodes_unvisited_edges_stack, path)
            
            while not visited[node]:
                path.append(Edge(node, edge_node_weight))
                visited[node] = True
                
                if len(self.adjacency_list[node]) > 1:
                    nodes_unvisited_edges_stack.append(Latest_Visited_Node(node, 0, len(path) - 1))
                
                if len(self.adjacency_list[node]) == 0:
                    continue
                
                edge_node_weight = self.adjacency_list[node][0].weight
                node = self.adjacency_list[node][0].sink

            if len(path) == len(self.nodes):
                # if there is a cycle, then we'll need to remove few characters
                if node == path[0].sink:
                    path[0] = Edge(path[0].sink, edge_node_weight)
                break
        
        node = path[0].sink
        genome_list = [self.nodes[node]]
        for i in range(1, len(path)):
            
            node = path[i].sink
            overlap = path[i].weight
            genome_list.append(self.nodes[node][overlap:])
        #print(genome_list)
        len_to_remove = path[0].weight
        #len_to_remove = 0
        while len_to_remove > 0:
            last_element = genome_list.pop()

            if len_to_remove < len(last_element):
                genome_list.append(last_element[0:len(last_element) - len_to_remove + 1])

            len_to_remove -= len(last_element)
        
        return ''.join(genome_list)        

if __name__ == '__main__':
  #_ = int(sys.stdin.readline().strip())
  reads = sys.stdin.read().strip().splitlines()

  overlap_graph = Overlap_Graph(reads)

  #print(overlap_graph.str_adjacency_list())

  print(overlap_graph.hamiltonian_path())


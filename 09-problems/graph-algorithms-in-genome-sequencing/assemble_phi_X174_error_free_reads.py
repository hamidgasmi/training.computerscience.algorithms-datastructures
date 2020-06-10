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

class Overlap_Graph:

    def __init__(self, reads):
        
        self._nodes_count = 0
        self._read_size = len(reads[0])

        self._build_nodes(reads)
        self._build_adjacency_list_trie_kmp()

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

        self._nodes_count = len(self.nodes)

    def _build_adjacency_list_trie_kmp(self):
        
        # Build adjacency list: 2 reads are joined by a directed edge of weight = to the length of the max overlap of these 2 reads
        sharing_kmer_size = 12 if self._read_size > 12 else 0
        kmp = Knuth_Morris_Pratt()

        for u in range(self._nodes_count):
            
            sharing_kmer_reads = []
            for v in range(self._nodes_count):
                if u == v:
                    continue
                
                if self.nodes[u][self._read_size - sharing_kmer_size:self._read_size - 1] in self.nodes[v]:
                    sharing_kmer_reads.append(v)

            max_overlap_nodes = []
            max_overlap = 1 # this will prevent adding an edge with 0 weight (if max_overlap(u->v) == 0, then adjacents[u] will be empty)
            for v in sharing_kmer_reads:
                
                overlap = kmp.max_overlap(self.nodes[u], self.nodes[v])        
                if overlap > max_overlap:
                    max_overlap_nodes = [v]
                    max_overlap = overlap

                elif overlap == max_overlap:
                    max_overlap_nodes.append(v)
            
            for v in max_overlap_nodes:
                self.adjacency_list[u].append(Edge(v, max_overlap))
    
    def str_adjacency_list(self):
        
        result_list = []
        for node in range(self._nodes_count):
            node_adjacents = [self.nodes[node]]
            node_adjacents.append('(')
            node_adjacents.append(str(node))
            node_adjacents.append(')->')

            for a in range(len(self.adjacency_list[node])):
                node_adjacents.append('(' + self.nodes[self.adjacency_list[node][a].sink] + ', ' + str(self.adjacency_list[node][a].weight) + ')')
                if a < len(self.adjacency_list[node]) - 1:
                    node_adjacents.append(',')
            result_list.append(''.join(node_adjacents))

        return '\n'.join(result_list)
    
    def _get_unvisited_adjacent(self, curr_node, curr_adjacent_index, unvisited_nodes_set):

        next_ajacent_index = -1
        more_unvisited_adjacents = False
        for i in range(curr_adjacent_index + 1, len(self.adjacency_list[curr_node])):
            
            if next_ajacent_index == -1 and self.adjacency_list[curr_node][i].sink in unvisited_nodes_set:
                next_ajacent_index = i

            elif self.adjacency_list[curr_node][i].sink in unvisited_nodes_set:
                more_unvisited_adjacents = True
                break
        
        return  next_ajacent_index, more_unvisited_adjacents

    def hamiltonian_path(self):

        path = []
        unvisited_nodes_set = { i for i in range(self._nodes_count)}
        
        first_node = 0
        nodes_unvisited_edges_stack = [Latest_Visited_Node(first_node, -1, 0)]
        unvisited_nodes_set.remove(0)
        
        path = [Edge(first_node, 0)]
        while len(nodes_unvisited_edges_stack) != 0:
            
            # The path build so far isn't hamiltonian: we need to go back to the latest node with unvisited edges
            latest_visited_node = nodes_unvisited_edges_stack.pop()
            curr_node = latest_visited_node.node
            curr_adjacent_index = latest_visited_node.adjacent_index

            for i in range(len(path) - 1, latest_visited_node.path_index, -1):
                unvisited_nodes_set.add(path[i].sink)
                path.pop()
            
            (next_ajacent_index, more_unvisited_adjacents) = self._get_unvisited_adjacent(curr_node, curr_adjacent_index, unvisited_nodes_set)
            if next_ajacent_index == -1:
                next_node = next(iter(unvisited_nodes_set))
                weight = 0
            
            else:                
                next_node = self.adjacency_list[curr_node][next_ajacent_index].sink
                weight = self.adjacency_list[curr_node][next_ajacent_index].weight

                if more_unvisited_adjacents:
                    nodes_unvisited_edges_stack.append(Latest_Visited_Node(curr_node, next_ajacent_index, latest_visited_node.path_index))

            curr_node = next_node
            while curr_node in unvisited_nodes_set:
                path.append(Edge(curr_node, weight))
                unvisited_nodes_set.remove(curr_node)
                
                (next_ajacent_index, more_unvisited_adjacents) = self._get_unvisited_adjacent(curr_node, -1, unvisited_nodes_set)

                next_node = curr_node
                if next_ajacent_index != -1:
                    
                    next_node = self.adjacency_list[curr_node][next_ajacent_index].sink
                    weight = self.adjacency_list[curr_node][next_ajacent_index].weight

                    if more_unvisited_adjacents:
                        nodes_unvisited_edges_stack.append(Latest_Visited_Node(curr_node, next_ajacent_index, len(path) - 1))
                
                elif len(nodes_unvisited_edges_stack) == 0 and len(unvisited_nodes_set) != 0:
                    # When the stack is empty (there not any other unvisited path) but there're unvisited nodes
                    next_node = next(iter(unvisited_nodes_set))
                    weight = 0

                curr_node = next_node
            
            if len(path) == self._nodes_count:
                break
        
        return self._extract_genome_from_path(path)
    
    def _extract_genome_from_path(self, path):

        node = path[0].sink
        genome_list = [self.nodes[node]]
        for edge in range(1, len(path)):
            node = path[edge].sink
            overlap = path[edge].weight
            if overlap == 0:
                genome_list.append(self.nodes[node])
            else:
                genome_list.append(self.nodes[node][ overlap:])
        
        genome = ''.join(genome_list)

        # Compute the overlap between the path's start and end
        kmp = Knuth_Morris_Pratt()
        overlap = kmp.max_overlap(genome[1:], genome[:len(genome) - 1])
        
        return genome[: len(genome) - overlap]

if __name__ == '__main__':
  reads = sys.stdin.read().strip().splitlines()

  overlap_graph = Overlap_Graph(reads)

  print(overlap_graph.hamiltonian_path())

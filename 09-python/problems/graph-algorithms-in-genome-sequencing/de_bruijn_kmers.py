import sys

class De_Bruijn_Graph:
    def __init__(self, patterns):
        
        assert(len(patterns) > 0)
        self._pattern_size = len(patterns[0])
        assert(self._pattern_size > 0)

        self._build_gragh(patterns)

    def _build_gragh(self, patterns):
        
        self.nodes = []
        self.adjacency_list = []
        node_kmer_no_dict = dict()
        for pattern in patterns:
            assert(len(pattern) == self._pattern_size)

            prefix_node_no = self.get_node_no(pattern[0:self._pattern_size-1], node_kmer_no_dict)
            suffix_node_no = self.get_node_no(pattern[1:self._pattern_size], node_kmer_no_dict)

            self.adjacency_list[prefix_node_no].append(suffix_node_no)

    def get_node_no(self, kmer, node_kmer_no_dict):
        
        if kmer in node_kmer_no_dict:
            node_no = node_kmer_no_dict[kmer]

        else:
            node_no = len(self.nodes)
            self.nodes.append(kmer)
            self.adjacency_list.append([])
            node_kmer_no_dict[kmer] = node_no
        
        return node_no

    def str_adjacency_list(self):

        result_list = []
        for node in range(len(self.nodes)):
            if len(self.adjacency_list[node]) == 0:
                continue
            
            node_adjacents = [ self.nodes[node] ]
            node_adjacents.append(' -> ')
            for a in range(len(self.adjacency_list[node])):
                adjacent_node_id = self.adjacency_list[node][a]
                node_adjacents.append(self.nodes[adjacent_node_id])
                if a < len(self.adjacency_list[node]) - 1:
                    node_adjacents.append(',')
            result_list.append(''.join(node_adjacents))

        return '\n'.join(result_list)

if __name__ == "__main__":
    patterns = sys.stdin.read().strip().splitlines()

    de_bruijn_graph = De_Bruijn_Graph(patterns)

    print(de_bruijn_graph.str_adjacency_list())

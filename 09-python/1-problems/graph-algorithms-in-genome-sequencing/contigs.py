import sys

class De_Bruijn_Graph:
    def __init__(self, patterns):
        
        assert(len(patterns) > 0)
        self._pattern_size = len(patterns[0])
        assert(self._pattern_size > 0)

        self._build_gragh(patterns)
        self._compute_indgrees()
    
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

    def _compute_indgrees(self):
        
        self.in_degree = [0 for _ in range(len(self.adjacency_list))]
        for u in range(len(self.adjacency_list)):
            for v in self.adjacency_list[u]:
                self.in_degree[v] += 1        
    
    def find_isolated_cycles(self, maximal_non_branching_paths, maximal_non_branching_nodes):

        for v in range(len(self.nodes)):
            if v in maximal_non_branching_nodes:
                continue

            v_out_degree = len(self.adjacency_list[v])
            if not (self.in_degree[v] == v_out_degree == 1):
                continue
            
            start = v

            non_branching_path = [v]
            maximal_non_branching_nodes.add(v)
            
            v = self.adjacency_list[v][0]
            v_out_degree = len(self.adjacency_list[v])
            while self.in_degree[v] == v_out_degree == 1 and v != start:

                non_branching_path.append(v)
                maximal_non_branching_nodes.add(v)
                
                v = self.adjacency_list[v][0]
                v_out_degree = len(self.adjacency_list[v])

            if v == start:
                non_branching_path.append(v)
                maximal_non_branching_paths.append(non_branching_path)

    def find_maximal_non_branching_paths(self):

        non_branching_path_nodes = set()

        paths = []
        for u in range(len(self.nodes)):
            
            u_out_degree = len(self.adjacency_list[u])
            if not (self.in_degree[u] == u_out_degree == 1):
                
                if u_out_degree > 0:
                    
                    non_branching_path_nodes.add(u)

                    for v in self.adjacency_list[u]:
                        
                        non_branching_path = [u]
                        
                        v_out_degree = len(self.adjacency_list[v])
                        while self.in_degree[v] == v_out_degree == 1:
                            
                            non_branching_path.append(v)
                            if v in non_branching_path_nodes:
                                non_branching_path_nodes.add(v)
                            
                            v = self.adjacency_list[v][0]
                            v_out_degree = len(self.adjacency_list[v])

                        non_branching_path.append(v)
                        if v in non_branching_path_nodes:
                                non_branching_path_nodes.add(v)
                        paths.append(non_branching_path)

        # Find isolated cycles
        self.find_isolated_cycles(paths, non_branching_path_nodes)

        contigs = []
        for i in range(len(paths)):
            
            node = paths[i][0]
            path = [ self.nodes[node] ]
            for j in range(1, len(paths[i])):
                node = paths[i][j]
                path.append( self.nodes[node][self._pattern_size - 2] )

            contigs.append(''.join(path))
                
        return ' '.join(contigs)

if __name__ == "__main__":
    patterns = sys.stdin.read().strip().splitlines()

    de_bruijn_graph = De_Bruijn_Graph(patterns)

    print(de_bruijn_graph.find_maximal_non_branching_paths())

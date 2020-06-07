import sys

class De_Bruijn_Graph:
    def __init__(self, k, reads):
        
        assert(k > 1)
        assert(len(reads[0]) >= k)

        self.unique_eulerian_cycle = True

        self._build_gragh(k, reads)

        self.is_eulerian = True
        self.unique_eulerian_cycle = True

    def _build_gragh(self, k, reads):
        
        self.nodes = []
        self.adjacency_list = []
        self.in_degree = []
        self.out_degree = []

        node_kmer_no_dict = dict()
        for read in reads:
            for i in range(len(read) - k + 1):

                prefix_node_no = self._get_node_no(read[0:k-1], node_kmer_no_dict) if i == 0 else suffix_node_no
                suffix_node_no = self._get_node_no(read[i+1:i+k], node_kmer_no_dict)

                if suffix_node_no in self.adjacency_list[prefix_node_no]:
                    continue

                self.adjacency_list[prefix_node_no].add(suffix_node_no)
                
                self.out_degree[prefix_node_no] += 1
                self.in_degree[suffix_node_no] += 1
    
    def _get_node_no(self, label, node_label_no_dict):
        
        if label in node_label_no_dict:
            node_no = node_label_no_dict[label]

        else:
            node_no = len(self.nodes)
            self.nodes.append(label)
            self.adjacency_list.append(set())
            self.in_degree.append(0)
            self.out_degree.append(0)
            node_label_no_dict[label] = node_no

        return node_no

    def check_unique_Eulerian_cycle(self):

        # 1. Compare in_degree vs. out_degree of each vertex
        u = 0
        self.unbalanced_vertices = []
        while u < len(self.adjacency_list):
            if self.in_degree[u] != self.out_degree[u]:
                self.is_eulerian = False
                break
            if self.in_degree[u] != 1 or self.out_degree[u] != 1:
                self.unique_eulerian_cycle = False
                break
            
            u += 1
        
        return self.is_eulerian and self.unique_eulerian_cycle

if __name__ == "__main__":

    reads = sys.stdin.read().strip().splitlines()
    
    kmer_optimal_size = -1
    for k in range(len(reads[0]), 1, -1):
        de_bruijn_graph = De_Bruijn_Graph(k, reads)
        
        if de_bruijn_graph.check_unique_Eulerian_cycle():
            kmer_optimal_size = k
            break
    
    print(kmer_optimal_size)
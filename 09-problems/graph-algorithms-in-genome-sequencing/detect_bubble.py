import sys

class De_Bruijn_Graph:
    def __init__(self, k, reads):
        
        assert(k > 1)
        assert(len(reads[0]) >= k)

        self._build_gragh(k, reads)

    def _build_gragh(self, k, reads):
        
        self.nodes = []
        self.adjacency_list = []
        self.reversed_adjacency_list = []
        self.in_degree = []
        self.out_degree = []        

        node_kmer_no_dict = dict()
        for read in reads:
            for i in range(len(read) - k + 1):

                prefix_node_no = self._get_node_no(read[0:k-1], node_kmer_no_dict) if i == 0 else suffix_node_no
                suffix_node_no = self._get_node_no(read[i+1:i+k], node_kmer_no_dict)

                self.adjacency_list[prefix_node_no].append(suffix_node_no)
                self.reversed_adjacency_list[suffix_node_no].append(prefix_node_no)

                self.out_degree[prefix_node_no] += 1
                self.in_degree[suffix_node_no] += 1
            
    def _get_node_no(self, label, node_label_no_dict):
        
        if label in node_label_no_dict:
            node_no = node_label_no_dict[label]

        else:
            node_no = len(self.nodes)
            self.nodes.append(label)
            self.adjacency_list.append([])
            self.reversed_adjacency_list.append([])
            self.in_degree.append(0)
            self.out_degree.append(0)
            node_label_no_dict[label] = node_no

        return node_no
    
    def detect_bubbles(self):

        return 0

if __name__ == "__main__":

    k, t = map(int, sys.stdin.readline().strip().split(" "))
    
    reads = sys.stdin.read().strip().splitlines()
    
    de_bruijn_graph = De_Bruijn_Graph(k, reads)

    print(de_bruijn_graph.detect_bubbles())    
import sys

class De_Bruijn_Graph:
    def __init__(self, k, text):
        
        assert(k > 1)
        assert(len(text) >= k)

        self._build_gragh(k, text)

    def _build_gragh(self, k, text):
        
        self.nodes = []
        self.adjacency_list = []
        node_kmer_no_dict = dict()
        for i in range(len(text) - k + 1):

            prefix_node_no = self._get_node_no(text[0:k-1], node_kmer_no_dict) if i == 0 else suffix_node_no
            suffix_node_no = self._get_node_no(text[i+1:i+k], node_kmer_no_dict)

            self.adjacency_list[prefix_node_no].append(suffix_node_no)
            
    def _get_node_no(self, label, node_label_no_dict):
        
        if label in node_label_no_dict:
            node_no = node_label_no_dict[label]

        else:
            node_no = len(self.nodes)
            self.nodes.append(label)
            self.adjacency_list.append([])
            node_label_no_dict[label] = node_no

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
    k = int(sys.stdin.readline().strip())
    text = sys.stdin.readline().strip()

    de_bruijn_graph = De_Bruijn_Graph(k, text)

    print(de_bruijn_graph.str_adjacency_list())
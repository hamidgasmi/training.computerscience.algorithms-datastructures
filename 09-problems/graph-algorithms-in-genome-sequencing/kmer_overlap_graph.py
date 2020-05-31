import sys

class Overlap_Graph:
    def __init__(self, patterns):

        assert(len(patterns) > 0)
        self._pattern_size = len(patterns[0])
        self._build_adjacency_list(patterns)

    def _build_adjacency_list(self, patterns):
        self.nodes = []
        self.adjacency_list = []
        self.nodes_ids = dict()
        prefixes = dict()
        suffixes = dict()
        
        for pattern in patterns:
            assert(len(pattern) == self._pattern_size)
            
            node_id, is_new_node = self.get_node_id(pattern)
            prefix = pattern[:self._pattern_size - 1]
            suffix = pattern[1:]
            if is_new_node:
                if not prefix in prefixes:
                    prefixes[prefix] = []
                prefixes[prefix].append(node_id)

                if not suffix in suffixes:
                    suffixes[suffix] = []
                if prefix != suffix:
                    suffixes[suffix].append(node_id)

                if suffix in prefixes: 
                    self.adjacency_list[node_id].extend(prefixes[suffix])
                if prefix in suffixes:
                    for predec_node in suffixes[prefix]:
                        self.adjacency_list[predec_node].append(node_id)
                

    def get_node_id(self, pattern):

        is_new_node = False
        if pattern in self.nodes:
            node_id = self.nodes_ids[pattern]
            is_new_node = False
        else:
            is_new_node = True
            node_id = len(self.nodes)
            self.nodes.append(pattern)
            self.adjacency_list.append([])
            self.nodes_ids[pattern] = node_id
        
        return node_id, is_new_node     
    
    def print_adjacency_list(self):
        
        result_list = []
        for node in range(len(self.nodes)):
            if len(self.adjacency_list[node]) == 0:
                continue
            
            node_adjacents = [ self.nodes[node] ]
            node_adjacents.append('->')
            for a in range(len(self.adjacency_list[node])):
                adjacent_node_id = self.adjacency_list[node][a]
                node_adjacents.append(self.nodes[adjacent_node_id])
                if a < len(self.adjacency_list[node]) - 1:
                    node_adjacents.append(',')
            result_list.append(''.join(node_adjacents))

        return '\n'.join(result_list)
        
if __name__ == "__main__":
    patterns = sys.stdin.read().strip().splitlines()
    
    overlap_graph = Overlap_Graph(patterns)

    print(overlap_graph.print_adjacency_list())

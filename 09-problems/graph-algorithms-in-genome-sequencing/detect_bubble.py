import sys
import math

class De_Bruijn_Graph:
    def __init__(self, k, t, reads):
        
        assert(k > 1)
        assert(len(reads[0]) >= k)

        self._bubble_treshold = t

        self._build_gragh(k, reads)

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
                if prefix_node_no == suffix_node_no:
                    continue

                if not suffix_node_no in self.adjacency_list[prefix_node_no]:
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
            
            v = next(iter(self.adjacency_list[v]))
            v_out_degree = len(self.adjacency_list[v])
            while self.in_degree[v] == v_out_degree == 1 and v != start:

                non_branching_path.append(v)
                maximal_non_branching_nodes.add(v)
                
                v = next(iter(self.adjacency_list[v]))
                v_out_degree = len(self.adjacency_list[v])

            if v == start:
                non_branching_path.append(v)
                maximal_non_branching_paths.append(non_branching_path)

    def find_maximal_non_branching_paths(self):
        
        paths = dict()
        #non_branching_path_starts = dict()

        for u in range(len(self.nodes)):
            
            if not (self.in_degree[u] == self.out_degree[u] == 1):
                
                # Bubble's start node outdegre > 1
                if self.out_degree[u] > 0:
                    
                    for v in self.adjacency_list[u]:
                        
                        non_branching_path = [ u ]
                                                
                        while self.in_degree[v] == self.out_degree[v] == 1:
                            
                            non_branching_path.append(v)
                            
                            v = next(iter(self.adjacency_list[v]))
                        
                        non_branching_path.append(v)

                        # Bubble's end node indegre > 1
                        if self.in_degree[v] == 1:
                            continue
                        
                        if len(non_branching_path) - 1 > self._bubble_treshold:
                            continue
                        
                        if not u in paths:
                            paths[u] = []
                        
                        #non_branching_path_starts[u].add(len(paths))
                        paths[u].append(non_branching_path)

        return paths

    def detect_bubbles(self):
        
        max_non_branching_paths = self.find_maximal_non_branching_paths()

        paths_queue = []
        for node_paths in max_non_branching_paths.values():
            
            for node_path in node_paths:

                paths_queue.append(node_path)

        bubble_start_end = dict()
        while len(paths_queue) != 0:
            path = paths_queue.pop(0)

            path_start_node = path[0]
            if not path_start_node in bubble_start_end:
                bubble_start_end[ path_start_node ] = dict()

            path_end_node  = path[len(path) - 1]
            if not path_end_node in bubble_start_end[ path_start_node ]:
                bubble_start_end[ path_start_node ][ path_end_node ] = 0
            bubble_start_end[ path_start_node ][ path_end_node ] += 1
            
            if not path_end_node in max_non_branching_paths:
                continue

            for adjacent_path in max_non_branching_paths[path_end_node]:
                if len(path) + len(adjacent_path) - 1 > self._bubble_treshold:
                    continue
                if adjacent_path[len(adjacent_path) - 1] in path:
                    continue
                
                paths_queue.append(path + adjacent_path[1:])
        
        #print(bubble_start_end)
        bubble_count = 0
        #print(bubble_start_end.values())
        for candidate_bubble in bubble_start_end.values():
            
            paths_count = next(iter(candidate_bubble.values()))

            #if path_count > 2, then there are n choose k bubbles n = paths count and k = 2
            bubble_count += 0 if paths_count < 2 else ((math.factorial(paths_count) // math.factorial(paths_count - 2)) // 2)

        return bubble_count

    def str_adjacency_list(self):

        result_list = []
        for node in range(len(self.nodes)):
            if len(self.adjacency_list[node]) == 0:
                continue
            
            node_adjacents = [ self.nodes[node] ]
            node_adjacents.append(' -> ')
            
            for adjacent_node in self.adjacency_list[node]:
                
                node_adjacents.append(self.nodes[adjacent_node])
                node_adjacents.append(',')
            
            result_list.append(''.join(node_adjacents))

        return '\n'.join(result_list)

if __name__ == "__main__":

    k, t = map(int, sys.stdin.readline().strip().split(" "))
    
    reads = sys.stdin.read().strip().splitlines()
    
    de_bruijn_graph = De_Bruijn_Graph(k, t, reads)

    #print(de_bruijn_graph.str_adjacency_list())

    print(de_bruijn_graph.detect_bubbles())    
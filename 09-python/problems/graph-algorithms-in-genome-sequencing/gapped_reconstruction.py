import sys
from collections import namedtuple

Node_Degree = namedtuple('Node_Degree', ['vertex_no', 'in_degree', 'out_degree'])

class Paired_De_Bruijn_Graph:
    def __init__(self, k, d, paired_comp):
        
        assert(len(paired_comp) > 0)
        self._pattern_size = k
        self._distance = d
        assert(self._pattern_size > 0)

        self._build_gragh(paired_comp)

    def _build_gragh(self, paired_comp):
        
        self.nodes = []
        self.adjacency_list = []
        node_kmer_no_dict = dict()
        for pair in paired_comp:
            prefix, suffix = pair.split('|')
            assert(len(prefix) == self._pattern_size)
            assert(len(suffix) == self._pattern_size)

            prefix_node_no = self.get_node_no(prefix[0:self._pattern_size-1] + suffix[0:self._pattern_size-1], node_kmer_no_dict)
            suffix_node_no = self.get_node_no(prefix[1:] + suffix[1:], node_kmer_no_dict)

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

    def find_unbalanced_vertices(self):

        # 1. Compute in_degree for each vertex
        in_degree = [0 for _ in range(len(self.adjacency_list))]
        for u in range(len(self.adjacency_list)):
            for v in self.adjacency_list[u]:
                in_degree[v] += 1

        # 2. Compare in_degree vs. out_degree of each vertex
        u = 0
        self.unbalanced_vertices = []
        while u < len(self.adjacency_list):
            if in_degree[u] != len(self.adjacency_list[u]):
                self.unbalanced_vertices.append(Node_Degree(u, in_degree[u], len(self.adjacency_list[u])))
        
            u += 1

        return self.unbalanced_vertices

    def form_cycle(self, start, cycle, visited_edge_indexes, unvisited_edge_node_dict):
        
        node = start
        while visited_edge_indexes[node] + 1 < len(self.adjacency_list[node]):
            
            cycle.append(node)

            # Save this node, if there are 2 or more unvisited edges
            if (visited_edge_indexes[node] + 2) < len(self.adjacency_list[node]):
                unvisited_edge_node_dict[node] = (len(cycle) - 1)

            elif node in unvisited_edge_node_dict:
                unvisited_edge_node_dict.pop(node)
            
            visited_edge_indexes[node] += 1
            node = self.adjacency_list[node][ visited_edge_indexes[node] ]
            
        cycle.append(node)
                
        return -1 if len(unvisited_edge_node_dict) == 0 else next(iter(unvisited_edge_node_dict.values()))
    
    def eulerian_cycle(self):
                
        cycle = []
        visited_edge_indexes = [-1 for _ in range(len(self.nodes))]

        # nodes with unvisited edges: {node, position in cycle}
        unvisited_edge_node_dict = dict()
        
        new_start_pos_in_cycle = self.form_cycle(0, cycle, visited_edge_indexes, unvisited_edge_node_dict)

        while new_start_pos_in_cycle != -1:
            
            new_start = cycle[new_start_pos_in_cycle]
            new_cycle = cycle[new_start_pos_in_cycle:]
            new_cycle.extend(cycle[1:new_start_pos_in_cycle])
            cycle = new_cycle
            for node in unvisited_edge_node_dict:
                if unvisited_edge_node_dict[node] >= new_start_pos_in_cycle:
                    unvisited_edge_node_dict[node] -= new_start_pos_in_cycle
                else:
                    unvisited_edge_node_dict[node] += (len(cycle) - new_start_pos_in_cycle)

            new_start_pos_in_cycle = self.form_cycle(new_start, cycle, visited_edge_indexes, unvisited_edge_node_dict)
        
        return cycle

    def eulerian_path(self, unbalanced_vertices):
        
        path = []
        
        u = unbalanced_vertices[0].vertex_no
        u_in_degree = unbalanced_vertices[0].in_degree
        u_out_degree = unbalanced_vertices[0].out_degree

        v = unbalanced_vertices[1].vertex_no
        v_in_degree = unbalanced_vertices[1].in_degree
        v_out_degree = unbalanced_vertices[1].out_degree
    
        if (u_in_degree - u_out_degree) * (v_in_degree - v_out_degree) == -1:
            # Add an additional edge
            if u_in_degree > u_out_degree:
                add_edge_start = u
                add_edge_end = v

            else:
                add_edge_start = v
                add_edge_end = u

            self.adjacency_list[add_edge_start]. append(add_edge_end)
            
            # Find an Eulerian Cycle with the additional edge (it must be strongly connected)
            cycle = self.eulerian_cycle()

            # Remove the additional edge from the cycle
            edge_position_in_cycle = -1
            for i in range(len(cycle) - 1):
                if cycle[i] == add_edge_start and cycle[i + 1] == add_edge_end:
                    edge_position_in_cycle = i
                    break

            assert(edge_position_in_cycle != -1)

            if edge_position_in_cycle == len(cycle) - 2:
                path = cycle [0: edge_position_in_cycle + 1]

            elif edge_position_in_cycle == 0:
                path = cycle [1: ]

            else:
                path = cycle [edge_position_in_cycle + 1: ]
                path.extend(cycle [1: edge_position_in_cycle + 1])

        return path

    def _reconstruct_from_gapped_genome_path(self, path):
        
        prefixes, suffixes = [], []
        for node in path:
            node_label = self.nodes[ node ]
            prefix = node_label[0:self._pattern_size - 1]
            suffix = node_label[self._pattern_size - 1:]
            print("node_label, prefix, suffix: ", node_label, prefix, suffix)

            if len(prefixes) == 0:
                prefixes.append(prefix)
            elif (len(prefixes) - 2) < self._distance: 
                prefixes.append(prefix[self._pattern_size - 2])

            if len(suffixes) == 0:
                suffixes.append(suffix)
            else:
                suffixes.append(suffix[self._pattern_size - 2])
        print(prefixes, suffixes)
        return ''.join(prefixes + suffixes)

    def string_reconstruct(self):

        self.find_unbalanced_vertices()

        if not len(self.unbalanced_vertices) in (0, 2):
            return []

        if len(self.unbalanced_vertices) == 0:
            path =  self.eulerian_cycle()
            path.append(path[0])
            path = path[1:]
            
        else:
            path =  self.eulerian_path(self.unbalanced_vertices)
            
        return self._reconstruct_from_gapped_genome_path(path)

if __name__ == "__main__":
    k, d = map(int, sys.stdin.readline().strip().split())
    paired_comp = [line.strip() for line in sys.stdin if line.strip()]

    paired_de_bruijn_graph = Paired_De_Bruijn_Graph(k, d, paired_comp)

    print(paired_de_bruijn_graph.string_reconstruct())

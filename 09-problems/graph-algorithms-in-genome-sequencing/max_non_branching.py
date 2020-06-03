import sys

class Graph:
    def __init__(self, edges):
        
        self._build_graph(edges)
        self._compute_indgrees()
    
    def _build_graph(self, edges):
        
        self.nodes = []
        self.adjacency_list = []
                
        node_label_dict = dict()
        for edge in edges:    
            (start_vertex_label, end_vertices_labels) = edge.split(' -> ')
            
            start_vertex_no = self._get_node_no(start_vertex_label, node_label_dict)

            self.adjacency_list[start_vertex_no] = [self._get_node_no(label, node_label_dict) for label in end_vertices_labels.split(',')]
    
    def _get_node_no(self, label, node_label_dict):
        
        if label in node_label_dict:
            node_no = node_label_dict[label]

        else:
            node_no = len(self.nodes)
            self.nodes.append(label)
            self.adjacency_list.append([])
            node_label_dict[label] = node_no

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

            non_branching_path = [self.nodes[v]]
            maximal_non_branching_nodes.add(v)
            
            v = self.adjacency_list[v][0]
            v_out_degree = len(self.adjacency_list[v])
            while self.in_degree[v] == v_out_degree == 1 and v != start:

                non_branching_path.append(self.nodes[v])
                maximal_non_branching_nodes.add(v)
                
                v = self.adjacency_list[v][0]
                v_out_degree = len(self.adjacency_list[v])

            if v == start:
                non_branching_path.append(self.nodes[v])
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
                        
                        non_branching_path = [self.nodes[u]]
                        
                        v_out_degree = len(self.adjacency_list[v])
                        while self.in_degree[v] == v_out_degree == 1:
                            
                            non_branching_path.append(self.nodes[v])
                            if v in non_branching_path_nodes:
                                non_branching_path_nodes.add(v)
                            
                            v = self.adjacency_list[v][0]
                            v_out_degree = len(self.adjacency_list[v])

                        non_branching_path.append(self.nodes[v])
                        if v in non_branching_path_nodes:
                                non_branching_path_nodes.add(v)
                        paths.append(non_branching_path)

        # Find isolated cycles
        self.find_isolated_cycles(paths, non_branching_path_nodes)
                
        return '\n'.join( ['->'.join(paths[i]) for i in range(len(paths))])


if __name__ == "__main__":
    edges = sys.stdin.read().strip().splitlines()

    graph = Graph(edges)

    print(graph.find_maximal_non_branching_paths())

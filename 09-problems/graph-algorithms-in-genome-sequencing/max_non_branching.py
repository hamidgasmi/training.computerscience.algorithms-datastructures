import sys
from collections import namedtuple

Node_Degree = namedtuple('Node_Degree', ['vertex_no', 'in_degree', 'out_degree'])

class Graph:
    def __init__(self, edges):
        
        self._build_graph(edges)
    
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
            self.reversed_adjacency_list.append([])
            node_label_dict[label] = node_no

        return node_no

    def compute_indgrees(self):

        # 1. Compute in_degree for each vertex
        self.in_degree = [0 for _ in range(len(self.adjacency_list))]
        for u in range(len(self.adjacency_list)):
            for v in self.adjacency_list[u]:
                self.in_degree[v] += 1        
    
    def find_maximal_non_branching_paths(self):
        
        
        return ""


if __name__ == "__main__":
    edges = sys.stdin.read().strip().splitlines()

    graph = Graph(edges)

    print(graph.find_maximal_non_branching_paths())

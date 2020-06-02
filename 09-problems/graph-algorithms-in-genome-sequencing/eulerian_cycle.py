import sys
from collections import namedtuple

Node_Degree = namedtuple('Node_Degree', ['vertex_no', 'in_degree', 'out_degree'])

class Graph:
    def __init__(self, edges):
        
        self._build_graph(edges)
    
    def _build_graph(self, edges):
        
        self.nodes = []
        self.adjacency_list = []
        self.reversed_adjacency_list = []

        node_label_dict = dict()
        for edge in edges:    
            (start_vertex_label, end_vertices_labels) = edge.split(' -> ')
            
            start_vertex_no = self._get_node_no(start_vertex_label, node_label_dict)

            self.adjacency_list[start_vertex_no] = [self._get_node_no(label, node_label_dict) for label in end_vertices_labels.split(',')]

            for a in self.adjacency_list[start_vertex_no]:
                 self.reversed_adjacency_list[a].append(start_vertex_no)

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
    
    def explore(self, v, adj, postOrderVisits):
        self.visited[v] = True
        for a in adj[v]:
            if not self.visited[a]:
                self.explore(a, adj, postOrderVisits)

        postOrderVisits.append(v)

    def dfs(self, adj, postOrderVisits):

        self.visited = [ False for _ in range(len(self.nodes)) ]
        for v in range(len(adj)):
            if not self.visited[v]:
                self.explore(v, adj, postOrderVisits)

    def find_strongly_connected_components(self):
        
        postOrderVisits = []
        self.dfs(self.reversed_adjacency_list, postOrderVisits)
        self.visited = [ False for _ in range(len(self.nodes)) ]
        self.strongly_connected_components = []
        for i in range(len(postOrderVisits) - 1, -1, -1):
            v = postOrderVisits[i]
            if not self.visited[v]:
                aSCC = []
                self.explore(v, self.adjacency_list, aSCC)
                self.strongly_connected_components.append(aSCC)

        return self.strongly_connected_components

    def _is_eulerian_graph(self):
        
        # 1. Is balanced
        self.find_unbalanced_vertices()
        assert(len(self.unbalanced_vertices) == 0)

        # 2. Is strongly connected
        self.find_strongly_connected_components()
        assert(len(self.strongly_connected_components) == 1)

        return True

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

        assert(self._is_eulerian_graph())
        
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

if __name__ == "__main__":
    edges = sys.stdin.read().strip().splitlines()
    
    eulerian_graph = Graph(edges)

    print('->'.join( [ eulerian_graph.nodes[node] for node in eulerian_graph.eulerian_cycle() ] ))

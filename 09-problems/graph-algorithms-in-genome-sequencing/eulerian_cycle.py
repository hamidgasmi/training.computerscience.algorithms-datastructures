import sys

class Eulerian_Graph:
    def __init__(self, edges):
        
        self._build_graph(edges)
        
        self._is_eulerian_graph()
    
    def _build_graph(self, edges):
        
        self.nodes = []
        self.adjacency_list = []
        self.reversed_adjacency_list = []
        self.edges_counts = 0
        node_label_dict = dict()

        for edge in edges:    
            (start_vertex_label, end_vertices_labels) = edge.split(' -> ')
            
            start_vertex_no = self._get_node_no(start_vertex_label, node_label_dict)

            self.adjacency_list[start_vertex_no] = [self._get_node_no(label, node_label_dict) for label in end_vertices_labels.split(',')]
            self.edges_counts += len(self.adjacency_list[start_vertex_no])

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

    def _is_balanced(self):

        # 1. Compute in_degree for each vertex
        in_degree = [0 for _ in range(len(self.adjacency_list))]
        for u in range(len(self.adjacency_list)):
            for v in self.adjacency_list[u]:
                in_degree[v] += 1

        # 2. Compare in_degree vs. out_degree of each vertex
        balanced = True
        u = 0
        self.balanced = ""
        while u < len(self.adjacency_list):
            if in_degree[u] != len(self.adjacency_list[u]):
                balanced = False
                break
        
            u += 1
        
        return balanced

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

    def strongly_connected_components_number(self):
        
        postOrderVisits = []
        self.dfs(self.reversed_adjacency_list, postOrderVisits)
        self.visited = [ False for _ in range(len(self.nodes)) ]
        aSCCList = []
        for i in range(len(postOrderVisits) - 1, -1, -1):
            v = postOrderVisits[i]
            if not self.visited[v]:
                aSCC = []
                self.explore(v, self.adjacency_list, aSCC)
                aSCCList.append(aSCC)

        return aSCCList

    def _is_strongly_connected(self):
        
        aSCCList = self.strongly_connected_components_number()
        
        return len(aSCCList) == 1

    def _is_eulerian_graph(self):
        
        # 1. Is balanced
        assert(self._is_balanced())

        # 2. Is strongly connected
        assert(self._is_strongly_connected())

    def form_cycle(self, start, cycle, visited_edge_indexes, unvisited_edge_node_dict):
        
        node = start

        while visited_edge_indexes[node] + 1 < len(self.adjacency_list[node]):
            
            cycle.append(node)

            # Save this node, if there are 2 or more unvisited edges
            if visited_edge_indexes[node] + 2 < len(self.adjacency_list[node]):
                unvisited_edge_node_dict[node] = len(cycle) - 1

            elif node in unvisited_edge_node_dict:
                unvisited_edge_node_dict.pop(node)
            
            visited_edge_indexes[node] += 1
            node = self.adjacency_list[node][ visited_edge_indexes[node] ]
            
        cycle.append(node)
        
        return -1 if len(unvisited_edge_node_dict) == 0 else unvisited_edge_node_dict.popitem()[1]

    def eulerian_cycle(self):
        
        cycle = []
        visited_edge_indexes = [-1 for _ in range(len(self.nodes))]

        # nodes with unvisited edges: {node, position in cycle}
        unvisited_edge_node_dict = dict()

        new_start_pos_in_cycle = self.form_cycle(0, cycle, visited_edge_indexes, unvisited_edge_node_dict)

        while new_start_pos_in_cycle != -1:

            new_cycle = cycle[new_start_pos_in_cycle:]
            new_cycle.extend(cycle[1:new_start_pos_in_cycle])
            cycle = new_cycle
            
            new_start = cycle[0]
            new_start_pos_in_cycle = self.form_cycle(new_start, cycle, visited_edge_indexes, unvisited_edge_node_dict)
        
        return '->'.join([ self.nodes[node] for node in cycle])

if __name__ == "__main__":
    edges = sys.stdin.read().strip().splitlines()
    
    eulerian_graph = Eulerian_Graph(edges)

    print(eulerian_graph.eulerian_cycle())

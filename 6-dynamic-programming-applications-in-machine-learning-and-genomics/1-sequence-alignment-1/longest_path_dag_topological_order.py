import sys
from collections import namedtuple

Edge = namedtuple('Edge', ['v_no', 'w'])
Vertice_Dist = namedtuple('Vertice_Dist', ['prev', 'dist'])

class Directed_Acyclic_Graph:
    def __init__(self, source, sink, edges):
        
        self.v_no_label_gap = source * (-1) #v_no are 0-based index but input labels could start at any position
        self.vertices_count = abs(sink - source) + 1
        self.is_valid_dag = True
        self.longest_path_len = 0
        self.longest_path = []

        self.build_adjacency_list(edges)
        
    def build_adjacency_list(self, edges):
        
        self.adjacency_list = [[] for _ in range(self.vertices_count)]

        self.is_valid_source = True
        self.is_valid_sink = False
        for edge in edges:
            u = int(edge.split("->")[0]) + self.v_no_label_gap
            v = int(edge.split("->")[1].split(":")[0]) + self.v_no_label_gap
            w = int(edge.split("->")[1].split(":")[1])
            
            self.adjacency_list[u].append(Edge(v, w))
            
            self.is_valid_source &= (v != 0)
            self.is_valid_sink |= (v == self.vertices_count - 1)
            
        self.is_valid_source &= (len(self.adjacency_list[0]) > 0)
        self.is_valid_sink &= len(self.adjacency_list[self.vertices_count - 1]) == 0

    def check_cycke_vertex(self, u, visited, cycle):
        
        visited[u] = True
        cycle[u] = True
        for edge in self.adjacency_list[u]:

            if cycle[edge.v_no]:
                return True
            
            if visited[edge.v_no]:
                continue
            
            if self.check_cycke_vertex(edge.v_no, visited, cycle):
                return True

        cycle[u] = False

        return False

    def check_dag_dfs(self):

        visited = [False for _ in range(self.vertices_count)] 
        cycle  = [False for _ in range(self.vertices_count)] 
        
        self.is_valid_dag = True
        for v in range(self.vertices_count):
            if not visited[v]:
                if self.check_cycke_vertex(v, visited, cycle):
                    self.is_valid_dag = False
                    break
    
    def sort_topologically_vertex(self, u, visited, topo_sort):
        
        visited[u] = True
        for edge in self.adjacency_list[u]:
            if not visited[edge.v_no]:
               self.sort_topologically_vertex(edge.v_no, visited, topo_sort)
        
        topo_sort.append(u)

    def sort_topologically_dfs(self):
                
        visited = [False for _ in range(self.vertices_count)]
        topo_sort = []
        for u in range(self.vertices_count):
            if not visited[u]:
                self.sort_topologically_vertex(u, visited, topo_sort)
        
        return topo_sort[::-1]

    def longest_path_backtrack(self, u, max_distance):

        longest_path = []     
        while u != -1:
            longest_path.append(str(u - self.v_no_label_gap))
            u = max_distance[u].prev
        
        return longest_path[::-1]

    def compute_longest_path(self):

        # Validations:
        #  G is a valid DAG: it has no cycle
        #  Source is a valid source vertex: there is no incoming edges
        #  Sink is a valid sink vertex: there is no outgoing edges
        if not (self.is_valid_source and self.is_valid_sink):
            return
        self.check_dag_dfs()
        if not self.is_valid_dag:
            return

        max_distance = [Vertice_Dist(-1, - sys.maxsize - 1) for _ in range(self.vertices_count)]
        max_distance[0] = Vertice_Dist(-1, 0)

        topo_sort = self.sort_topologically_dfs()
        for u in topo_sort:
            for e in self.adjacency_list[u]:
                v = e.v_no
                candidate_distance = max_distance[u].dist + e.w
                if max_distance[v].dist < candidate_distance:
                    max_distance[v] = Vertice_Dist(u, candidate_distance)
        
        sink_vertex = self.vertices_count - 1
        self.longest_path_len = max_distance[sink_vertex].dist
        self.longest_path = self.longest_path_backtrack(sink_vertex, max_distance)

    def longest_path_to_str(self):

        return '->'.join(self.longest_path)

if __name__ == "__main__":

    source = int(sys.stdin.readline().strip())
    sink = int(sys.stdin.readline().strip())
    edges = [line.strip() for line in sys.stdin]

    dag = Directed_Acyclic_Graph(source, sink, edges)
    dag.compute_longest_path()

    print(dag.longest_path_len)
    print(dag.longest_path_to_str())

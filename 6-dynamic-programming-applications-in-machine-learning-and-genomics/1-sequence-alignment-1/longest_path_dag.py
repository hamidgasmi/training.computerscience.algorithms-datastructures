import sys
from collections import namedtuple

Edge = namedtuple('Edge', ['v', 'w'])

class Directed_Acyclic_Graph:
    def __init__(self, source, sink, edges):
        
        self.v_no_label_gap = source #v_no are 0-based index but input labels could start at any position
        self.vertices_count = sink - source + 1
        self.is_valid_dag = True
        
        self.build_adjacency_list(edges)
        
        #print(self.adjacency_list)
        #print("self.is_valid_source: ", self.is_valid_source)
        #print("self.is_valid_sink: ", self.is_valid_sink)
        #print("self.is_valid_dag: ", self.is_valid_dag)
        
    def build_adjacency_list(self, edges):
        
        self.adjacency_list = [[] for _ in range(self.vertices_count)]

        self.is_valid_source = True
        self.is_valid_sink = False
        for edge in edges:
            u = int(edge.split("->")[0]) - self.v_no_label_gap
            v = int(edge.split("->")[1].split(":")[0]) - self.v_no_label_gap
            w = int(edge.split("->")[1].split(":")[1])

            self.adjacency_list[u].append(Edge(v, w))
            
            self.is_valid_source &= (v != 0)
            self.is_valid_sink |= (v == self.vertices_count - 1)
            
        self.is_valid_source &= (len(self.adjacency_list[0]) > 0)
        self.is_valid_sink &= len(self.adjacency_list[self.vertices_count - 1]) == 0
        
    def explore_path(self, u, visited, cycle):
        
        visited[u] = True
        cycle[u] = True
        for edge in self.adjacency_list[u]:

            if cycle[edge.v]:
                return True
            
            if visited[edge.v]:
                continue
            
            if self.explore_path(edge.v, visited, cycle):
                return True

        cycle[u] = False

        return False

    def check_dag_dfs(self):

        visited = [False for _ in range(self.vertices_count)] 
        cycle  = [False for _ in range(self.vertices_count)] 

        self.is_valid_dag = True
        for v in range(self.vertices_count):
            if not visited[v]:
                if self.explore_path(v, visited, cycle):
                    self.is_valid_dag = False
                    break
    
    def compute_longest_path(self, source, sink):
        self.longest_path_len = 0
        self.longest_path = []

        if not (self.is_valid_source and self.is_valid_sink):
            return

        self.check_dag_dfs()
        if not self.is_valid_dag:
            return

        longest_paths = [0 for _ in range(self.vertices_count)]
        #compute_longest_paths()
        


    def longest_path_to_str(self):

        return '->'.join(self.longest_path)

if __name__ == "__main__":

    source = int(sys.stdin.readline().strip())
    sink = int(sys.stdin.readline().strip())
    edges = [line.strip() for line in sys.stdin]

    dag = Directed_Acyclic_Graph(source, sink, edges)
    dag.compute_longest_path(source, sink)

    print(dag.longest_path_len)
    print(dag.longest_path_to_str())

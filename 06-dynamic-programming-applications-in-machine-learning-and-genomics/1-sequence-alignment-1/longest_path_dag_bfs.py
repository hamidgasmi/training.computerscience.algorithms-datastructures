import sys
from queue import Queue
from collections import namedtuple

Edge = namedtuple('Edge', ['v_no', 'w'])
Vertex_Distance = namedtuple('Vertex_Distance', ['predecessor', 'dist'])

class Directed_Acyclic_Graph:
    def __init__(self, source, sink, edges):
        
        self.v_no_label_gap = source * (-1) #v_no are 0-based index but input labels could start at any position
        self.vertices_count = abs(sink - source) + 1
        self.is_valid_dag = True
        
        self.build_adjacency_list(edges)
        
    def build_adjacency_list(self, edges):
        
        self.adjacency_list = [[] for _ in range(self.vertices_count)]

        self.is_valid_source = True
        self.is_valid_sink = True
        for edge in edges:
            u = int(edge.split("->")[0]) + self.v_no_label_gap
            v = int(edge.split("->")[1].split(":")[0]) + self.v_no_label_gap
            w = int(edge.split("->")[1].split(":")[1])
            
            self.adjacency_list[u].append(Edge(v, w))
            
            self.is_valid_source &= (v != 0)
        
        self.is_valid_source &= (len(edges) == 0 or len(self.adjacency_list[0]) > 0)
        self.is_valid_sink = len(self.adjacency_list[self.vertices_count - 1]) == 0

    def explore_path(self, u, visited, cycle):
        
        visited[u] = True
        cycle[u] = True
        for edge in self.adjacency_list[u]:

            if cycle[edge.v_no]:
                return True
            
            if visited[edge.v_no]:
                continue
            
            if self.explore_path(edge.v_no, visited, cycle):
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
    def longest_path_backtrack(self, u, max_distance):

        longest_path = []     
        while u != -1:
            longest_path.append(str(u - self.v_no_label_gap))
            u = max_distance[u].predecessor
        
        return longest_path[::-1]

    def longest_path_bfs(self, source, sink):
        self.longest_path_len = 0
        self.longest_path = []

        if not (self.is_valid_source and self.is_valid_sink):
            return

        self.check_dag_dfs()
        if not self.is_valid_dag:
            return

        max_distance = [Vertex_Distance(-1, - sys.maxsize - 1) for _ in range(self.vertices_count)]
        max_distance[0] = Vertex_Distance(-1, 0)

        q = Queue()
        q.put(0)

        while not q.empty():
            u = q.get()
            for e in self.adjacency_list[u]:
                candidate_distance = max_distance[u].dist + e.w
                if max_distance[e.v_no].dist < candidate_distance:
                    max_distance[e.v_no] = Vertex_Distance(u, candidate_distance)

                q.put(e.v_no)
        
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
    dag.longest_path_bfs(source, sink)

    print(dag.longest_path_len)
    print(dag.longest_path_to_str())

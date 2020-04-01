#Uses python3
import sys
import itertools

class Graph:
    def __init__(self, n, edges):
        self.vertices_size = n
        self.adjacency_list = [set()] * n
        self.create_adjacency_list(edges)

    def create_adjacency_list(self, edges):
        for (a, b) in edges:
            self.adjacency_list[a - 1].add(b)
            self.adjacency_list[b - 1].add(a)
        
    

class Hamiltonian_path_sat_reduction:
    def __init__(self, n, edges):
        self.clauses = []
        self.positions = [p for p in range(1, n + 1)]
        self.graph = Graph(n, edges)

    def vertice_num(self, v, p):
        return len(self.positions) * (v - 1) + p

    def exactly_one_of(self, literals):
        self.clauses.append([l for l in literals])

        for pair in itertools.combinations(literals, 2):
            self.clauses.append([-l for l in pair])

    def create_sat_clauses(self):
        
        # 1- Each vertice v must appear in the path: (X1v V X2v V ... Xvn)
        # 2- No vertice v can appear twice in the path: (-Xiv V -Xjn) and i != j
        for v in range(1, self.graph.vertices_size + 1):
            self.exactly_one_of([ self.vertice_num(v, p) for p in self.positions ])

        # 3- Each position p in the path must be occupied by a vertice: (Xp1 V Xp2 V ... V Xpn)
        # 4- No 2 nodes can occupy the same position: (-Xpv1 V Xpv2) for all p and v1 != v2
        for p in self.positions:
            self.exactly_one_of([ self.vertice_num(v, p) for v in range(1, self.graph.vertices_size + 1) ])

        # 5- No adjacent vertices (v, u) in the graph can't be adjacent in the path: 
        #    (-Xpv V -Xp+1u) for 1 <= p < n and for all v and non adjancent vertices u
        for i in range(self.graph.vertices_size):
            for j in range(self.graph.vertices_size):

                v = i + 1
                u = j + 1

                if v == u:
                    continue
                
                if u in self.graph.adjacency_list[i]:
                    continue
                
                for p in range(1, len(self.positions)):
                    self.clauses.append([-self.vertice_num(v, p) -self.vertice_num(u, p + 1)])
    
    def print_equisatisfiable_sat_formula(self):
        
        for c in self.clauses:
            for l in c:
                print(l, end = " ")
            print(0, end = "")
            print("")

if __name__ == "__main__":

    n, m = map(int, input().split())
    edges = [ list(map(int, input().split())) for i in range(m) ]

    reduction = Hamiltonian_path_sat_reduction(n, edges)
    reduction.create_sat_clauses()
    reduction.print_equisatisfiable_sat_formula()

#Uses python3
import sys
import itertools

# Analysis:
# Cleaning appartment problem corresponds to Hamiltonian path problem where:
# ... Every room is represented with a vertice
# ... Every corridor between 2 rooms is reprensented by an edge between 2 vertices
# Hamiltonian path could be reduced to a sat problem with:
# ... as literals: Xpv for a position p in the path is occupied by a vertice v
# ... as conditions:
# .... 1- Each vertice v must appear in the path: (X1v V X2v V ... Xvn)
# .... 2- No vertice v can appear twice in the path: (-Xiv V -Xjv) and for all v, i, j and i != j
# .... 3- Each position p in the path must be occupied by a vertice: (Xp1 V Xp2 V ... V Xpn) for all 1 <= p <= n
# .... 4- No 2 vertices can occupy the same position: (-Xpv V -Xpu) for all p, v, u and v != u
# .... 5- No adjacent vertices (v, u) in the graph can't be adjacent in the path: (-Xpv V -Xp+1u) for 1 <= p < n and for all v and non adjancent vertices u
# ....... We'll use an adjacency list with "set" data-structure, to let find if a vertice u is adjacent to v in O(1)

class Graph:
    # Running Time: O(|E|)
    def __init__(self, n, edges):
        self.vertices_size = n
        self.adjacency_list = [set() for _ in range(n)]
        self.create_adjacency_list(edges)

    # Running Time: O(|E|)
    def create_adjacency_list(self, edges):
        for (a, b) in edges:
            self.adjacency_list[a - 1].add(b)
            self.adjacency_list[b - 1].add(a)
        
class Hamiltonian_path_sat_reduction:
    
    # Running Time: O(|E|)
    def __init__(self, n, edges):
        self.clauses = []
        self.positions = [p for p in range(1, n + 1)]
        self.graph = Graph(n, edges)

    # Running Time: O(1)
    def vertice_num(self, v, p):
        return len(self.positions) * (v - 1) + p

    # Running Time: O(L^2)
    def exactly_one_of(self, literals):
        # O(L)
        self.clauses.append([l for l in literals])

        # O(L * (L - 1) / 2) = O(L^2)
        for pair in itertools.combinations(literals, 2):
            self.clauses.append([-l for l in pair])

    # Running time: O(|V|^3)
    def create_sat_clauses(self):
        
        # 1- Each vertice v must appear in the path: (X1v V X2v V ... Xvn)
        # 2- No vertice v can appear twice in the path: (-Xiv V -Xjv) and i != j
        # Running time: |V| * T(exactly_one_of()) = O(|V|^3)
        for v in range(1, self.graph.vertices_size + 1):
            self.exactly_one_of([ self.vertice_num(v, p) for p in self.positions ])

        # 3- Each position p in the path must be occupied by a vertice: (Xp1 V Xp2 V ... V Xpn) for all 1 <= p <= n
        # 4- No 2 vertices can occupy the same position: (-Xpv V -Xpu) for all p, v, u and v != u
        # Running time: |V| * T(exactly_one_of()) = O(|V|^3)
        for p in self.positions:
            self.exactly_one_of([ self.vertice_num(v, p) for v in range(1, self.graph.vertices_size + 1) ])

        # 5- No adjacent vertices (v, u) in the graph can't be adjacent in the path: 
        #    (-Xpv V -Xp+1u) for 1 <= p < n and for all v and non adjancent vertices u
        # Running time: O(|V| (|V| (|V| - 1) - |E|)) = O(|V| (|V|^2 - |E|))
        # In case of a dense graph (|E| ~ |V|^2): O(|V|)
        # In case of a sparse graph (|E| ~ |V|): O(|V|^3)
        for i in range(self.graph.vertices_size):
            for j in range(self.graph.vertices_size):
                # The number of loops is: the number of possible edges x 2 minus the number of actual edges:
                # ... (x2) because an edge (u, v) is considered twice: 
                # ...... from u to v: u would be then in p and v in p + 1 
                # ...... from v to u: v would be then in p and u in p + 1
                # The number of loops is (|V| - 1) - |E|
                
                v = i + 1
                u = j + 1
                
                if v == u:
                    continue
                
                # O(1)
                if u in self.graph.adjacency_list[i]:
                    continue
                
                # O(|V|)
                for p in range(1, len(self.positions)):
                    not_reachable_literals = []
                    not_reachable_literals.append(-self.vertice_num(v, p))
                    not_reachable_literals.append(-self.vertice_num(u, p + 1))
                    self.clauses.append(not_reachable_literals)
    
    def print_equisatisfiable_sat_formula(self):
        
        print(len(self.clauses), self.graph.vertices_size * len(self.positions))

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

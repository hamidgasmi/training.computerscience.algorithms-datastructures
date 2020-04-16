# python3

class Implication_graph:
    def __init__(self, n, clauses):
        self.sat_variables_count = n
        self.vertices_count = 2 * n
        self.build_adjacency_list(clauses)
        self.build_reversed_adjacency_list()

    # Each variable Xi in SAT formula, 2 vertices will be created
    # ... Vertice 1 corresponds to Xi and its number is Xi - 1
    # ... Vertice 2 corresponds to -Xi and its number is Xi - 1 + Variables count
    # E.g. 3 SAT variables: X1, X2, X3: 6 vertices will be created
    #   Vertices  0      1       2       3       4       5
    #   Variables X1     X2      X3     -X1     -X2     -X3
    def vertice_num(self, variable_num):
        return variable_num - 1 if variable_num > 0 else (-1) * variable_num - 1 + self.sat_variables_count

    def non_vertice_num(self, vertice_num):
        return vertice_num + self.sat_variables_count if vertice_num < self.sat_variables_count else vertice_num - self.sat_variables_count
        
    # Time Complexity: O(|C|)
    def build_adjacency_list(self, clauses):

        self.adjacency_list = [[] for _ in range(2 * self.sat_variables_count)]

        for c in clauses:
            l = c[0]
            v_l  = self.vertice_num(l)
            v_non_l = self.vertice_num((-1) * l)
            if len(c) == 1:
                # (l): to create an edge from -l to l: -l --> l
                self.adjacency_list[v_non_l].append(v_l)

            else:
                k = c[1]
                v_k = self.vertice_num(k)
                v_non_k = self.vertice_num((-1) * k)
                # (l V k): to create 2 edges from !l to k and !k to l: 
                # ... !l --> k 
                # ... !k --> l
                self.adjacency_list[v_non_l].append(v_k)
                self.adjacency_list[v_non_k].append(v_l)

        #for v in range(self.vertices_count:
        #    print("Vertice V (" + str(v) + ") Adjacency list: ", self.adjacency_list[v])
    
    # Time Complexity: O(|E|) = O(|Edges|) = O(2 |Clauses|) = O(|C|)
    def build_reversed_adjacency_list(self):

        self.reversed_adjacency_list = [[] for _ in range(self.vertices_count)]

        for v in range(self.vertices_count):
            for a in self.adjacency_list[v]:
                self.reversed_adjacency_list[a].append(v)

        #for v in range(self.vertices_count:
        #    print("Vertice V (" + str(v) + ") Reversed Adjacency list: ", self.reversed_adjacency_list[v])

    def explore(self, v, an_adjacency_list, preorder_visits, postorder_visits):
        
        self.visited[v] = True
        if preorder_visits != None:
            preorder_visits.append(v)

        for a in an_adjacency_list[v]:
            if not self.visited[a]:
                self.explore(a, an_adjacency_list, preorder_visits, postorder_visits)

        if postorder_visits != None:
            postorder_visits.append(v)

    def dfs(self, an_adjacency_list, dfs_preorder, dfs_postorder):
        self.visited = [False] * self.vertices_count

        for v in range(self.vertices_count):
            if not self.visited[v]:
                self.explore(v, an_adjacency_list, dfs_preorder, dfs_postorder)

    def stronly_connected_components(self):

        dfs_postorder = []

        # 1. Find postorder in Gr
        # ... Source vertices in Gr have the highest postorder
        # ... A source vertice in Gr is Sink vertice in G
        self.dfs(self.reversed_adjacency_list, None, dfs_postorder)
        print("dfs_postorder: ", dfs_postorder)

        # 2. Find SCCs in G
        sccs = []
        self.visited = [False] * self.vertices_count
        for i in range(len(dfs_postorder) - 1, -1, -1):
            v = dfs_postorder[i]
            if not self.visited[v]:
                sccs.append([])
                self.explore(v, self.adjacency_list, None, sccs[len(sccs) - 1])

        return sccs

    def solve_2sat(self):

        strongly_connected_components = self.stronly_connected_components()
        
        # sccs is ordered in reversed topological order
        vertice_assignment = [-1] * self.vertices_count
        for scc in strongly_connected_components:
            for v in scc:
                if vertice_assignment[v] == -1:
                    vertice_assignment[v] = 1

                    non_v = self.non_vertice_num(v)
                    if vertice_assignment[non_v] == -1:
                        vertice_assignment[non_v] = 0

                if vertice_assignment[non_v] == 1:
                    return None

        print("sccs: ", strongly_connected_components)
        print("vertice_assignment: ", vertice_assignment)
        return vertice_assignment[:self.sat_variables_count]


def isSatisfiable(n, clauses):
    
    g = Implication_graph(n, clauses)
    
    return g.solve_2sat()

# Naive Solution:
# Time Complexity: O(2^n)
def isSatisfiable_naive(n, clauses):
    for mask in range(1<<n):
        result = [ (mask >> i) & 1 for i in range(n) ]
        formulaIsSatisfied = True
        for clause in clauses:
            clauseIsSatisfied = False
            if result[abs(clause[0]) - 1] == (clause[0] < 0):
                clauseIsSatisfied = True
            if result[abs(clause[1]) - 1] == (clause[1] < 0):
                clauseIsSatisfied = True
            if not clauseIsSatisfied:
                formulaIsSatisfied = False
                break
        if formulaIsSatisfied:
            return result
    return None

if __name__ == "__main__":
    
    n, m = map(int, input().split())
    clauses = [ list(map(int, input().split())) for i in range(m) ]

    #result = isSatisfiable_naive(n, clauses)
    result = isSatisfiable(n, clauses)

    if result is None:
        print("UNSATISFIABLE")
    else:
        print("SATISFIABLE")
        print(" ".join(str(i + 1 if result[i] else -i-1) for i in range(n)))
        #print(" ".join(str(-i-1 if result[i] else i+1) for i in range(n)))

# python3

# Naive Solution:
# Time Complexity: O(2^n)
def isSatisfiable_naive():
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

class ImplicationGraph:
    def __init__(self, n, clauses):
        self.adjacency_list = [[] for _ in range(2 * n)]
        self.build_adjacency_list(n, clauses)
        self.build_reversed_adjacency_list()

    def sat_variables_count(self):
        len(self.adjacency_list) // 2

    def vertices_count(self):
        len(self.adjacency_list)

    # Each variable Xi in SAT formula, 2 vertices will be created
    # ... Vertice 1 corresponds to Xi and its number is Xi - 1
    # ... Vertice 2 corresponds to -Xi and its number is Xi - 1 + Variables count
    # E.g. 3 SAT variables: X1, X2, X3: 6 vertices will be created
    #   Vertices  0      1       2       3       4       5
    #   Variables X1     X2      X3     -X1     -X2     -X3
    def get_vertice_num(self, variable_num):
        return variable_num - 1 if variable_num > 0 else (-1) * variable_num - 1 + self.sat_variables_count()

    # Time Complexity: O(|C|)
    def build_adjacency_list(self, n, clauses):

        for c in clauses:
            l = c[0]
            v_non_l = self.get_vertice_num((-1) * l)
            v_l  = self.get_vertice_num(l)
            if len(c) == 1:
                # (l): to create an edge from -l to l: -l --> l
                self.adjacency_list[v_non_l].append(v_l)

            else:
                k = c[1]
                v_k = self.get_vertice_num(k)
                v_non_k = self.get_vertice_num((-1) * k)
                # (l V k): to create 2 edges from !l to k and !k to l: 
                # ... !l --> k 
                # ... !k --> l
                self.adjacency_list[v_non_l].append(self.get_vertice_num(v_k))
                self.adjacency_list[v_non_k].append(self.get_vertice_num(v_l))
    
    # Time Complexity: O(|E|) = O(|Edges|) = O(2 |Clauses|) = O(|C|)
    def build_reversed_adjacency_list(self):

        self.reversed_adjacency_list = [[] for _ in range(self.vertices_count())]

        for v in range(self.vertices_count()):
            for a in self.adjacency_list[v]:
                self.reversed_adjacency_list[a].append(v)
    
if __name__ == "__main__":
    
    n, m = map(int, input().split())
    clauses = [ list(map(int, input().split())) for i in range(m) ]

    result = isSatisfiable_naive()
    if result is None:
        print("UNSATISFIABLE")
    else:
        print("SATISFIABLE")
        print(" ".join(str(-i-1 if result[i] else i+1) for i in range(n)))

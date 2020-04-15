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
        self.reversed_adjacency_list = [[] for _ in range(2 * n)]
        self.build_adjacency_list(clauses)

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

    # It will build 2 adjacency lists:
    # ... 1. 1st one corresponds to the implication graph G
    # ... 2. 2nd one corresponds to the reversed graph of G, Gr
    def build_adjacency_list(self, clauses):

        for c in clauses):
            pass

if __name__ == "__main__":
    
    n, m = map(int, input().split())
    clauses = [ list(map(int, input().split())) for i in range(m) ]

    result = isSatisfiable_naive()
    if result is None:
        print("UNSATISFIABLE")
    else:
        print("SATISFIABLE")
        print(" ".join(str(-i-1 if result[i] else i+1) for i in range(n)))

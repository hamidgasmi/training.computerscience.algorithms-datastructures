import sys
from collections import deque

# This problem can be reduced to a 2-SAT problem
# 2-SAT problem can be then solved efficiently by using an implication graph
# It's solved 3 different ways:
# ... 1- Naive solution
# ... 2- Implication graph + recursive DFS
# ... 3- Implication graph + Iterative DFS

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

    # Time Complexity: O(|E|) = O(|Edges|) = O(2 |Clauses|) = O(|C|)
    def build_reversed_adjacency_list(self):

        self.reversed_adjacency_list = [[] for _ in range(self.vertices_count)]

        for v in range(self.vertices_count):
            for a in self.adjacency_list[v]:
                self.reversed_adjacency_list[a].append(v)
    
    def previsit(self, v, preorder_visits):
        self.visited[v] = True
        if preorder_visits != None:
            preorder_visits.append(v)

    def postvisit(self, v, postorder_visits):
        if postorder_visits != None:
            postorder_visits.append(v)
    
    # The method below does a DFS exploration from a vertice:
    #   - It visits all unvisited vertices reachable from a vertice, v
    #   - It's not a DFS traversal
    #   - It uses the following class attribute "self.visited" to know whether a vertice is already visited or not
    #
    # It's iterative:
    #   - It mimics the recursive version
    #   - It uses a stack to track previous virtice visited
    #   - It puts in the stack 1 adjacent vertice at once
    #   - Each element in the stack is in the format: vertice, current adjacent index
    #   - It avoids the stack to contain twice or more the same vertice: 
    #   - E.g.,   Graph:      Stack at the end of each iteration: 
    #        A --- B --- C    I-0  |  I-1  |  I-2  |  I-3 | I-4  |  I-5  |
    #         \   /         (A, -1)|(B, -1)|(C, -1)|(B, 0)|(A, 0)|(E, -1)|
    #           E                  |(A, 0) |(B, 0) |(A, 0)|      |(A, 1) |
    #                              |       |(A, 0) |      |      |       |
    # It's kept general: 
    #   - It doesn't do any specific operation on vertices
    #   - Specific operations must be applied by traversing the 2 lists the method returns:
    #   - 1. preorder_visits list: it contains all vertices ordered by when they're previsited
    #   - 2. postorder_visits: it contains all vertices ordered by when they're postvisited
    #   - Here, it's called by "DFS traversal" and "Find Strongly Connected Components" methods
    #
    # Time Complexity: O(|V| + |E|)
    # Space Complexity: O(|V|)
    #   - Worst case: explore a linked list from its head
    #   - The stack will contain all vertices
    def explore_iterative(self, v, an_adjacency_list, preorder_visits, postorder_visits):
        
        stack = deque()
        stack.append(latest_visited_vertice_adjacent(v, -1))

        while stack:
            
            latest_v_a = stack.pop()
            v = latest_v_a.vertice
            adjacent_index = latest_v_a.adjacent_index + 1

            if adjacent_index == 0:
                self.previsit(v, preorder_visits)
            
            if adjacent_index >= len(an_adjacency_list[v]):
                self.postvisit(v, postorder_visits)
                continue
            
            stack.append(latest_visited_vertice_adjacent(v, adjacent_index))

            a = an_adjacency_list[v][adjacent_index]
            if not self.visited[a]:
                stack.append(latest_visited_vertice_adjacent(a, -1))

    def explore(self, v, an_adjacency_list, preorder_visits, postorder_visits):
        
        self.previsit(v, preorder_visits)

        for a in an_adjacency_list[v]:
            if not self.visited[a]:
                self.explore(a, an_adjacency_list, preorder_visits, postorder_visits)

        self.postvisit(v, postorder_visits)

    def dfs(self, an_adjacency_list, dfs_preorder, dfs_postorder, iterative):
        
        self.visited = [False] * self.vertices_count
        for v in range(self.vertices_count):
            if not self.visited[v]:
                if iterative:
                    self.explore_iterative(v, an_adjacency_list, dfs_preorder, dfs_postorder)
                else:
                    self.explore(v, an_adjacency_list, dfs_preorder, dfs_postorder)

    def stronly_connected_components(self, iterative):

        dfs_postorder = []

        # 1. Find postorder in Gr
        # ... Source vertices in Gr have the highest postorder
        # ... A source vertice in Gr is Sink vertice in G
        self.dfs(self.reversed_adjacency_list, None, dfs_postorder, iterative)

        # 2. Find SCCs in G
        sccs = []
        self.visited = [False] * self.vertices_count
        for i in range(len(dfs_postorder) - 1, -1, -1):
            v = dfs_postorder[i]
            if not self.visited[v]:
                sccs.append([])
                if iterative:
                    self.explore_iterative(v, self.adjacency_list, None, sccs[len(sccs) - 1])
                else:
                    self.explore(v, self.adjacency_list, None, sccs[len(sccs) - 1])

        return sccs

    def solve_2sat(self, iterative):

        strongly_connected_components = self.stronly_connected_components(iterative)
        
        # sccs is ordered in reversed topological order
        vertice_assignment = [-1] * self.vertices_count
        for scc in strongly_connected_components:
            
            scc_vertices = set()
            for v in scc:

                scc_vertices.add(v)

                non_v = self.non_vertice_num(v)
                if non_v in scc_vertices:
                    return None

                if vertice_assignment[v] == -1:
                    vertice_assignment[v] = 1
                    vertice_assignment[non_v] = 0
                    
        return vertice_assignment[:self.sat_variables_count]

# Utility class to use for DFS iterative to store in a stack
class latest_visited_vertice_adjacent:

    def __init__(self, vertice, adjacent_index):
        self.vertice = vertice
        self.adjacent_index = adjacent_index

def isSatisfiable(n, clauses, iterative):
    
    g = Implication_graph(n, clauses)
    
    return g.solve_2sat(iterative)

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
    
    #sys.setrecursionlimit(10**7)

    n, m = map(int, input().split())
    clauses = [ list(map(int, input().split())) for i in range(m) ]
    
    #result = isSatisfiable_naive(n, clauses)
    result = isSatisfiable(n, clauses, iterative=True)

    if result is None:
        print("UNSATISFIABLE")
    else:
        print("SATISFIABLE")
        print(" ".join(str(i + 1 if result[i] else -i-1) for i in range(n)))
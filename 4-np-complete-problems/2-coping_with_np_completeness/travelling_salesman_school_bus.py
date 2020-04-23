# python3
from itertools import permutations

INF = 10 ** 9

# Analysis: 
# Input data structure: a weighted graph
# ... Bus depot, children homes and the school are represented with vertices
# ... The route between each location is represented with an edge
# ... The time needed fom the bus to go from location A to B is represented with a weight on the edge (A, B)
# ... The time needed to go from a location A to B and B to A could be different
# ... If there isn't a route from a location A to B, their corresponding edge weight will be infinite (INF)
# ... We'll use a 2-D matrix to represent such a graph
# Solution: Dynamic Programming:
# ... Let's S be a subset of the graph vertices
# ... Let's w(i, j) be the weight of the edge (i, j), i, j ∈ graph vertices
# ... Let's C(S, i) the shortest path that starts from the vertice 1, ends at vertice i and visits all vertices in S
# ... C({1}, 1) = 0, C(S, 1) = INF when |S| > 1
# ... C(S, i) = Min{ C(S - {i}, j) + w(j, i)} for all j ∈ S and j != i
# Solution data structure:
# ... We'll reprensent vertices from 0 to n - 1 (the number of vertices)
# ... All possible subsets S could be represented with a number (s)
# ... If the i-th bit is equal to 1, the vertice i is included in S
# ... If the i-th bit is equal to 0, the vertice i isn't included in S
# ... E.g. n = 3:  s    bits    S            C
#                  0    0 0 0   {}          INF
#                  1    0 0 1   {0}         C({0}, 0) = 0
#                  2    0 1 0   {1}         INF because vertice (bit) 0 isn't included
#                  3    0 1 1   {0, 1}      C({0, 1}, 0) = 0)
#                  4    1 0 0   {2}
#                  5    1 0 1   {2, 0}
#                  6    1 1 0   {2, 1}
#                  7    1 1 1   {2, 1, 0}
# ... Since n < 18, an integer is enough to represent all possible susets (2**17)
# ... So, to loop on all possible vertices, we just need to loop s from 1 to 2**n - 1
def shortest_path(w, S, C):

    shortest_path_length = INF
    for i in C[S]:
        if C[S][i] + w[i][0] >= shortest_path_length:
            continue
        shortest_path_length = C[S][i] + w[i][0]

    if shortest_path_length == INF:
        return -1, []

    path_length = shortest_path_length
    shortest_path = [-1] * len(w[0])
    shortest_path[0] = 1
    
    prev_v = 0
    pos = len(w[0]) - 1
    while S > 0:
    
        for i in C[S]:
            if C[S][i] == path_length - w[i][prev_v]:
                shortest_path[pos] = i + 1

                pos -= 1
                path_length -= w[i][prev_v]
                prev_v = i
                S = S ^ (1 << i)
                
                break
        
    return shortest_path_length, shortest_path

def optimal_path(w):

    n = len(w[0])
    S = (1 << n) - 1 #2**n - 1
    
    # mapping between the vertine no and its corresponding bit position
    b = 1
    map_v_bit_position = dict()
    for i in range(n):
        map_v_bit_position[b] = i
        b *= 2

    # C(S, i)
    C = dict()
    C[1] = dict()
    C[1][0] = 0 # For S = 00001 = {0}, C({0}, 0) = 0

    for s in range(3, S + 1, 2):
        C[s] = dict()
        C_S = C[s]

        i = 1
        while i * 2 <= s: # for all vertices i in s
            i *= 2
            v_i = map_v_bit_position[i]
            
            if i & s == 0: # the vertice i isn't included in s
                continue

            C_S[v_i] = INF
            
            s_minus_i  = s ^ i

            C_S_minus_i = C[s_minus_i]
            if s_minus_i > 1: 
                # C(S, 0) = INF for |S| > 1
                C[s_minus_i][0] = INF
            
            j = 1
            while j <= s_minus_i: #for all vertices j in s (j != i):

                if s_minus_i & j == 0: # the vertice j isn't included in s_minus_i
                    j *= 2
                    continue
                
                v_j = map_v_bit_position[j]
                C_S[v_i] = min(C_S[v_i], C_S_minus_i[v_j] + w[v_j][v_i])
                j *= 2

    return shortest_path(w, S, C)

def optimal_path_naive(graph):
    # This solution tries all the possible sequences of stops.
    # It is too slow to pass the problem.
    # Implement a more efficient algorithm here.
    n = len(graph)
    best_ans = INF
    best_path = []

    for p in permutations(range(n)):
        
        cur_sum = 0
        for i in range(1, n):
            if graph[p[i - 1]][p[i]] == INF:
                break
            cur_sum += graph[p[i - 1]][p[i]]
        else:
            if graph[p[-1]][p[0]] == INF:
                continue
            cur_sum += graph[p[-1]][p[0]]
            if cur_sum < best_ans:
                best_ans = cur_sum
                best_path = list(p)

    if best_ans == INF:
        return (-1, [])
    return (best_ans, [x + 1 for x in best_path])

def print_answer(path_weight, path):
    print(path_weight)
    if path_weight == -1:
        return
    print(' '.join(map(str, path)))

def read_data():
    n, m = map(int, input().split())
    graph = [[INF] * n for _ in range(n)]
    for _ in range(m):
        u, v, weight = map(int, input().split())
        u -= 1
        v -= 1
        graph[u][v] = graph[v][u] = weight
    
    return graph



if __name__ == '__main__':
    print_answer(*optimal_path(read_data()))
    #print_answer(*optimal_path_naive(read_data()))

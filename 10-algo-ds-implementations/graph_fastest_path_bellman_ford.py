'''
    Input: G(V, E, W) a directed graph without a negative cycle, s ∈ V
        - -Infinity < We < +Infinity for any e in E
        - G MUST not have a negative cycle => min_dist(u, v) = -Infinity for any { u, v } ⊆ V
        - G does not have negative cycle => G is Directed graph
            E.g. 
                G(V, E, W) an undirected graph with 2 vertices and 1 edge with weight is negative
                min_distance(1, 2) = - Infinity
                    -1
                1 ------- 2

    Output:
        - fastest path from s to any v in V
        - fastest path distances from s to any v in V

    Question: Why Dijskra's algorithm doesn't work in this case?
           -2
        3 ---- > 4      Dijkstra(1, 4) = 2
        ^        ^      Bellman-Ford(1, 4) = 1
       3|        | 1
        1 -----> 2
            1
    
    Time & Space Complexity:
        - Time Complexity:
        - Space Complexity:

    Implementation Assumptions:
        - Zero-based numbering: Edges number starts from 0
        - Edges list is valid
            - 0 <= edge.source, edge.sink < vertices_count for any edge in edges list
            - It does not have duplicates
            - It doesn't have a negative cycle

'''
from graph_fastest_path_base import Fastest_Path_Base


class Bellman_Ford(Fastest_Path_Base):
    
    def __compute_fastest_path (self):
        pass
    


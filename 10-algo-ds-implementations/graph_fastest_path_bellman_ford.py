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
        # Initializations
        self.__parent = [ -1 for _ in range(self.__graph.vertices_count) ]
        self.__distance = [ self.__max_distance for _ in range(self.__graph.vertices_count) ]

        self.__distance[ self.__path_source_node ] = 0

        for n in range(self.__graph.vertices_count):
            for v in range(self.__graph.vertices_count):
                if self.__distance[v] != self.__max_distance:
                    for edge in self.__graph.adjacency_list[v]:
                        candidate_distance = self.__distance[v] + edge.weight
                        if self.__distance[edge.sink] > candidate_distance:
                            self.__distance[edge.sink] = candidate_distance
                            parents[edge.sink] = v
                            reachable[edge.sink] = 1
                            if n == self.__graph.vertices_count - 1:
                                q.put(a_tuple.vertex) 
    


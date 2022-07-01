import heapq
from typing import List
from .graph import Positively_Weighted_Edge

'''
    Dijkstra's Algorithm
    Input: Weighted Graph: G(V, E, W), s ∈ V
        - Undirected or Directed
        - w >= 0 for all w in W

    Output: 
        - fastest path from s to any v in V
        - fastest path distances from a to any v in V

    Assumptions:
        - Directed graph
        - Edges number starts from 0 (zero-based numbering)
        - Edges list is valid
            - 0 <= edge.source, edge.sink < vertices_count for any edge in edges list
            - It does not have duplicates
    
    Time and Space Complexity:
        - Time Complexity:
        - Space Complexity:
'''
class Dijkstra:
    def __init__(self, vertices_count: int, edges: List[Positively_Weighted_Edge], s: int):
        self.__max_distance = 10**7
        
        self.__adjacency_list = self.__build_adjacency_list(vertices_count, edges)

        self.__path_source_node = s
        self.__parents = []
        self.__distances = []
    
    def fastest_distance_to(self, v: int) -> int:
        return self.__distances[v]

    def fastest_path_to(self, v: int) -> List[int]:
        reversed_path = []
        while v != -1:
            reversed_path.append(v)
            v = self.__parents[v]
        
        return reversed_path[::-1]
    
    def __compute_fastest_path (self, v: int) -> List[int]:
        vertices_count = len(self.__adjacency_list)
        self.__parents = [ -1 for _ in range(vertices_count) ]
        self.__distances = [ self.__max_distance for _ in range(vertices_count) ]

        self.__distances[self.__path_source_node] = 0
        closest_nodes_queue = [ (0,  self.__path_source_node) ]

        while closest_nodes_queue:
            (distance, node) = heapq.heappop(closest_nodes_queue)
            
            for edge in self.__adjacency_list[node]:
                adjacent = edge.sink
                candidate_distance = distance + edge.weight
                if candidate_distance < self.__distances[ adjacent ]:
                    self.__parents[ adjacent ] = node
                    self.__distances[ adjacent ] = candidate_distance
                    heapq.heappush(closest_nodes_queue, (candidate_distance, adjacent))
    
    def __build_adjacency_list(self, vertices_count: int, edges: List[Positively_Weighted_Edge]) -> List[List[Positively_Weighted_Edge]]:
        adjacency_list = [ [] for _ in range(vertices_count) ]
        for edge in edges:
            adjacency_list[edge.source] = edge
        
        return adjacency_list
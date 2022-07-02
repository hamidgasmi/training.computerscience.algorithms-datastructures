import heapq
from typing import List
from graph import Graph_Adjacency_List

'''
    Dijkstra's Algorithm
    Input: Weighted Graph: G(V, E, W), s ∈ V
        - Undirected or Directed
        - We >= 0 for all e in E

    Output: 
        - fastest path from s to any v in V
        - fastest path distances from s to any v in V
    
    Time and Space Complexity:
        - Time Complexity: O(|V| + |E|log|E|)
            - T(Initialization) + T(Compute Min Distance) = O(|V|) + P(|E|*log|E|)
            - Dense graph (|E| = O(|V|^2)) --> T = O(|V| + |V|^2 * log|V|^2) = O(|V|^2 * log|V|)
            - Sparce graph (|E| ~ |V|)     --> T = O(|V| + |V|log|V|) = O(|V|log|V|) 
        - Space Complexity: O(|V| + |E|)
            - S(Parent list) + S(distance list) + S(Heap queue) = O(|V| + |V| + |E|) = O(|V| + |E|)
    
    Implementation Assumptions:
        - Directed graph
        - Edges number starts from 0 (zero-based numbering)
        - Edges list is valid
            - 0 <= edge.source, edge.sink < vertices_count for any edge in edges list
            - It does not have duplicates
    
'''

class Dijkstra_Heap_Queue:
    def __init__(self, graph: Graph_Adjacency_List, s: int):
        self.__max_distance = 10**7
        
        self.__graph = graph

        self.__path_source_node = s
        self.__parent = []
        self.__distance = []
    
    def fastest_distance_to(self, dest: int) -> int:
        if len(self.__distance) == 0:
            self.__compute_fastest_path()
        
        return self.__distance[dest]

    def fastest_path_to(self, dest: int) -> List[int]:
        if len(self.__distance) == 0:
            self.__compute_fastest_path()
        
        v = dest
        reversed_path = []
        while v != -1:
            reversed_path.append(v)
            v = self.__parent[v]
        
        return reversed_path[::-1]
    
    def __compute_fastest_path (self) -> List[int]:
        # Initialization
        self.__parent = [ -1 for _ in range(self.__graph.vertices_count) ]                       # O(|V|)
        self.__distance = [ self.__max_distance for _ in range(self.__graph.vertices_count) ]    # O(|V|)

        self.__distance[self.__path_source_node] = 0
        closest_nodes_queue = [ (0,  self.__path_source_node) ]

        # Computing min distance for each v in V
        while closest_nodes_queue:                                                      # T(Push to hq) + T(Pop from hq) = O(2*|E|*log|E|) = O(|E|*log|E|):
            (distance, node) = heapq.heappop(closest_nodes_queue)                       # we can pop at most |E| edges from the hq
            
            for edge in self.__graph.adjacency_list[node]:                                    
                adjacent = edge.sink
                candidate_distance = distance + edge.weight                             
                if candidate_distance < self.__distance[ adjacent ]:
                    self.__parent[ adjacent ] = node
                    self.__distance[ adjacent ] = candidate_distance
                    
                    # we can push at most |E| edges into the hq
                    heapq.heappush(closest_nodes_queue, (candidate_distance, adjacent))
                    # We could build a custom minheap that can return the position of an element in O(1).
                    # We can then change its priority in O(log|V|): heapq.changepriority(closest_nodes_queue, adjacent, candidate_distance)
                    # The heap queue will contain then at most: |V| elements (instead of |E| element as it's implemented here) 
        
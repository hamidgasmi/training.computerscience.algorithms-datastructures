'''
    Dijkstra's Algorithm
    Input: Weighted Graph: G(V, E, W), s ∈ V
        - Undirected or Directed
        - We >= 0 for all e in E

    Output: 
        - fastest path from s to any v in V
        - fastest path distances from s to any v in V
    
    Time and Space Complexity:
        - Time Complexity: O(|V|^2)
            - T(Initialization) + T(Compute Min Distance) = O(|V|) + O(|V|^2 + |E|)
            - Dense graph (|E| = O(|V|^2)) --> T = O(|V|^2 + |V|^2) = O(|V|^2)
            - Sparce graph (|E| ~ |V|)     --> T = O(|V|^2 + |V|) = O(|V|^2) 
        - Space Complexity: O(|V|)
            - S(Parent list) + S(distance list) + S(visited nodes set) = O(|V| + |V| + |V|) = O(|V|)
    
    Implementation Assumptions:
        - Directed graph
        - Edges number starts from 0 (zero-based numbering)
        - Edges list is valid
            - 0 <= edge.source, edge.sink < vertices_count for any edge in edges list
            - It does not have duplicates
    
'''
from typing import List
from graph_fastest_path_base import Fastest_Path_Base

class Dijkstra_Heap_Queue(Fastest_Path_Base):
        
    # O(|V|)
    def __get_closest_node(self, visited_nodes: set) -> int:
        closest_node = -1
        min_distance = self.__max_distance
        for candidate in range(self.__graph.vertices_count):
            if candidate not in visited_nodes and self.__distance[candidate] < min_distance:
                closest_node = candidate
                min_distance = self.__distance[candidate]
        
        return closest_node
    
    # O(|V|^2)
    def __compute_fastest_path (self):
        # Initialization
        self.__parent = [ -1 for _ in range(self.__graph.vertices_count) ]                       # O(|V|)
        self.__distance = [ self.__max_distance for _ in range(self.__graph.vertices_count) ]    # O(|V|)

        self.__distance[self.__path_source_node] = 0
        visted_nodes = set()

        # Computing min distance for each v in V
        closest_node = 0
        while closest_node != -1:                                  # |V| * T(self.__get_closest_node) + Sum(indegree(closest_node)) = |V|^2 + |E|
            distance =  self.__distance[closest_node]
            visted_nodes.add(closest_node)
            
            for edge in self.__graph.adjacency_list[closest_node]: # O(indegree(closest_node))
                adjacent = edge.sink
                candidate_distance = distance + edge.weight
                if candidate_distance < self.__distance[ adjacent ]:
                    self.__parent[ adjacent ] = closest_node
                    self.__distance[ adjacent ] = candidate_distance
            
            closest_node = self.__get_closest_node(visted_nodes)   # O(|V|)

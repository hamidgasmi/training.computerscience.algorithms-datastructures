from typing import List
from collections import namedtuple

'''
    Build Adjacency List
    Input: Eges List
    Output: 
        - Graph implemented with an adjacency list
    
    Time and Space Complexity:
        - Time Complexity: O(|E|) 
        - Space Complexity: O(|V| + |E|)
    
'''

Edge = namedtuple('Edge', ['source', 'sink', 'weight'])

class Graph_Adjacency_List:
    def __init__(self, vertices_count: int, edges: List[Edge]):
        self.vertices_count = vertices_count
        self.adjacency_list = self.__build_adjacency_list(edges) # O(|E|)
    
    def __build_adjacency_list(self, edges: List[Edge]) -> List[List[Edge]]:
        adjacency_list = [ [] for _ in range(self.__vertices_count) ]
        for edge in edges:
            adjacency_list[edge.source] = edge
        
        return adjacency_list
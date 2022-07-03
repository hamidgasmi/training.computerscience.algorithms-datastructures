from typing import List
from graph import Graph_Adjacency_List

'''
    Fastest Path base
    
    Implementation Assumptions:
        - Directed graph
        - Edges number starts from 0 (zero-based numbering)
        - Edges list is valid
            - 0 <= edge.source, edge.sink < vertices_count for any edge in edges list
            - It does not have duplicates
    
'''

class Fastest_Path_Base:
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
    
    # abstract method
    def __compute_fastest_path (self):
        pass
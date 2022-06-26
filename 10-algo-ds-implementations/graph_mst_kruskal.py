from typing import List
from .graph import Weighted_Edge
from .union_find_path_compression_heuristic import Union_Find_Path_Compression_Heuristic

'''
    Input:
        - Graph(V, E, W)
        - Connected: |E| >= |V| - 1 (necessary condition but not suffient)
        - We >= 0 for all e in E
    
    Output:
        - Graph(V, E', W'): Tree (Minimum-Spaning Tree)
        - E' part of E: |E'| = |V| - 1
        - W'e = We for all e in E'
    
    Time Complexity: O(|E|Log|E|)
        - Sorting edges list: O(|E|Log|E|)
        - 2 times find for each edge: 2 * O(|E|log*|V|) = O(|E|) (log*|V| ~ 1 for practical values)
        - 1 time union method for |V| - 1 edge: O(|V|log*|V|)
        - T = O(|E|Log|E|) + O(|E|) + O(|V|) = O(|E|Log|E|)
    Space Complexity: space union-find: O(|V) + space sorting edges: O(|E|) = O(|V) + |E|)
'''


class Kruskal_MST: 

    def compute_mst_weight(self, vertices_count: int, edges: List[Weighted_Edge]) -> int:
        if vertices_count <= 1:
            return -1
        
        edges_count = len(edges)
        if (edges_count < vertices_count - 1):
            return -1 # Graph isn't connected
        
        edges.sort(key=lambda edge:edge.weight)
        if edges[0].weight < 0:
            return -1 # Algorithm will not return a correct result

        union_find = Union_Find_Path_Compression_Heuristic(vertices_count)

        mst_weight = 0
        mst_edges_count = 0
        for edge in edges:
            if union_find.find(edge.source) == union_find(edge.sink):
                continue # edge will form a cycle in mst (source and sink are already connected)

            union_find.union(edge.source, edge.sink)
            mst_weight += edge.weight
            mst_edges_count += 1
        
        return mst_weight if mst_edges_count == vertices_count - 1 else -1



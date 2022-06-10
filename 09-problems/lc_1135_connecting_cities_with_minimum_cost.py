class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        minimum_edges_count = n - 1
        if len(connections) < minimum_edges_count:
            return - 1
        
        connections.sort(key=lambda edge:edge[2])
        
        union_find = Union_Find_Path_Compression_Heuristic(n)
        
        path_total_cost = 0
        mst_edges_count = 0
        for [ a, b, cost ] in connections:
            node_a = a - 1
            node_b = b - 1
            
            if union_find.find(node_a) == union_find.find(node_b):
                continue
            
            mst_edges_count += 1
            path_total_cost += cost
            union_find.union(node_a, node_b)
        
        return path_total_cost if mst_edges_count == minimum_edges_count else -1

class Union_Find_Path_Compression_Heuristic:
    def __init__(self, n: int):
        self.__rank = [ 0 for _ in range(n) ]
        self.__parent = [ i for i in range(n) ]
    
    # Time Complexity: O(logn)
    def find(self, i: int) -> int:
        if i < 0 or i >= len(self.__parent):
            return -1

        if i != self.__parent[i]:
            self.__parent[i] = self.find(self.__parent[i])
        
        return self.__parent[i]
    
    # Time Complexity: O(logn)
    def union(self, i: int, j: int):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i == root_j:
            return
        
        if self.__rank[root_i] > self.__rank[root_j]:
            # We choose root_i as the root of the merged tree
            self.__parent[root_j] = root_i
         
        else:
            # We choose root_j as the root of the merged tree
            self.__parent[root_i] = root_j
            if self.__rank[root_i] == self.__rank[root_j]:
                self.__rank[root_j] += 1
        
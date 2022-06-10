
class Union_Find_Rank_Heuristic:
    def __init__(self, n: int):
        self.__rank = [ 0 for _ in range(n) ]
        self.__parent = [ i for i in range(n) ]
    
    # Time Complexity: O(logn)
    def find(self, i: int) -> int:
        if i < 0 or i >= len(self.__parent):
            return -1
        
        root_i = i
        while root_i != self.__parent[root_i]:
            root_i = self.__parent[root_i]
        
        return root_i
    
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
        
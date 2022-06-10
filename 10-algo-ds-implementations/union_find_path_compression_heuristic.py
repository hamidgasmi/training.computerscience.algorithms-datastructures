
class Union_Find_Path_Compression_Heuristic:
    def __init__(self, n: int):
        self.__rank = [ 0 for _ in range(n) ]
        self.__parent = [ i for i in range(n) ]
    
    # Time Complexity: O(log*n)
    def find(self, i: int) -> int:
        if i < 0 or i >= len(self.__parent):
            return -1

        if i != self.__parent[i]:
            self.__parent[i] = self.find(self.__parent[i])
        
        return self.__parent[i]
    
    # Time Complexity: O(log*n)
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
        
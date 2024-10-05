"""
    1. Problem Summary / Clarifications / TDD:
        Parent :   -1   0   0   1   1   2   2
        Node no:    0   1   2   3   4   5   6
                 0
               /   \
              1     2
             / \   / \
            3   4 5   6

"""
class TreeAncestorNaive1:
    def __init__(self, n: int, parent: List[int]):
        
        self.parent = parent
    
    def getKthAncestor(self, node: int, k: int) -> int:
        if not k:
            return node
        
        elif not node:
            return -1
        
        else:
            return self.getKthAncestor(self.parent[node], k - 1)

class TreeAncestorNaive2:
    """
    2. Inuition:
        - Use a list to store all ancestors for each node: __ancestors
        - The kth ancestor of node k will be stored in: __ancestors[node][k - 1]

    3. Implementation:
    4. Tests:

    5. Complexity Analysis:
        Time Complexity:
            - Constructor: O(1)
            - Get kth ancestor: O(n^2)
                - Worst case (the tree looks like a linked list): O(n^2) = O(1 + 2 + 3 + ... + n) = O((n + 1) * n/2)
                - Best case (the tree is balanced): O(logn^2) = O(1 + 2 + 3 + ... + logn) = O((logn + 1) * logn/2)
        Space Complexity:
            - Constructor: O(1)
            - Get kth ancestor: O(n^2)
                - Worst case (the tree looks like a linked list): O(n^2) = O(1 + 2 + 3 + ... + n) = O((n + 1) * n/2)
                - Best case (the tree is balanced): O(logn^2) = O(1 + 2 + 3 + ... + logn) = O((logn + 1) * logn/2)

    """
    def __init__(self, n: int, parent: List[int]):
        
        self.parent = parent
        
        self.__ancestors = {0:[]}
    
    def getKthAncestor(self, node: int, k: int) -> int:
        if node not in self.__ancestors:
            self.__find_all_ancestors(node)
        
        return self.__ancestors[node][k - 1] if k <= len(self.__ancestors[node]) else -1
    
    def __find_all_ancestors(self, node: int):
        if node in self.__ancestors:
            return
        
        parent = self.parent[node]
        self.__ancestors[node] = [parent]
        
        self.__find_all_ancestors(parent)
        self.__ancestors[node].extend(self.__ancestors[parent])


"""
    1. Problem Summary / Clarifications / TDD:
        0   1   2   3   4   5   6
        parents
            0   0   1   1   2   2 
                    0   0   0   0

"""
class TreeAncestorNaiveOptimized:

    def __init__(self, n: int, parent: List[int]):
        
        self.parent = parent
        
        self.ancestors = {0:[]}
    
    def getKthAncestor(self, node: int, k: int) -> int:
        if node in self.ancestors:
            ancestors_len = len(self.ancestors[node])
            if k <= ancestors_len:
                return self.ancestors[node][k - 1]
                        
            elif not node or not self.ancestors[node][-1]:
                return -1
            
            else:
                ancestor = self.ancestors[node][-1]
        
        else:
            ancestor = self.parent[node]
            self.ancestors[node] = [ancestor]
            ancestors_len = 1
        
        if k - ancestors_len:
            self.getKthAncestor(ancestor, k - ancestors_len)
            for p in range(ancestors_len - 1):
                parent = self.ancestors[node][p]
                self.ancestors[parent].extend(self.ancestors[ancestor])
            self.ancestors[node].extend(self.ancestors[ancestor])
        
        return self.ancestors[node][k - 1] if k <= len(self.ancestors[node]) else -1

class TreeAncestorBinaryLifting:
    def __init__(self, n: int, parent: List[int]):
        pass
    
    def getKthAncestor(self, node: int, k: int) -> int:
        pass

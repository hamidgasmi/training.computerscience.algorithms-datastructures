"""
    1. Problem Summary / Clarifications / TDD:
    
        E.g.1. n = 3, k = 1
               k = 1 123
               k = 2 132
               k = 3 2 1 3
               
    2. Intuition:
          
            1         2
          2   3
        3    2
"""

class Solution:
    
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    def getPermutation(self, n: int, k: int) -> str:
        
        path_set = set()
        
        permutation = []
        len_permutation = n
                
        while len(permutation) != len_permutation:
            
            # 1. Find the position of the digit
            pos = 1
            fact_n_minus_1 = math.factorial(n - 1)
            while k > fact_n_minus_1 and pos <= fact_n_minus_1:
                k -= fact_n_minus_1
                pos += 1
            
            # 2. Find the corresponding digit at position: pos without including digits that are already in Permutation
            i = 0
            while pos:
                i += 1
                if i in path_set:
                    continue
                    
                pos -= 1
            
            # 3. Add the digit into permutation
            permutation.append(chr(i + 48))
            path_set.add(i)
            
            # 4. Go to the next level
            n -= 1
        
        return ''.join(permutation)
    
class SolutionBacktracking:
    
    # Time Complexity: O((n - 1)!)
    # Space Complexity: O(n)
    def get_permutation(self, n: int, k: int) -> str:
        
        fact_n = math.factorial(n - 1)
        
        start = 1
        while k > fact_n:
            k -= fact_n
            start += 1
            
        (_, path) = self.__kth_permutation(n, k, start, [], set())
            
        return ''.join([ str(i) for i in path ])
    
    def _kth_permutation(self, n, k, start, path, path_set):
        
        if len(path) == n:
            return (0, path) if k - 1 == 0 else (k - 1, [])
        
        permutations_count = 0
        for i in range(start, n + 1):
            
            if i in path_set:
                continue
            
            path_set.add(i)
            (k, result) = self._kth_permutation(n, k, 1, path + [i], path_set)
            path_set.remove(i)
            
            if result:
                return (0, result)
        
        return (k, [])
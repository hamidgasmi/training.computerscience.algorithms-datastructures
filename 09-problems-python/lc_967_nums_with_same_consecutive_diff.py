"""
    1. Problem Summary / Clarifications / TDD:
        Output(N = 3, K = 7): [181,292,707,818,929]
        Output(N = 3, K = 3): [147,141,258,252,369,363,303,474,414,585,525,696,636,630,747,741,858,852,969,963]
        Output(N = 2, K = 1): [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
        
    2. Intuition:
               1..9 
               / \
              4   6
        - It's a forest of binary trees of height N - 1:
        - The forest roots value is from 1 to 9
        - Solution2: DFS, BFS

    3. Implementation
    4. Tests:
        Edge Cases:
            Output(N = 1, K = X): [0,1,2,3,4,5,6,7,8,9]
            Output(N = 2, K = 0): [11,22,33,44,55,66,77,88,99]

    5. Complexity Analysis:
        - N > 1
        - Each binary tree has a max height of N
        - Each binary tree has at most 2^N-1 paths (from root to leaves): potential candidates
        - Each binary tree has at most 1 + 2 + ... + 2^N-1 = 2^N - 1 nodes
        - The forest has at most 9 * (2^N - 1) nodes and 9 * 2^N-1 paths (results)
        - So our solution could have at most 9 * 2^N-1 numbers

"""

class Solution_DFS:
    """
       Time Complexity:
            - O(1) if N = 1
            - O(N) if K = 0
            - O(9 * (2^N - 1)) = O(2^N)
        Space Complexity:
            - O(1) if N = 1
            - Recursion space + results: O(N) + O(9 * 2^N-1) = O(2^N)
    """
    def nums_same_consec_diff(self, N: int, K: int) -> List[int]:
        if N == 1:
            return [i for i in range(10)]
        
        results = []
        for n in range(1, 10):
            self._nums_same_consec_diff_dfs(N - 1, K, results, n)
            
        return results
    
    def _nums_same_consec_diff_dfs(self, N, K, results, num):
        if not N:
            results.append(num)
            return
        
        tail_digit = num % 10
        num *= 10
        N -= 1
        
        if tail_digit + K < 10:
            self._nums_same_consec_diff(N, K, results, num + tail_digit + K)
            
        if K and tail_digit - K >= 0:
            self._nums_same_consec_diff(N, K, results, num + tail_digit - K)

class Solution_BFS:
    """
       Time Complexity:
            - O(1) if N = 1
            - O(N) if K = 0
            - O(9 * (2^N - 1)) = O(2^N)
        Space Complexity:
            - O(1) if N = 1
            - results: O(9 * 2^N-1) = O(2^N)
        
    """

    def nums_same_consec_diff(self, N: int, K: int) -> List[int]:
        if N == 1:
            return [i for i in range(10)]
        
        results = []
        for n in range(1, 10):
            results.extend(self._nums_same_consec_diff_bfs(N-1, K, n))
        
        return results
    
    def _nums_same_consec_diff_bfs(self, N, K, num):
        
        curr_level = [num]
        while N:
            next_level = []
            for n in curr_level:
                tail_digit = n % 10
                n *= 10
                
                if K and tail_digit - K >= 0:
                    next_level.append(n + tail_digit - K)
                
                if tail_digit + K < 10:
                    next_level.append(n + tail_digit + K)
            
            curr_level = next_level
            N -= 1
        
        return curr_level
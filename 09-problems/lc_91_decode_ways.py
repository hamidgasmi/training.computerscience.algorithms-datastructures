
class SolutionRecursive:
    """
    Intuition:
        - Backtracking + memoization
    
    Complexity Analysis:
        Time Complexity: O(N)
        Space Complexity: O(N)
    
    """
    def num_decodings(self, s: str) -> int:

        memo = {}
        return self.backtrack(s, 0, memo)

    def backtrack(self, s: str, idx: int, memo: dict) -> int:
        
        len_s = len(s)
        if idx == len_s:
            return 1
        
        elif s[idx] == '0':
            return 0

        elif idx in memo:
            return memo[idx]        
                
        decoding_count = self.backtrack(s, idx + 1, memo)
        if idx + 1 < len_s and int(s[idx: idx + 2]) < 27:
            decoding_count += self.backtrack(s, idx + 2, memo)
        
        memo[idx] = decoding_count
        
        return decoding_count
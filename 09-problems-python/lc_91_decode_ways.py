"""
    1. Problem Summary / Clarifications / TDD:
        num_decodings('0') = 0
        num_decodings('1') = 1
        num_decodings('10') = 1
        num_decodings('20') = 1
        num_decodings('12') = 2
        num_decodings('226') = 3
        num_decodings("2101") = 1
        num_decodings("111111111111111111111111111111111111111111111") = 1836311903

"""


class SolutionRecursive:
    """
    2. Intuition:
        - Backtracking + memoization
    
    3. Complexity Analysis:
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

class SolutionDP:
    """
    2. Intuition:
        - Dynamic Programming
        - dp[0] = 0
        - dp[1] = 0 if s[0] = '0' else 1
        - dp[i] = dp[i - 2] if s[i - 1] = '0' and s[i - 2] in ('1', '2')
        - dp[i] = dp[i - 1] if s[i - 1] != '0'
                + dp[i - 2] if <= s[i - 2: i] < 27)
    
    3. Complexity Analysis:
        Time Complexity: O(N)
        Space Complexity: O(N)

    """
    def num_decodings(self, s: str) -> int:
        len_dp = len(s) + 1
        
        dp = [1, 0 if s[0] == '0' else 1]
        for i in range(2, len_dp):
            
            s_curr_idx = i - 1
            
            dp.append(0)
            dp[i] = 0 if s[s_curr_idx] == '0' else dp[i - 1]
            dp[i] += dp[i - 2] if 9 < int(s[s_curr_idx - 1: s_curr_idx + 1]) < 27 else 0              
        
        return dp[len_dp - 1]

class SolutionDPOptimized:
    """
    2. Intuition:
        - Dynamic Programming
        - dp[0] = 0
        - dp[1] = 0 if s[0] = '0' else 1
        - dp[i] = dp[i - 2] if s[i - 1] = '0' and s[i - 2] in ('1', '2')
        - dp[i] = dp[i - 1] if s[i - 1] != '0'
                + dp[i - 2] if <= s[i - 2: i] < 27)
    
    3. Complexity Analysis:
        Time Complexity: O(N)
        Space Complexity: O(1)

    """
    def num_decodings(self, s: str) -> int:
        
        prev = 1
        curr = 0 if s[0] == '0' else 1
        for i in range(2, len(s) + 1):
            
            next_ = 0 if s[i - 1] == '0' else curr
            next_ += prev if 9 < int(s[i - 2: i]) < 27 else 0
            
            prev = curr
            curr = next_
        
        return curr
"""
    1. Problem Summary / Clarifications / TDD:
        num_decodings('0') = 0
        num_decodings('1') = 1
        num_decodings('*') = 9
        num_decodings('10') = 1
        num_decodings('20') = 1
        num_decodings('12') = 2
        num_decodings('10*') = 1
        num_decodings('20*') = 1
        num_decodings('12*') = 2
        num_decodings('226') = 3
        num_decodings('22*6') = 28
        num_decodings('22*7') = 26
        num_decodings("2101") = 1
        num_decodings("2*101") = 15
        num_decodings("21*01") = 4
        num_decodings("111111111111111111111111111111111111111111111") = 836311896
        num_decodings("*********************************************") = 506269638

"""

class SolutionDP:
    """
    2. Intuition:
        - Dynamic Programming
    
    3. Complexity Analysis:
        Time Complexity: O(N)
        Space Complexity: O(N)

    """
    def __init__(self):
        self.mod = 10**9 + 7
        
    def numDecodings_(self, s: str) -> int:
        
        len_dp = len(s) + 1
        dp = [0 for _ in range(len_dp)]
        dp[0] = 1
        dp[1] = (0 if s[0] == '0' else (9 if s[0] == '*' else 1))
        for i in range(2, len_dp):
            s_idx = i - 1
            
            if s[s_idx] == '0':
                if s[s_idx - 1] in ('1', '2'):
                    dp[i] = dp[i - 2]
                
                elif s[s_idx - 1] == '*':
                    dp[i] = 2 * dp[i - 2]
                    
            elif s[s_idx] == '*':
                dp[i] = 9 * dp[i - 1]
                
                if s[s_idx - 1].isdigit():
                    if s[s_idx - 1] == '1':
                        dp[i] += 9 * dp[i - 2]
                        
                    elif s[s_idx - 1] == '2':
                        dp[i] += 6 * dp[i - 2]
                    
                elif s[s_idx - 1] == '*':
                    dp[i] += 9 * dp[i - 2]
                    dp[i] += 6 * dp[i - 2]
                
            else:
                dp[i] = dp[i - 1]
                
                if s[s_idx - 1].isdigit() and 9 < int(s[s_idx - 1:s_idx + 1]) < 27:
                    dp[i] += dp[i - 2]
                    
                elif s[s_idx - 1] == '*':
                    dp[i] += 2 * dp[i - 2] if s[s_idx] < '7' else dp[i - 2]
            
            dp[i] %= self.mod       
        
        return dp[-1]

class SolutionDPOptimized:
    """
    2. Intuition:
        - Dynamic Programming
        - We just need 2 previous values => get rid of dp list
    
    3. Complexity Analysis:
        Time Complexity: O(N)
        Space Complexity: O(1)

    """
    def __init__(self):
        self.mod = 10**9 + 7
    
    def num_decodings(self, s: str) -> int:
                
        prev = 1
        curr = (0 if s[0] == '0' else (9 if s[0] == '*' else 1))
        for i in range(1, len(s)):
                        
            next_ = 0
            
            if s[i] == '0':
                next_ = prev if s[i - 1] in '12' else 2 * prev if s[i - 1] == '*' else 0
                    
            elif s[i] == '*':
                next_ += 9 * curr
                next_ += 9 * prev if s[i - 1] in '1*' else 0
                next_ += 6 * prev if s[i - 1] in '2*' else 0
                
            else:
                next_ = curr
                
                if s[i - 1] == '*':
                    next_ += 2 * prev if s[i] < '7' else prev
                    
                elif 9 < int(s[i - 1:i + 1]) < 27:
                    next_ += prev                    
            
            next_ %= self.mod
            
            prev, curr = curr, next_
        
        return curr
"""
    1. Problem Summary / Clarifications / TDD:
        output("abcd", "abecd") = "e"
                
    2. Inuition: xor operator

    3. Tests:
        output("abcd", "abecd") = "e": The added character is in the middle of t
        output("abcd", "abcde") = "e": The added character is at the end of t
        output("abcd", "eabcd") = "e": The added character is at the beginning of t

        Specific case
        output("aaa", "aaaa")   = "a"

        Edge case: s is empty
        output("", "a")         = "a"

    3. Complexity Analysis:
        Time Complexity: O(|t|)
        Space Complexity: O(1)       
    
"""
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        xor_result = 0
        for i in range(len(s)):
            xor_result ^= ord(s[i])
            xor_result ^= ord(t[i])
        xor_result ^= ord(t[-1])
        
        return chr(xor_result)
        
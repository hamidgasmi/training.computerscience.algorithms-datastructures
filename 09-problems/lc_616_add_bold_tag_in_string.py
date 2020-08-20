"""
    1. Problem Summary / Clarifications / TDD:
        - Do the words in Dict have the same length? No
        - Are there special characters? No
    
    2. Intuition:
        1. Find all intervals indexes [start, end] where dict words are in s
        2. Merge all intervals above
        3. Insert bold tags

    3. Implementation
        - Solution 1: uses naive string search
        - Solution 2: uses Knuth-Morris-Pratt to string search
    4. Tests:
    5. Complexity Analysis:
       Time Complexity:
       Space Compexity:

"""
class Solution:
    
    def __init__(self, pattern_maching=None):
        self._start, self._end = 0, 1

        self.__pattern_matching = pattern_maching if pattern_maching else NaivePatternMatch()
    
    def add_bold_tag(self, s: str, dict: [str]) -> str:
        
        # O(|s|^2) time, O(|s|) space
        intervals = self._search_words(s, dict)
        if not intervals:
            return s
        
        # O(|s|log|s|) time, O(|s|) space
        intervals = self._merge_intervals(intervals)
        
        # O(|s|) time, O(|s|) space
        bolded_s = []
        prev_interval_end = -1
        for interval in intervals:
            
            bolded_s.append(s[prev_interval_end+1:interval[self._start]])
            
            bolded_s.append('<b>')
            bolded_s.append(s[interval[self._start]:interval[self._end]+1])
            bolded_s.append('</b>')
            
            prev_interval_end = interval[self._end]
        bolded_s.append(s[intervals[-1][self._end]+1:])

        # O(|s|) time, O(1) space
        return ''.join(bolded_s)

    def _search_words(self, s: str, dict_: [str]) -> [[int, int]]:
        intervals = []
        for word in dict_:
            
            word_len = len(word)
            
            matching_positions = self.__pattern_matching.get_exact_matching_positions(s, word)
            for start_pos in matching_positions:
                intervals.append([start_pos, start_pos + word_len - 1])
        
        return intervals
    
    # Time Complexity: O(IlogI)
    # Space Complexity: O(I)
    def _merge_intervals(self, intervals: [[int, int]]) -> [[int, int]]:
        
        # 1. Sort by interval.start
        intervals.sort(key=lambda i:i[0])
        
        # 2. Merge
        merged_intervals = []
        for interval in intervals:
            if merged_intervals and interval[self._start] - 1 <= merged_intervals[-1][self._end]:
                merged_intervals[-1][self._end] = max(merged_intervals[-1][self._end], interval[self._end])
            
            else:
                merged_intervals.append(interval)
        
        return merged_intervals

class NaivePatternMatching:
    # Time Complexity:  O(|s|^2)
    #   |s| + |s| - 1 + ... 1 = |s|(|s| - 1) // 2
    # Space Complexity: O(|s|)
    def get_exact_matching_positions(self, s: str, p: str) -> [int]:
        
        matching_positions = []

        l = 0
        while p in s:
            idx = s.index(p) 
            l += idx

            matching_positions.append(l)
            l += 1
            s = s[idx + 1:]
        
        return matching_positions

import math
import random
class RabinKarpPatternMatching:
    def __init__(self):
        self.__prime = 1009
        self.__multiplier = random.randint(1, self.__prime - 1)

    def get_exact_matching_positions(self, s: str, p: str) -> [int]:
        
        len_p = len(p)
        len_s = len(s)
        if len_p > len_s:
            return []
        
        p_hash = self.__get_hash(p)
        s_window_hash = self.__get_hash(s, 0, len(p) - 1)
        #print('->', self.__multiplier, p, s_window_hash)
        multiplier_powred = int(math.pow(self.__multiplier, len_p - 1)) % self.__prime

        matching_positions = [0] if s_window_hash == p_hash and s[:len_p] == p else []
        for i in range(len_p, len_s):
            s_window_hash -= (ord(s[i - len(p)]) - ord('a') + 1)
            s_window_hash //= self.__multiplier
            s_window_hash += (ord(s[i]) - ord('a') + 1) * multiplier_powred
            s_window_hash %= self.__prime
            
            if s_window_hash == p_hash and s[i-len_p+1:i+1] == p:
                matching_positions.append(i-len_p+1)
            #print(i, p_hash, s_window_hash, s[i-len_p+1:i+1], p, matching_positions)

        return matching_positions

    def __get_hash(self, t:str, l=0, r=None) -> int:
        if r is None:
            r = len(t) - 1

        hash = 0
        for i in range(r, l-1, -1):
            hash = (hash * self.__multiplier + ord(t[i]) - ord('a') + 1) % self.__prime
        
        return hash

class KnuthMorrisPrattPatternMatching:
    """ 
        Knuth-Morris-Pratt algorithm to search a pattern in a text:
        Time Complexity: O(|s| + |p|)
        Space Complexity: O(|s| + |p|)
    """

    # Time Complexity:  O(|s| + |words|)
    # Space Complexity: O(|s|)
    def get_exact_matching_positions(self, s: str, p: str) -> [int]:
        
        len_p = len(p)
        len_s = len(s)
        if len_p > len_s:
            return []
        
        ps = [p[i] for i in range(len(p))] + ['$'] + [s[i] for i in range(len(s))]
        prefix_func = self.__prefix_function(ps)

        matching_positions = []
        for i in range(len_p + 1, len_p + len_s):
            if prefix_func[i] == len_p:
                matching_positions.append(i - 2 * len_p)

        return matching_positions
    
    # Time Complexity: O(|ps|)
    # Space Complexity: O(|ps|)
    def __prefix_function(self, ps:str) -> [int]:
        
        len_ps = len(ps)

        prefix_func = [0 for _ in range(len_ps)]
        border = 0
        for i in range(1, len_ps):
            while border and ps[i] != ps[border]:
                border = prefix_func[border - 1]

            if ps[i] == ps[border]:
                border += 1

            else:
                border = 0
            prefix_func[i] = border

        return prefix_func

if __name__ == '__main__':
    
    # Test 1
    solution = Solution(NaivePatternMatching())
    print(solution.add_bold_tag('abcxyz123', ['b','c','x','1','2']))
    
    solution = Solution(RabinKarpPatternMatching())
    print(solution.add_bold_tag('abcxyz123', ['b','c','x','1','2']))
    
    solution = Solution(KnuthMorrisPrattPatternMatching())
    print(solution.add_bold_tag('abcxyz123', ['b','c','x','1','2']))

    # Test 2:
    solution = Solution(NaivePatternMatching())
    print(solution.add_bold_tag('aabcd', ['ab','bc']))
    
    solution = Solution(RabinKarpPatternMatching())
    print(solution.add_bold_tag('aabcd', ["ab","bc"]))
    
    solution = Solution(KnuthMorrisPrattPatternMatching())
    print(solution.add_bold_tag('aabcd', ["ab","bc"]))


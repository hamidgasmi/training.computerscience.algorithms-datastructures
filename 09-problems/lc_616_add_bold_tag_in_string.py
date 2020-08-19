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

class Solution_1:
    """
        Time Complexity: O(|s|^2)
        Space Complexity: O(|s|)
    """
    def __init__(self):
        self._start, self._end = 0, 1
    
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
        return ''.join(bolded_str)

    # Time Complexity:  O(|s|^2)
    #   |s| + |s| - 1 + ... 1 = |s|(|s| - 1) // 2
    # Space Complexity: O(|s|)
    def _search_words(self, s: str, dict: [str]) -> [[int, int]]:
        intervals = []
        for word in dict:
            l = 0
            suffix = s
            word_len = len(word)
            while l <= len(s) - word_len and word in suffix:
                idx = suffix.index(word) 
                l += idx
                
                intervals.append([l, l+word_len-1])
                l += 1
                suffix = suffix[idx + 1:]
        
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

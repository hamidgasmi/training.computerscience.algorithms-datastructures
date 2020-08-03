class Solution:
    
    # Time Complexity: O(|s|)
    # Space Complexity: O(1)
    def length_longest_substring_two_distinct(self, s: str) -> int:
        if not s:
            return 0
        
        next_l = l = 0
        max_sub_str_len = 1
        distinct_c_set = {s[0]}
        for r in range(1, len(s)):
            
            if s[r] in distinct_c_set:
                
                max_sub_str_len = max(max_sub_str_len, r - l + 1)
                
            elif len(distinct_c_set) < 2:
                
                distinct_c_set.add(s[r])
                    
                max_sub_str_len = max(max_sub_str_len, r - l + 1)
                    
            else:
                
                max_sub_str_len = max(max_sub_str_len, r - l)
                l = next_l
                    
                distinct_c_set.clear()
                distinct_c_set.add(s[r-1])
                distinct_c_set.add(s[r])
            
            next_l = next_l if s[r] == s[r - 1] else r
        
        return max_sub_str_len
            
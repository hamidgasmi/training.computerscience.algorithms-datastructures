class Solution:
    """
    I. Clarifications:
       1. The problem doesn't mention a z axis to compute a volume
       2. The problem consists of returning the max area: let's call is max_area
       3. Let's call the height at position i: h(i)
       3. Let's call The area between between 2 positions: l and r: area(l, r) l < r
       4. We have then area(l, r) = (r - l) * min[h(l), h(r)]

    II. Intuition: Greedy algorithm:
        1. Greedy Choice: 
            - Compute surface with l-th and r-th vertical bars: initially (l,r) = (0, n-1)
            - Scenario 1: h(l) < h(r): l++
            - Scenario 2: h(l) > h(r): r--
            - Scenario 3: h(l) = h(r): l++ and r--
        2. The choice is Safe? Yes. Let's prove it by contradiction.
            - Scenario 1: h(l) < h(r) => area(l, r) = (r - l) * h(l)
                Let's assume that there's a position i (l < i < r) such that max_area = area(l, i) = (i - l) * min[h(l), h(i)]
                This means that: max_area > area(l, r) <=> (i - l) * min[h(l), h(i)] > (r - l) * h(l)
                But this is a contradiction since: min[h(l), h(i)] <= h(i) and (i - l) < (r - l) (because l < i < r)

            - Scenario 2: same proof

            - Scenario 3: h(l) = h(r) => area(l, r) = (r - l) * h(l) = (r - l) * h(r)
                Let's assume that there's a position i such that max_area = area(l, i) or max_area = area(i,r) 
                if max_area = area(l, i), follow scenario 1 proof
                if max_area = area(i, r), follow scenario 2 proof
        
    III. Implementation:
        1. Time Analysis: O(|height|)
        2. Space Analysis: O(1)
    
    """

    def maxArea(self, height: List[int]) -> int:
        
        n = len(height)
        
        l = 0
        r = n - 1
        
        max_surface = 0
        while l < r:
            
            curr_surface = (r - l) * min(height[r], height[l])
            
            if height[l] == height[r]:
                l += 1
                r -= 1
            
            elif height[l] > height[r]:
                r -= 1
                
            else:
                l += 1
            
            if curr_surface > max_surface:
                max_surface = curr_surface
                
        return max_surface    
    
    # Time Complexity: O(|height|**2)
    # Space Complexity: O(1)
    def _maxArea_naive(self, height: List[int]) -> int:
        
        n = len(height)
        
        max_surface = 0
        for i in range(n):
            for j in range(i + 1, n):
                
                curr_surface = (j - i) * min(height[i], height[j])
                if curr_surface > max_surface:
                    max_surface = curr_surface
                    
        return max_surface
    
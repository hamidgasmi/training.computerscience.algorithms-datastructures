"""
    1. Problem Summary / Clarifications / TDD:
        [[1,12],[2,9],[3,10],[13,14],[15,16],[16,17]]
        
    2. Inuition:
        |------||----------||----|
        
        |------|
           |--|
            |----------|
                 |----|
            
"""

class Solution_1:
    """
        - Use hash table to store intervals initial positions
        - Sort by interval start
        - Modified Binary search that will return the min interval which start is greater than a value

        Complexity Analysis:
            - Time Complexity: O(nlogn)
            - Space Complexity: O(n)
    """
    
    def find_right_interval(self, intervals: List[List[int]]) -> List[int]:
        
        start, end = 0, 1
        len_intervals = len(intervals)
        
        # 1. Keep track of initial intervals positions
        intervals_pos = {}
        for i in range(len_intervals):
            intervals_pos[intervals[i][start]] = i
        
        # 2. Sort intervals by interval start
        intervals.sort(key=lambda i:i[start])
        
        # 3. Find the minimum right interval for each 
        right_intervals = [-1 for _ in range(len_intervals)]
        for i in range(len_intervals):
            
            curr_start = intervals[i][start]
            curr_pos = intervals_pos[curr_start]
            
            right_interval = self._binary_search(intervals, intervals[i][end], i + 1, len_intervals - 1)
            
            if right_interval >= 0:
                right_interval_start = intervals[right_interval][start]
                right_intervals[curr_pos] = intervals_pos[right_interval_start]
        
        return right_intervals
    
    def _binary_search(self, intervals, val, l, r):
        
        ans = -1
        while l <= r:
            mid = (l + r) // 2
            
            if val <= intervals[mid][0]:
                ans = mid
                r = mid - 1
                
            else:
                l = mid + 1
                
        return ans

class Solution_2:
    """
        - Use hash table to store intervals initial positions
        - Store all start and end points in points array
        - Sort points arrays
        - Scan each point
            - If there is an interval starting from point, store it for later
            - If there is an interval ending in point, set the minimum interval for all interval starting before point (found step 1)
        Complexity Analysis:
            - Time Complexity: O(nlogn)
            - Space Complexity: O(n)
    """
    def find_right_interval(self, intervals: List[List[int]]) -> List[int]:
        start, end = 0, 1
        len_intervals = len(intervals)
        
        # 1. Store intervals by their start and end
        start_intervals_pos = {}
        end_intervals_pos = {}
        points = []
        for i in range(len_intervals):
            
            interval = intervals[i]
            
            if not interval[start] in start_intervals_pos and not interval[start] in end_intervals_pos:
                points.append(interval[start]) # avoid inserting duplicates in points
            start_intervals_pos[interval[start]] = i
            
            if not interval[end] in start_intervals_pos and not interval[end] in end_intervals_pos:
                points.append(interval[end])  # avoid inserting duplicates in points
            
            if not interval[end] in end_intervals_pos:
                end_intervals_pos[interval[end]] = []
            end_intervals_pos[interval[end]].append(i)
        
        # 2. Sort points
        points.sort()
        
        # 3. Find the minimum right interval for each:
        right_intervals = [-1 for _ in range(len_intervals)]
        
        left_intervals = []
        for p in points:
            
            # If there intervals ending at p, keep track of them in left intervals
            if p in end_intervals_pos:
                left_intervals.extend(end_intervals_pos[p])
            
            # If there are intervals starting at p, then set up right interval for all intervals store in left intervals
            if not p in start_intervals_pos:
                continue

            for l in left_intervals:
                right_intervals[l] = start_intervals_pos[p]
            left_intervals = []
        
        return right_intervals

class Solution_3:
    """
        Complexity Analysis:
            - Time Complexity: O(n^2)
            - Space Complexity: O(n)
    """ 
    def find_right_interval(self, intervals: List[List[int]]) -> List[int]:
        
        start, end = 0, 1
        len_intervals = len(intervals)
        
        intervals_pos = {}
        for i in range(len_intervals):
            intervals_pos[intervals[i][start]] = i
        
        intervals.sort(key=lambda i:i[start])
        
        right_intervals = [-1 for _ in range(len_intervals)]
        
        for i in range(len_intervals):
            
            for j in range(i+1, len_intervals):
                if intervals[i][end] <= intervals[j][start]:
                    curr_start = intervals[i][start]
                    curr_pos = intervals_pos[curr_start]
                    
                    next_start = intervals[j][start]
                    
                    right_intervals[curr_pos] = intervals_pos[next_start]
                    
                    break
        
        return right_intervals
    
class Solution_4:
    """
        - Naive solution
        Complexity Analysis:
            - Time Complexity: O(n^2)
            - Space Complexity: O(n)
    """ 
    def find_right_interval(self, intervals: List[List[int]]) -> List[int]:
        
        start, end = 0, 1
        len_intervals = len(intervals)
        
        right_intervals = [-1 for _ in range(len_intervals)]
        for i in range(len_intervals):
            
            for j in range(len_intervals):
                if i == j:
                    continue
                
                if intervals[i][end] > intervals[j][start]:
                    continue
                
                prev_right_interval = right_intervals[i]
                
                if prev_right_interval == -1 or intervals[prev_right_interval][start] > intervals[j][start]:
                    right_intervals[i] = j
        
        return right_intervals
        
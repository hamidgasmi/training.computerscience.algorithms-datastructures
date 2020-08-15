"""
    1. Problem Summary / Clarifications / TDD:
        insert([[1,3],[6,9]], [0,0]) = [[0,0],[1,3],[6,9]]
        insert([[1,3],[6,9]], [0,1]) = [[0,3],[6,9]]
        insert([[1,3],[6,9]], [0,5]) = [[0,5],[6,9]]
        insert([[1,3],[6,9]], [3,5]) = [[0,5],[6,9]]
        insert([[1,3],[6,9]], [3,6]) = [[0,9]]
        insert([[1,3],[6,9]], [4,5]) = [[1,3],[4,5],[6,9]]
        insert([[1,3],[6,9]], [4,6]) = [[1,9]]
        insert([[1,3],[6,9]], [0,10]) = [[0,10]]
        insert([[1,3],[6,9]], [10,11]) = [[1,3],[6,9],[10,11]]

"""

class BinarySearchSolutions:
    """
        2. Intuition:
        - Binary Search: find the intervals new_interval overlap with : insert_start=i, insert_end=j :
  	          Intervals:               |---0---| ... |--i-1--||---i---|  ... |---j---||--j+1--|  ... |---n---| 
  	       new_interval:                                           |--------------|
        - Update new_interval :
  	          Intervals:              |---0---| ... |--i-1--||---i---|  ... |---j---||--j+1--|  ... |---n---| 
  	       new_interval:                                     |----------------------|
  	    - Return [0 : i[ + new_interval + ]j : n] :
  							          |---0---| ... |--i-1--||----------------------||--j+1--|  ... |---n---| 

        3. Implementations:
            - Solution 1: Modify the input intervals by replacing all overlapping intervals with new_interval
            - Solution 2: Create a new merged_intervals list

        4. Complexity Analysis:
            - Let's n be the length of the input list intervals
            - Let's m be the length of the output list
            - Solution 1:
                - The input is modified and returned
                - Space Complexity: O(1): in Place
                - Time Complexity: O(n)
                - It requires to delete fromintervalsall overlapping intervals
            - Solution 2:
                - A new list is returned
                - Space Complexity:O(m)
                - Time Complexity:Θ(max(logn, m)) = O(n)(here n is an upper-bound only)
                - The worst case time complexity is O(n): when for example new_interval doesn't overlap with any interval in intervals
                - The best case time complexity is O(logn): when new_interval overlaps whith the majority of intervals, more than: n - logn
                - In practice, this solution is faster than solution 1

    """
    def __init__(self):
        self._start, self._end = 0, 1
    
    # Solution 1:
    def insert_1(self, intervals, new_interval):
        
        intervals_count = len(intervals)
        
        # 1. Search in intervals where new_interval.start fits in: O(logn) time
        insert_pos_start = self._binary_search(intervals, new_interval[self._start], 0, intervals_count - 1)
        if insert_pos_start < intervals_count and intervals[insert_pos_start][self._start] <= new_interval[self._start] <= intervals[insert_pos_start][self._end]:
            new_interval[self._start] = intervals[insert_pos_start][self._start]
            new_interval[self._end] = max(intervals[insert_pos_start][self._end], new_interval[self._end])        
        
        # 2. Search in intervals where new_interval.end fits in: O(logn) time
        insert_pos_end = self._binary_search(intervals, new_interval[self._end], insert_pos_start, intervals_count - 1)
        if insert_pos_end < intervals_count and intervals[insert_pos_end][self._start] <= new_interval[self._end]:
            new_interval[self._end] = max(intervals[insert_pos_end][self._end], new_interval[self._end])
            insert_pos_end += 1
        
        # 3. Replace overlapping intervals with new_interval: O(n) time and O(1) space
        intervals[insert_pos_start:insert_pos_end] = [new_interval]
        
        return intervals
    
    # Solution 2:
    def insert_2(self, intervals, new_interval):
        
        intervals_count = len(intervals)
        
        # 1. Search in intervals where new_interval.start fits in: O(logn) time
        insert_pos_start = self._binary_search(intervals, new_interval[self._start])
        if insert_pos_start < intervals_count and intervals[insert_pos_start][self._start] <= new_interval[self._start] <= intervals[insert_pos_start][self._end]:
            new_interval[self._start] = intervals[insert_pos_start][self._start]
            new_interval[self._end] = max(intervals[insert_pos_start][self._end], new_interval[self._end])        
        
        # 2. Search in intervals where new_interval.end fits in: O(logn) time
        insert_pos_end = self._binary_search(intervals, new_interval[self._end], insert_pos_start)
        if insert_pos_end < intervals_count and intervals[insert_pos_end][self._start] <= new_interval[self._end]:
            new_interval[self._end] = max(intervals[insert_pos_end][self._end], new_interval[self._end])
            insert_pos_end += 1
        
        # 3. Create new merged_intervals list: O(n) time in worst case and O(n) space
        merged_intervals = intervals[:insert_start]       # Insert all intervals before insert_start
        merged_intervals.append(new_interval)             # Insert new_interval
        merged_intervals.extend(intervals[insert_end:])   # Insert all intervals after insert_end
        
        return merged_intervals

    def _binary_search(self, intervals, val, l=0, r=None):
        if r is None:
            r = len(intervals) - 1
        
        while l <= r:
            mid = (l + r) // 2
            if intervals[mid][self._start] <= val <= intervals[mid][self._end]:
                return mid
            
            elif val > intervals[mid][self._end]:
                l = mid + 1
                
            else:
                r = mid - 1
        
        return l

class Solution3:
    """
    2. Intuition: Merge Interval technique
        - Insert all interval which interval.start < new_interval.start
        - Insert or Merge new Intervals
        - Insert or Merge all following intervals interval.start > new_interval.start
    
    4. Complexity Analysis:
        - Time Complexity: O(n)
        - Space Complexity: O(n)
    
    """

    def __init__(self):
        self._start, self._end = 0, 1

    def insert_3(self, intervals, new_interval):
        
        merged_intervals = []

        intervals_count = len(intervals)
        
        i = 0
        while i < intervals_count and intervals[i][self._start] <= new_interval[self._start]:
            new_intervals.append(intervals[i])
            i += 1
        
        if not new_intervals or new_intervals[-1][self._end] < new_interval[self._start]:
            new_intervals.append(new_interval)
                
        else:
            new_intervals[-1][self._end] = max(new_intervals[-1][self._end], new_interval[self._end])
        
        for j in range(i, intervals_count):
            if new_intervals[-1][self._end] < intervals[j][self._start]:
                new_intervals.append(intervals[j])
                
            else:
                new_intervals[-1][self._end] = max(new_intervals[-1][self._end], intervals[j][self._end])
        
        return new_intervals
        
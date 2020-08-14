class SolutionBinarySearch:
    
    def __init__(self):
        self._start, self._end = 0, 1
    
    # Time Complexity:  O(n)
    # Space Complexity: O(1)
    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        
        intervals_count = len(intervals)
        
        insert_pos_start = self._binary_search(intervals, new_interval[self._start], 0, intervals_count - 1)
        if insert_pos_start < intervals_count and intervals[insert_pos_start][self._start] <= new_interval[self._start] <= intervals[insert_pos_start][self._end]:
            new_interval[self._start] = intervals[insert_pos_start][self._start]
            new_interval[self._end] = max(intervals[insert_pos_start][self._end], new_interval[self._end])        
        
        insert_pos_end = self._binary_search(intervals, new_interval[self._end], insert_pos_start, intervals_count - 1)
        if insert_pos_end < intervals_count and intervals[insert_pos_end][self._start] <= new_interval[self._end]:
            new_interval[self._end] = max(intervals[insert_pos_end][self._end], new_interval[self._end])
            insert_pos_end += 1
        
        intervals[insert_pos_start:insert_pos_end] = [new_interval]
           
        return intervals
    
    def _binary_search(self, intervals: List[List[int]], val, l, r):
        
        while l <= r:
            mid = (l + r) // 2
            if intervals[mid][self._start] <= val <= intervals[mid][self._end]:
                return mid
            
            elif val > intervals[mid][self._end]:
                l = mid + 1
                
            else:
                r = mid - 1
        
        return l

class SolutionInPlace:
    
    def __init__(self):
        self._start, self._end = 0, 1

    # Time Complexity:  O(n)
    # Space Complexity: O(1)
    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        
        intervals_count = len(intervals)
        
        insert_pos_start = -1
        while insert_pos_start + 1 < intervals_count and intervals[insert_pos_start + 1][self._start] <= new_interval[self._start]:
            insert_pos_start += 1
        if 0 <= insert_pos_start < intervals_count and intervals[insert_pos_start][self._end] >= new_interval[self._start]:
            new_interval[start] = intervals[insert_pos_start][self._start]
            new_interval[end] = max(intervals[insert_pos_start][self._end], new_interval[self._end])
        
        else:
            insert_pos_start += 1
        
        insert_pos_end = insert_pos_start
        while insert_pos_end + 1 < intervals_count and intervals[insert_pos_end + 1][start] <= new_interval[end]:
            insert_pos_end += 1
        if 0 <= insert_pos_end < intervals_count and intervals[insert_pos_end][start] <= new_interval[end]:
            new_interval[end] = max(intervals[insert_pos_end][end], new_interval[end])
            insert_pos_end += 1
        
        intervals[max(0, insert_pos_start):max(0,insert_pos_end)] = [new_interval]
           
        return intervals

class Solution3:
    
    def __init__(self):
        self._start, self._end = 0, 1

    # Time Complexity:  O(n)
    # Space Complexity: O(n)
    def _insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        
        intervals_count = len(intervals)
        
        new_intervals = []
        
        start, end = 0, 1
        
        i = 0
        while i < intervals_count and intervals[i][start] <= new_interval[start]:
            new_intervals.append(intervals[i])
            i += 1
        
        
        if not new_intervals or new_intervals[-1][end] < new_interval[start]:
            new_intervals.append(new_interval)
                
        else:
            new_intervals[-1][end] = max(new_intervals[-1][end], new_interval[end])
        
        for j in range(i, intervals_count):
            if new_intervals[-1][end] < intervals[j][start]:
                new_intervals.append(intervals[j])
                
            else:
                new_intervals[-1][end] = max(new_intervals[-1][end], intervals[j][end])
        
        return new_intervals
        
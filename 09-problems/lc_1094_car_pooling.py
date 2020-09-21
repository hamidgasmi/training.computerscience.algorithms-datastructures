class SolutionCumulativeSum:
    """
    2. Intuition:
        - Store the nbr of the passengers picked or dropped off by time
        - Compute the cumulative sum by time and check if it exceeds the capacity
    
    3. Complexity Analysis:
        - Time Complexity: O(N)
        - Space Complexity: O(N)

    """
    
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        count_idx, start_idx, end_idx = 0, 1, 2
        
        passengers_count_change_by_time = [0 for _ in range(1001)]
        for trip in trips:
            passengers_count_change_by_time[trip[start_idx]] += trip[count_idx]
            passengers_count_change_by_time[trip[end_idx]] -= trip[count_idx]
        
        for passenger_count in passengers_count_change_by_time:
            capacity -= passenger_count
            if capacity < 0:
                return False
        
        return True

import heapq
class SolutionHeap:
    """
    2. Intuition:
        - Sort the trips by start time
        - Loop on each trip:
            - Store in a heap current trips
            - Dequeue all trip which end time is less current trip start time and update capacity
            - If current trip passengers nbr > capacity: return False
            - Else: update capacity and loop
    
    3. Complexity Analysis:
        - Time Complexity: O(NlogN)
        - Space Complexity: O(N)

    """
    
    def carPooling_heap(self, trips: List[List[int]], capacity: int) -> bool:
        
        count_idx, start_idx, end_idx = 0, 1, 2
        trips.sort(key = lambda t: t[start_idx])
        
        heap = []
        for trip in trips:
            
            while heap and heap[0][0] <= trip[start_idx]:
                capacity += heap[0][1]
                heapq.heappop(heap)
                
            if trip[count_idx] > capacity:
                return False
            
            capacity -= trip[count_idx]
            heapq.heappush(heap, (trip[end_idx], trip[count_idx]))
            
        return True       
        
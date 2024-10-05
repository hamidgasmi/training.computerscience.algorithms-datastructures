"""
    1. Problem Summary / Clarifications / TDD:
      [[1,4,3], [2,5,4], [7,9,6]]:       7
      [[6,7,10], [2,4,11], [8,12,15]]:  15
      [[1,4,2], [2,4,1], [3,6,5]]:       8
Output: 8

    2. Intuition:
        1. Store store current end time and current load
        2. Compute current load: current load + curr_job.cpu_load - all previous job cpu load which job.end < curr_job.start
        3. Compute the max cpu load

    3. Implementation:
    4. Tests:
        Edge case 1: []:                 0
        Edge case 2: [[0,2,3]]:          3
        Edge case 3: [[0,2,3],[0,2,3]]:  6
        Spacial case: [[0,20,3],[1,21,3],[2,22,3],[3,23,3]]: 12
        Cases above

    5: Complexity Analysis:
        Time Complexity: O(nlogn) because of the sorting and heappush/heappop
        Space Complexity: O(n) when max(jobs.start.values) < min(jobs.end.values)

"""
import heapq

class Solution:
    def __init__(self):
        self._start = 0
        self._end = 1
        self._cpu_load = 2

    def find_max_cpu_load(self, jobs):

        # 1. Sort all job by job start time
        jobs.sort(key=lambda job: job[self._start])

        job_end_time_heap = []
        
        # 2. Compute cpu max load
        cpu_max_load = 0
        cpu_curr_load = 0
        for job in jobs:
            # 2.1. Deduce all previous job cpu loads
            while job_end_time_heap and job[self._start] > job_end_time_heap[0][0]:
                cpu_curr_load -= job_end_time_heap[0][1]
                heapq.heappop(job_end_time_heap)
            
            # 2.2. Add current job cpu load
            cpu_curr_load += job[self._cpu_load]
            # 2.3. Push current job cpu load
            heapq.heappush(job_end_time_heap, (job[self._end], job[self._cpu_load]))
            
            cpu_max_load = max(cpu_max_load, cpu_curr_load) 

        return cpu_max_load

if __name__ == '__main__':

    max_cpu_load_solution = Solution()

    # Edge Cases:
    print('[]: ', max_cpu_load_solution.find_max_cpu_load([]))
    print('[[0,2,3]]: ', max_cpu_load_solution.find_max_cpu_load([[0,2,3]]))
    print('[[0,2,3],[0,2,3]]: ', max_cpu_load_solution.find_max_cpu_load([[0,2,3],[0,2,3]]))

    # Spacial Cases:
    print('[[0,20,3],[1,21,3],[2,22,3],[3,23,3]]: ', max_cpu_load_solution.find_max_cpu_load([[0,20,3],[1,21,3],[2,22,3],[3,23,3]]))
        
    # Test Cases:
    print('[[1,4,3],[2,5,4],[7,9,6]]: ', max_cpu_load_solution.find_max_cpu_load([[1,4,3],[2,5,4],[7,9,6]]))
    print('[[6,7,10],[2,4,11],[8,12,15]]: ', max_cpu_load_solution.find_max_cpu_load([[6,7,10],[2,4,11],[8,12,15]]))
    print('[[1,4,2],[2,4,1],[3,6,5]]: ', max_cpu_load_solution.find_max_cpu_load([[1,4,2],[2,4,1],[3,6,5]]))

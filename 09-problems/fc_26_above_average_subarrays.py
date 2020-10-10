""" Issue: #293

    1. Problem Summary / Clarifications / TDD:
         above_average_subarrays([3, 4, 2]) = [[1, 2], [1, 3], [2, 2]]
    
    2. Intuition:
        - Naive:
            - Scan all possible subarrays and check its average with remaining average
            - 2 nested loops
            - Time Complexity: O(n^2)
            - 2 pointers approach
            3, 4, 2
            ^         sum = 3 (avg. 3) >= next_sum = 6 (next avg. 3)
            ^  ^      sum = 7 (avg. 3.5) >= next_sum = 2 (next avg. 2)  => append([0,1])
            ^     ^   sum = 9 (avg. 3) >= next_sum = 0 (next avg. 0)    => append([0,2])
               ^
        - We could do better:
            - I don't see how to improve it
    
    3. Implementation: See below
    4. Tests: See below
    5. Complexity Analysis:
       Time Complexity: O(N^2)
       Space Compexity: O(1) without including the output
                        O(N) with including the output

"""

class Solution:

    def above_average_subarrays(self, A:[int]) -> [[int]]:
        N = len(A)

        curr_elements_sum, remaining_elements_sum = 0, sum(A)

        subarrays = []
        for l in range(N):

            for r in range(l, N):
                curr_elements_sum += A[r]
                remaining_elements_sum -= A[r]
                
                curr_elements_count = r - l + 1
                remaining_elements_count = N - curr_elements_count
                remaining_elements_avg = (remaining_elements_sum / remaining_elements_count  if remaining_elements_count else 0)
                if curr_elements_sum / curr_elements_count > remaining_elements_avg:
                    subarrays.append([l + 1, r + 1])
            
            remaining_elements_sum += curr_elements_sum
            curr_elements_sum = 0

        return subarrays

if __name__ == '__main__':

    print(Solution().above_average_subarrays([1]))
    print(Solution().above_average_subarrays([3, 4, 2]))
    print(Solution().above_average_subarrays([1, 1, 1]))
    print(Solution().above_average_subarrays([3, 1, 5, 4, 2]))
    print(Solution().above_average_subarrays([2, 6, 4, 3, 1, 5]))
    print(Solution().above_average_subarrays([1, 5, 6, 4, 3, 2]))
    
"""
    1. Problem Summary / Clarifications / TDD:

"""

"""
    1. Problem Summary / Clarifications / TDD:
    
    2. Intuition:
        - Naive:
        - We could do better:

    3. Implementation
    4. Tests:
    5. Complexity Analysis:
       - Time Complexity:
       - Space Compexity:
    6. Advanced discussion:
        - Scalability
"""

"""
    1. Problem Summary / Clarifications / TDD:
        - Can we assume that the input can fit in memory
    2. Intuition:
        - Naive:
        - We could do better:
    3. Implementation
    4. Tests:
    5. Complexity Analysis:
       - Time Complexity:
       - Space Compexity:
    6. Advanced discussion:
        - Scalability (Input Size ? Memory? Disk ? Distributed Machine?)
"""
class Solution:
    def __init__(self):
        pass

    def solve(self):
        pass

if __name__ == "__main__":

    s = Solution()
    print(s.solve())

"""
Recursive solution time/space complexity analysis template:

depth         Nbr of problem           work at corresponding depth
  0             1                        O(N) #divide expression
  1             2                        O(1) + O(N - 2) = O(N) * 2
  ...
  i             2^i                      O(N) * 2^i 
  ...
  N//2          2^N//2                   O(N) * 2^N//2

Total time complexity: O(N) (2^0 + 2^1 + ... + 2^N//2) = O(N * 2^N//2) = O(N * 2^N)
Total space complexity: O(N/2 * space allocated in every call)


"""
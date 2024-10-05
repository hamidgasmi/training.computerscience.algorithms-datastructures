"""
    1. Problem Summary / Clarifications / TDD:
       [-1, -1, 3, 4, 5]       
       [-1, 2, 3], k=3
       [-1, -1, 4], k=3       

    2. Inuition:
        - Solution 1:
            - Add all elements of nums to a set
            - Loop on positive numbers, 
                - If a positive number isn't the set, add it as a missing number
                - Leave when k missing numbers are found
        - Solution 2:
            - Step 1: Remove negative numbers:
                - Keep in the array only positive numbers: if nums[i] <= 0, nums[i] = -1
                - If nums[i] > n: no action
                - If 1 <= nums[i] <= n: move the value to the position nums[i] - 1: value 1 will be put at position 0
                - So, if the array contains only positive integers from 1 to n, at the end of this step, the array should be sorted: 1, 2, 3, 4, 5
            - Step 2: Find all missing numbers:
                - Find all missing numbers between 1 and n: stop when k missing numbers are found
                - Find all missing numbers greater than n:
                    - Scan number > n, if it's not already in nums, add it as a missing number
                    - instead of checking in num, it's better to check in a set

    3. Implementation
    
"""

class Solution_1:
    """
        4. Complexity Analysis:
            Time Complexity: O(n + k)
            Space Complexity: O(n)
    """
    def find_first_k_missing_positive(self, nums, k):
        
        positive_nbrs = set()
        for n in nums:
            if n > 0 and n not in positive_nbrs:
                positive_nbrs.add(n)

        missing_numbers = []

        n = 1
        while k:
            if n not in positive_nbrs:
                missing_numbers.append(n)
                k -= 1

            n += 1
        
        return missing_numbers

class Solution_2:

    def find_first_k_missing_positive(self, nums, k):

        n = len(nums)
        
        # 1. Get rid of negative numbers
        # 2. Move elements to their positions
        i = 0
        while i < n:
            j = nums[i] - 1

            if nums[i] <= 0:
                nums[i] = -1
                i += 1

            elif nums[i] > n:
                i += 1

            elif nums[i] == i + 1:
                i += 1

            elif nums[i] == nums[j]: 
                nums[i] = -1
                i += 1

            else:
                nums[i], nums[j] = nums[j], nums[i]

        # 3. Find missing numbers from 1 to n
        # 4. Keep track of all array values > n
        missingNumbers = []
        greater_numbers_set = set()
        for i in range(n):
            if nums[i] != i + 1:
                missingNumbers.append(i+1)
                k -= 1

                if not k:
                    break
                    
                if nums[i] > n and nums[i] not in greater_numbers_set:
                    greater_numbers_set.add(nums[i])

        # 5. Find remaining missing numbers greater to k:
        i = n + 1
        while k:
            if i not in greater_numbers_set:
                missingNumbers.append(i)
                k -= 1

            i += 1

        return missingNumbers

if __name__ == '__main__':

    print('Solution 1:')
    print('[3, -1, 4, 5, 5], 3: ', Solution_1().find_first_k_missing_positive([3, -1, 4, 5, 5], 3))
    print('[2, 3, 4], 3       : ', Solution_1().find_first_k_missing_positive([2, 3, 4], 3))
    print('[-2, -3, 4], 2     : ', Solution_1().find_first_k_missing_positive([-2, -3, 4], 2))
    print('[], 3              : ', Solution_1().find_first_k_missing_positive([], 3))
    print('[3], 3             : ', Solution_1().find_first_k_missing_positive([3], 3))

    print('Solution 2:')
    print('[3, -1, 4, 5, 5], 3: ', Solution_2().find_first_k_missing_positive([3, -1, 4, 5, 5], 3))
    print('[2, 3, 4], 3       : ', Solution_2().find_first_k_missing_positive([2, 3, 4], 3))
    print('[-2, -3, 4], 2     : ', Solution_2().find_first_k_missing_positive([-2, -3, 4], 2))
    print('[], 3              : ', Solution_2().find_first_k_missing_positive([], 3))
    print('[3], 3             : ', Solution_2().find_first_k_missing_positive([3], 3))

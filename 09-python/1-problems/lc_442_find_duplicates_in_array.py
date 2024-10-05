"""
    1. Problem Summary / Clarifications / TDD:
        Output([4,3,2,7,8,2,3,1]) = [2, 3]
        Output([4,5,6,6,7,7,8,8]) = [6, 7, 8]
        Output([1,2,3,4,5,6,7,8]) = []

        Edges cases:
        Output([])      = []
        Output([1])     = []
        Output([1,2])   = []
        Output([1,1])   = [1]
        
    2. Intuition:
        
        - Naive solution with a set data-structure: it's in an inplace algorithm.

        - In place solution:
            - Xor pattern won't work because we could have many duplicates (more than 2)
            - Sum pattern won't work because we could have more than 1 duplicate
            - Rearanging the array so each item value (val) will be in its corresponding cell: nums[val - 1]

            Indices: 0   1   2   3   4   5   6   7
             Values: 4   3   2   7   8   2   3   1
            Iter. 1: 4   3   2   7   8   2   3   1
        
    3. Complexity Analaysis:
        - Time Complexity: O(n)
        - Space Complexity: O(n)
        
"""

class Solution:

    """
    2. Intuition:

        - In place solution:
            - Xor pattern won't work because we could have many duplicates (more than 2)
            - Sum pattern won't work because we could have more than 1 duplicate
            - Rearanging the array so each item value (val) will be in its corresponding cell: nums[val - 1]

            Indices: 0   1   2   3   4   5   6   7  duplicates: []
             Values: 4   3   2   7   8   2   3   1  duplicates: []
            Iter. 1: 7   3   2   4   8   2   3   1  duplicates: []
                     3   3   2   4   8   2   7   1  duplicates: []
                     2   3   3   4   8   2   7   1  duplicates: []
                     3   2   3   4   8   2   7   1  duplicates: []
                    -1   2   3   4   8   2   7   1  duplicates: [3]
            Iter. 2:-1   2   3   4   8   2   7   1  duplicates: [3]
            Iter. 3:-1   2   3   4   8   2   7   1  duplicates: [3]
            Iter. 4:-1   2   3   4   8   2   7   1  duplicates: [3]
            Iter. 5:-1   2   3   4   1   2   7   8  duplicates: [3]
                     1   2   3   4  -1   2   7   8  duplicates: [3]
            Iter. 6: 1   2   3   4  -1  -1   7   8  duplicates: [3, 2]
            Iter. 7: 1   2   3   4  -1  -1   7   8  duplicates: [3, 2]
            Iter. 8: 1   2   3   4  -1  -1   7   8  duplicates: [3, 2]
        
    3. Complexity Analaysis:
        - Time Complexity: O(|nums|)
        - Space Complexity: O(1)
        
    """
    def find_duplicates(self, nums: List[int]) -> List[int]:
        
        duplicates = []
        for i in range(len(nums)):
            
            while nums[i] not in (-1, i + 1):
                
                j = nums[i] - 1
                if nums[j] == nums[i]:
                    duplicates.append(nums[i])
                    nums[i] = -1
                    
                else:
                    nums[i], nums[j] = nums[j], nums[i]
            
        return duplicates

class Solution_Set:
    """
    2. Intuition: 
        - Use a hash set data-structure to store already seen values
    
    3. Complexity Analaysis:
        - Time Complexity: O(|nums|)
        - Space Complexity: O(|nums|)
    
    """
    def find_duplicates(self, nums: List[int]) -> List[int]:
        
        seen_set = set()
        duplicates = []
        for n in nums:
            
            if n in seen_set:
                duplicates.append(n)
                
            else:
                seen_set.add(n)
        
        return duplicates
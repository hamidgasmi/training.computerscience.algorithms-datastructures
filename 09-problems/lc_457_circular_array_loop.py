"""
    1. Problem Summary / Clarifications / TDD:
        [0,-1,1,2,2]: True
        [-2,1,-1,-2,-2]: False
        [1]: False
        [-1]: False
        [-1,2]: False
    
    2. Intuition:
        - Scan all cells of the array
        - For each cell i, use Fast-Slow pointer to check if there is a cycle or not
        - For each cell i that doesn't have a cycle, mark visited (nums[j] = 0) all cells that belong to the path starting from cell i
    
    3. Complexity Analysis:
        - Time Complexity: O(|nums|)
            - Each cell is visited at most twice:
            - 1st. To check if there is a cycle or not
            - 2nd. to mark it as visited
        
        - Space Complexity: O(1)
    
"""
class Solution:
    
    def circularArrayLoop(self, nums: List[int]) -> bool:
        
        for i in range(len(nums)):
            
            if self._visited(nums, i):
                continue
            
            direction = nums[i] > 0
            
            # 1. Check if there is a cycle starting from i
            slow = fast = i
            while True:
                if self._visited(nums, slow) or self._visited(nums, fast): # already visited
                    break
                    
                slow = self._next(nums, slow, direction)
                fast = self._next(nums, self._next(nums, fast, direction), direction)
                
                if slow == -1 or fast == -1:
                    break
                
                elif slow == fast:
                    return True
            
            # 2. Mark visited all cells that belong to the path starting from i
            slow = i
            while self._next(nums, slow, direction) != -1:
                nums[slow], slow = 0, self._next(nums, slow, direction)
            
        return False
    
    def _visited(self, nums, i):
        return not nums[i]
    
    def _next(self, nums, idx, direction):
        
        if idx == -1: # To handle the case of next(next(fast)) = next(-1) = -1
            return -1
                
        elif (nums[idx] > 0) != direction: # check the direction
            return -1
        
        next_idx = (idx + nums[idx]) % len(nums)
        if next_idx < 0:
            next_idx += len(nums)
        
        return -1 if next_idx == idx else next_idx
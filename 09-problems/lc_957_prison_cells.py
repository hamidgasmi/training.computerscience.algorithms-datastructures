class Solution:
    """
    calls[i] = 1 if cells[i - 1] == cell[i+1]
    cells[i] = 0
    Approach:
      1. Find the operation that will let me know go from day d to day d+1
      2. loop until I get cycle or I get to N (64 possible combinations)
      3. loop again N mod cycle
      
    """
    # There're 2**6 states: 65 + 1 (the initial one)
    # Time Analysis: O(2**6) = O(1)
    # Space Complexity: O(1)
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        
        if N == 0:
            return cells

        # 1. Convert the list to bitmap
        cells_state = self._convert_list_bitmap(cells)
        
        # 2. State at Day 1
        cells_state = self.next_state(cells_state)
        N -= 1
        
        # 3. Find the cycle
        cycle = 0
        initial_state = cells_state
        while N:
            
            N -= 1
            cycle += 1
            cells_state = self.next_state(cells_state)
            if cells_state == initial_state:
                break
        
        # 4. If N too small, then stop
        if N == 0:
            self._convert_int_to_list(cells_state, cells)
            return cells
        
        # 5. loop at most cycle - 1 times
        for _ in range(N % cycle):
            cells_state = self.next_state(cells_state)
        
        # 6. Convert the bitmap to list
        self._convert_int_to_list(cells_state, cells)
        return cells
        
    def next_state(self, cells_state: int) -> int:
        
        return ( (~(cells_state << 1)) ^ cells_state >> 1) & 0x007e
        
    def _convert_list_bitmap(self, cells: List[int]) -> int:
        
        cells_state = 0
        for cell in cells:
            cells_state <<= 1
            cells_state |= cell
        
        return cells_state
    
    def _convert_int_to_list(self, cells_state, cells: List[int]):
                
        for i in range(7, -1, -1):
            cells[i] = cells_state & 1
            cells_state >>= 1
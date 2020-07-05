class Solution_3:
    """
        It optimized the previous solution
    """
    
    def hammingDistance(self, x: int, y: int) -> int:
        
        # 1. Find x's and y's bits that are different
        x ^= y
        
        # 2. Count the number of 1
        bit_1_count = 0
        while x != 0:
            bit_1_count += 1
            
            x &= (x - 1)
        
        return bit_1_count

class Solution_2:
    """
        1st. It finds all the different bits from x and y by using Xor operator on x and y
        2nd. It computes the numbers of "1" in the resulted number

    """
    
    def hammingDistance(self, x: int, y: int) -> int:
        
        # 1. Find x's and y's bits that are different
        x ^= y
        
        # 2. Count the number of 1
        bit_1_count = 0
        while x != 0:
            
            bit_1_count += (x & 1)
            
            x >>= 1
        
        return bit_1_count

class Solution_1:
    """
        This solution checks every bit if they're equal or not by using the Xor operator

        Comment: we don't need to Xor for every bit

    """
    # Time Analysis: O(1)
    # Space Analysis: O(1)
    def hammingDistance(self, x: int, y: int) -> int:
        
        different_bits_count = 0
        for _ in range(32):
            
            different_bits_count += (x & 1) ^ (y & 1)
            
            x >>= 1
            y >>= 1
        
        return different_bits_count
# Analysis: 
    # I. Addition of 2 bits:
    #   a b   sum_no_carry    carry   actual sum
    #   0 0        0            0        00       
    #   0 1        1            0        01
    #   1 0        1            0        01
    #   1 1        0            1        10      
    #   sum_no_carry = a (~b) + (~a) b = a^b
    #   carry = a & b
    #   Actual sum = sum_no_carry + (carry << 1)
    #   E.g. 3 + 1:
    #     1. 0b0011 + 0b0001: sum_no_carry = 0010; carry = 0001
    #     2. 0b0010 + (0b0001 << 1) = 0b0010 + 0b0010 => sum_no_carry = 0b0000; carry = 0b0010
    #     3. 0b0000 + (0b0010 << 1) = 0b0000 + 0b0100 => sum_no_carry = 0b0100; carry = 0b0000
    #     4. carry == 0: STOP
    #
    # II. What if a and b are negative:
    #   E.g. (-3) + (-1) = 0b1101 + 0b1111
    #     1. 0b1101 + 0b1111: sum_no_carry = 0b0010; carry = 0b1101
    #     2. 0b00010 + 0b11010: sum_no_carry = 0b11000; carry = 0b00010
    #     3. 0b11000 + 0b00100: sum_no_carry = 0b11100; carry = 0b00000
    #     4. carry = 0b00000: STOP
    #
    # III. What if one number is negative: b < 0 and |a| > |b| 
    #   E.g. (+3) + (-1) = 0b0011 + 0b1111
    #     1. 0b000011 + 0b111111: sum_no_carry = 0b111100; carry = 0b000011
    #     2. 0b111100 + 0b000110: sum_no_carry = 0b111010; carry = 0b000100
    #     3. 0b111010 + 0b001000: sum_no_carry = 0b110010; carry = 0b001000
    #     4. 0b110010 + 0b010000: sum_no_carry = 0b100010; carry = 0b010000
    #        ... we should continue until we reach 31st bit
    #     32.
    #     33. STOP
    #
    # IV. What if one number is negative: b < 0 and |a| < |b| 
    #   E.g. (+1) + (-3) = 0b00001 + 0b11101
    # V. Edge cases: Overflow issues:
    #    Python integer type size is: 32 bits but Python doesn't limit integers to 32 bits
    #    Integers range: [-2**31 - 2*31 - 1] = [-2147483648, +2147483647] = [0x80000000, 0x7fffffff]
    #    We need to make sure that our numbers don't exceed 32 bits: we'll use a mask: 0xffffffff
    #    What if our result > max positive integer (0x7fffffff): we should get its complement 2: 
    #       Solution 1: ~result + 1
    #       Solution 2: ~(a ^ 0xffffffff) = ~(a ^ mask) = ~ (a.(~mask) + (~a).mask) = ~(0 + ~a) = a
    #                   The only change here is the sign

class Solution:
    
    # Time Complexity: O(32) = O(1)
    # Space Complexity: O(1)
    def get_sum(self, a: int, b: int) -> int:
                
        mask = 0x0ffffffff
        for _ in range(32):
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
                        
            if b == 0:
                break
        
        return a if a <= 0x7fffffff else ~(a ^ mask)
        
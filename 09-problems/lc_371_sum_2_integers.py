class Solution:
    
    def get_sum(self, a: int, b: int) -> int:

        # 1. Addition between 2 positive integer
        while b != 0:
            a, b = (a ^ b), ((a & b) << 1)

        # 2. Addition between 2 negative integer: To
        #   sum = - (|a| + |b|)

        # 3. 2 integers with different signs:
             
        return a
        
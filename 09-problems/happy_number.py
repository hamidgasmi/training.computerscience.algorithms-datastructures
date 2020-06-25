
class Happy_Number:

    # Time Complexity: O(|cycle|)
    # Space Complexity: O(1)
    def is_happy(self, n: int) -> bool:

        slow_n = n
        fast_n = self._get_next(n)

        while slow_n != fast_n:
            slow_n = self._get_next(slow_n)
            fast_n = self._get_next(self._get_next(fast_n))

        return True if slow_n == 1 else False

    def _get_next(self, n: int) -> int:
        
        next_n = 0
        while n != 0:
            
            next_n += (n % 10)**2
            n //= 10
        
        return next_n
    
    # Time Complexity: O(|cycle|)
    # Space Complexity: O(|cycle|)
    def is_happy_naive(self, n: int) -> bool:
        
        cycle = set()
        
        next_n = n
        while not next_n in cycle:
            
            n = next_n
            cycle.add(n)

            next_n = self._get_next(n)
            
        return True if next_n == 1 else False

if __name__ == '__main__':

    happy_number = Happy_Number()

    #print(0, happy_number.is_happy_naive(0))
    #print(1, happy_number.is_happy_naive(1))
    #print(2, happy_number.is_happy_naive(2))
    #print(10, happy_number.is_happy_naive(10))
    #print(20, happy_number.is_happy_naive(20))
    #print(19, happy_number.is_happy_naive(19))
    #print(91, happy_number.is_happy_naive(91))

    print(0, happy_number.is_happy(0))
    print(1, happy_number.is_happy(1))
    print(2, happy_number.is_happy(2))
    print(10, happy_number.is_happy(10))
    print(20, happy_number.is_happy(20))
    print(19, happy_number.is_happy(19))
    print(91, happy_number.is_happy(91))

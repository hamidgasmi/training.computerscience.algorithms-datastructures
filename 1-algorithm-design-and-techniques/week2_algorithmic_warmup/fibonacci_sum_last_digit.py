#Last Digit of the Sum of Fibonacci Numbers:
#Problem Introduction:
#The goal in this problem is to find the last digit of a sum of the first n Fibonacci numbers.
import sys
from fibonacci_huge import get_fibonacci_huge

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10

# O(n)?
# Sum(F(n)) = F(n+2) - 1 for n > 3
# I proved it by induction:
# n = 4: Sum(F(4)) = 7 = 8 - 1 = F(6) - 1
# Let's assume Sum(F(n)) = F(n + 2) - 1 and let's prove that Sum(F(n + 1)) = F(n + 3) - 1 
# Sum(F(n + 1)) = Sum(F(n)) + F(n + 1) = F(n + 2) - 1 + F(n + 1) = F(n + 3) - 1
def fibonacci_sum(n, m):

    return((get_fibonacci_huge(n + 2, m) + m - 1) % m)
    
if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum(n, 10))
    
    for i in range(n):
        assert(fibonacci_sum_naive(i) == fibonacci_sum(i, 10))
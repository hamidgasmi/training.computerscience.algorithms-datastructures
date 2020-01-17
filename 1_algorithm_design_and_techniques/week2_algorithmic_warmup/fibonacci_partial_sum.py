# Last Digit of a Partial Sum of Fibonacci Numbers:
# Problem Introduction
# Now, we would like to find the last digit of a partial sum of Fibonacci numbers: F(m) + F(m + 1) + ... + F(n)
import sys
from fibonacci_sum_last_digit import fibonacci_sum

def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10

#O(n)?
def fibonacci_partial_sum(from_, to, m):
    if to < from_: return 0

    return((fibonacci_sum(to, m) + m - fibonacci_sum(from_ - 1, m)) % m)

if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())

    print(fibonacci_partial_sum(from_, to, 10))
    print(fibonacci_partial_sum_naive(from_, to))
    for i in range(from_, to):
        assert(fibonacci_partial_sum_naive(i, to) == fibonacci_partial_sum(i, to, 10))
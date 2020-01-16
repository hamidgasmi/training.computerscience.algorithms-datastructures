# Problem Introduction:
# In this problem, your goal is to compute F n modulo m, where n may be really huge: up to 10 18 . For such
# values of n, an algorithm looping for n iterations will not fit into one second for sure. Therefore we need to
# avoid such a loop.
import sys
from fibonacci_last_digit import get_fibonacci_last_digit

#O(m)
def get_fibonacci_huge(n, m):
    if n <= 1: return n

    previous = 0
    current  = 1
    period = []
    period.append(previous)
    period.append(current)
    tmp = []
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

        if len(period) > 0 and period[len(tmp)] == current:
            tmp.append(current)
            if len(period) == len(tmp): break
        else:
            if len(tmp) > 0: 
                period.extend(tmp) #O(m)?
                tmp.clear()
            period.append(current)

    return pattern[n % len(period)]

if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())

    #for i in range(n):
    #    assert(get_fibonacci_last_digit(i, m) == get_fibonacci_huge(i, m))

    print(get_fibonacci_huge(n, m))
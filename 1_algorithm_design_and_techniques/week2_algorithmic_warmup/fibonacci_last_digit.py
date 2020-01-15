# Uses python3
import sys

#Time: O(n)
#Description: The last digit of (a + b) = the last digit (a) + the last digit (b)
def get_fibonacci_last_digit(n):
    if n <= 1: return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current) % 10

    return current

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit(n))
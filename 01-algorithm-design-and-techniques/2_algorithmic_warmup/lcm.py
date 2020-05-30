# Uses python3
import sys
from gcd import get_gcd

def get_lcm(n, m):

    gcd = get_gcd(n, m)
    if gcd == 0: return 0
    return n * (m // gcd)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())

    print(get_lcm(a, b))
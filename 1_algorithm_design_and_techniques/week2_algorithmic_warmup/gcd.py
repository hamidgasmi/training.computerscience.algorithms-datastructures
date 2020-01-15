# Uses python3
def get_gcd_naive(m, n):
    if (m == 0): return n
    if (n == 0): return m

    for i in range(min(n,m), 0, -1):
        if (n % i == 0 and m % i == 0): return i

    return 1

# O(lognm)
def get_gcd(n, m):
    
    if (n == 0): return m
    if (m == 0): return n 
    
    mn = min(n,m)
    mx = max(n,m)
    if (mx % mn) == 0: return mn
    return get_gcd(mn, mx % mn)

if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    assert(len(arr) == 2)

    #input = sys.stdin.read()
    #a, b = map(int, input.split())

    #print(get_gcd_naive(arr[0], arr[1]))
    print(get_gcd(arr[0], arr[1]))
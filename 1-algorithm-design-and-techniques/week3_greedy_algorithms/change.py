# Greedy Algorithms project - Issue #1
import sys

# Greedy Strategy:
### Make a greedy choice: To choose the biggest coin (Cmax) that is small to m 1st as a safe choice
### Prove that it is a safe choice:
### Reduce to a subproblem: remove the biggest coin
### Solve the subproblem (Iterate): Solve the subproblem with the rest of division m and without the biggest coin 
# O(1)
def get_change(m):
    n10 = m // 10
    n5 = (m % 10) // 5
    n1 = m - 10 * n10 - 5 * n5
    return n10 + n5 + n1

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
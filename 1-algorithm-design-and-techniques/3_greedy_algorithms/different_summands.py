import sys

# Time Complexity O(n)
# Greedy Algorithm
#... 1. Make a greedy choice:
#....... Start with a number n and k-th prize = 0
#....... For the i-th prize, choose the smallest nbr Mi so that n - Mi > Mi
#... 2. Prove this choice is safe:
#... 3. Reduce to a subproblem: n = n - Mi, k-th prize = 
#... 4. Solve the subproblem (Iterate): go to 1.
def optimal_summands(n):
    summands = []
    
    CurrPrize = 0
    while (n > 0):
        if n - CurrPrize - 1 > CurrPrize + 1: 
            CurrPrize += 1
            summands.append(CurrPrize)
            n = n - CurrPrize
        else:
            summands.append(n)
            n = 0

    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')

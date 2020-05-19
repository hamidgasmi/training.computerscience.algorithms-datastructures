#python3
import sys

# 1. Express a solution mathematically: Change(M) = min{ Change(M - Coin[i]) } + 1 for all i between 0 and |Coins| - 1
# 2. Proof: Let's assume we came up with an optimal solution by using a subsolution j where Changes(j) > min{ change(j - Coin[i]) } + 1
#           Change(M, j) = Change(j) + ...
#           Let's note min{ change(Mj - Coin[i]) } + 1 = Change(j')
#           But since Change(j) > Change(j')
#           Then, we could replace in our optimal solution Change(j) by Change(j')
#           This will lead us to a contradiction: We would build a new solution Change(M, j') < Change(M, j)
# 3. Solutions: we can solve this problem in 2 ways:
#    1. Bottom up solution
#    2. Recursive + Memorization solution

# Running Time: O(monney * |coins|)
#   1. Coins array could be sorted by Counting Sort algorithm
#   2. 2 for loops: monney * |coins|
# Space Complexity: O(monney)
def find_change_buttom_up(monney, coins):
    
    changes = [0]
    coins.sort()

    for m in range(1, monney + 1, 1):
        changes.append(sys.maxsize)
        for coin in coins:
            if m >= coin:
                candidate_change = changes[ m - coin ] + 1
                changes[m] = min(changes[m], candidate_change)
            else:
                break
        
    return changes[monney]

if __name__ == "__main__":
    money = int(sys.stdin.readline().strip())
    coins = list(map(int, sys.stdin.readline().strip().split(',')))
    
    print(find_change_buttom_up(money, coins))


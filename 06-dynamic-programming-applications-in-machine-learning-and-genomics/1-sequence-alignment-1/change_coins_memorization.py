import sys
import math
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
class CoinChanger:
    def __init__(self, coins):
        self.coins = coins.copy()
        self.coins.sort()

    # Solution: top down
    # Running Time: O(monney * |coins|): 2 for loops: monney * |coins|
    # Space Complexity: O(max_coin)
    def make_change(self, money):
        
        changes = [math.inf for _ in range(money + 1)]
        changes[0] = 0
        
        money_change = self.make_change_memorized(money, coins, changes)
        return -1 if money_change == math.inf else money_change

    def make_change_memorized(self, m, coins, changes):
        if changes[m] != math.inf:
            return changes[m]
        
        for coin in coins:
            if m < coin:
                continue

            candidate_change = self.make_change_memorized(m - coin, coins, changes)
            if candidate_change == -1:
                continue
            changes[m] = min(changes[m], candidate_change + 1)

        if changes[m] == math.inf:
            changes[m] = -1

        return changes[m]

if __name__ == "__main__":
    money = int(sys.stdin.readline().strip())
    coins = list(map(int, sys.stdin.readline().strip().split(',')))
    
    coinchanger = CoinChanger(coins)
    
    print(coinchanger.make_change(money))

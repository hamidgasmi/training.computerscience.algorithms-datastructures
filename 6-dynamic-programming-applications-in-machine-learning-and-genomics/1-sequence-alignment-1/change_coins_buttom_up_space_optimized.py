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

    # Solution: buttom up solution
    # Running Time: O(money * |coins|): 2 for loops: money * |coins|
    # Space Complexity: O(max(money, max_coin))
    def make_change(self, money):
        
        max_coin = min(money, max(self.coins))
        changes = dict()
        changes[0] = 0
        
        for m in range(1, money + 1, 1):
            
            money_change = math.inf #sys.maxsize
            for coin in self.coins:
                if coin > m:
                    continue
                
                candidate_change = changes[m - coin] + 1
                money_change = min(money_change, candidate_change)

            if len(changes) >= max_coin:
                changes.pop(m - max_coin)
            changes[m] = money_change
            
        return -1 if changes[money] == math.inf else changes[money]

if __name__ == "__main__":
    money = int(sys.stdin.readline().strip())
    
    coins = list(map(int, sys.stdin.readline().strip().split(',')))
    
    coinchanger = CoinChanger(coins)    

    print(coinchanger.make_change(money))
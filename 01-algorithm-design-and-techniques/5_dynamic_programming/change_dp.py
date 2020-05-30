# Uses python3
import sys

def get_change(m, coins, results):
    if m == 0:
        return 0
    elif results[m] != 0:
        return results[m]

    results[m] = 1001
    for i in range(len(coins)):
        if m >= coins[i]:
            results[m] = min(results[m], get_change(m - coins[i], coins, results) + 1)

    return results[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    coins = [1, 3, 4]
    results = [0 for i in range(m + 1)]
    for i in range(0, len(coins)):
        if m >= coins[i]:
            results[coins[i]] = 1
    print(get_change(m, coins, results))

#python3 change_dp.py <<< "0"
#python3 change_dp.py <<< "1"
#python3 change_dp.py <<< "2"
#python3 change_dp.py <<< "3"
#python3 change_dp.py <<< "4"
#python3 change_dp.py <<< "5"
#python3 change_dp.py <<< "6"
#python3 change_dp.py <<< "7"
#python3 change_dp.py <<< "8"
#python3 change_dp.py <<< "9"
#python3 change_dp.py <<< "10"
#python3 change_dp.py <<< "11"
#python3 change_dp.py <<< "12"
#python3 change_dp.py <<< "13"
#python3 change_dp.py <<< "14"
#python3 change_dp.py <<< "15"
#python3 change_dp.py <<< "16"

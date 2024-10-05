import sys

def single_number(nums):
    
    if len(nums) == 0:
        return

    sn = 0
    for n in nums:
        sn ^= n

    return sn

if __name__ == "__main__":
    input = sys.stdin.read()
    tokens = input.split()
    nums = [ int(tokens[i]) for i in range(len(tokens)) ]
    print(single_number(nums))
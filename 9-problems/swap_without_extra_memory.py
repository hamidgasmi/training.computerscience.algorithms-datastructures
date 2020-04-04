# Time Complexity: O(1)
# Space Complexity: O(1)
def swap(a, b):
    a ^= b # a = initial_a XOR initial_b
    b ^= a # b = initial_b XOR a = initial_b XOR initial_a XOR b = initial_a
    a ^= b # a = a XOR b = initial_a XOR initial_b XOR initial_a = initial_b

    print("(a, b): ", a, b)

if __name__ == "__main__":
    a,b = map(int, input().split())
    swap(a, b)
    print("(a, b): ", a, b)

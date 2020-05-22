import sys
import math

# Solution: Combination = (total moves # choose total moves down #) or (total moves # choose total moves right #)
# Running Time: O(n + m): linear
# Space Complexity: O(1)
def compute_number_paths_grid_combination(n, m):
    
    if (n <= 0 or m <= 0) or (n == 1 and m == 1):
        return 0
    
    total_moves_nbr = (n - 1) + (m - 1)
    total_moves_down = (n - 1)
    return math.factorial(total_moves_nbr) // (math.factorial(total_moves_down) * math.factorial(total_moves_nbr - total_moves_down))

# Solution: Naive Approach
# Running Time: O(nm): Quadratic
# Space Complexity: O(nm): Quadratic
def compute_number_paths_grid(n, m):
    
    grid = [ [1 for _ in range(m)] for _ in range(n)]
    grid[0][0] = 0

    for r in range(1, n, 1):
        for c in range(1, m, 1):
            grid[r][c] = grid[r][c - 1] + grid[r - 1][c]
    
    return grid[n - 1][m - 1]

if __name__ == "__main__":

    n = int(sys.stdin.readline().strip())
    m = int(sys.stdin.readline().strip())

    print(compute_number_paths_grid(n, m))
    print(compute_number_paths_grid_combination(n, m))

    

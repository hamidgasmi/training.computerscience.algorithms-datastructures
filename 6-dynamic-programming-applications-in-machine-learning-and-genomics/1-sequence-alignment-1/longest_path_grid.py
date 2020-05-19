import sys

# 1. Express a solution mathematically: Let's be a Matrix M of (n+1) x (m+1):
#     For 0 <= r <= n and 0 <= c <= m, M[r,c] contains the longest path from the source (0, 0) to (r, c) 
#     M[0 , 0] = 0
#     M[0 , c] = M[0 , c - 1] + right[0, c] for 1 <= c <= m
#     M[r , 0] = M[r - 1 , 0] + down[r , 0] for 1 <= r <= n
#     M[r , c] = max(M[r - 1 , c] + down[r - 1 , c], M[r , c - 1] + right[r ,  c - 1])
# 2. Proof:
#     Let's assume that there is a vertice (r, c) that belongs to the optimal path P with a the longest path length |P|
#     But M[r , c] < max(M[r - 1 , c] + down[r - 1 , c], M[r , c - 1] + right[r ,  c - 1])
#     This means that if we replace M[r , c] with max(M[r - 1 , c] + down[r - 1 , c], M[r , c - 1] + right[r ,  c - 1])
#     The new path P length |P'| will be greater than |P| ==> contradiction with the fact that |P| was the longest path
# 3. Implementation:
#    Buttom up solution
#    Running Time: O(nm) (Quadratic)
#    Space complexity: O(nm) (Quadratic)
class Solution:
    def __init__(self, n, m):
        self.rows_count = n + 1
        self.columns_count = m + 1
    
    def longest_path(self, down, right):
        
        M = [ [0 for _ in range(self.columns_count)] for _ in range(self.rows_count) ]
        
        for c in range(1, self.columns_count, 1):
            M[0][c] = M[0][c - 1] + right[0][c - 1]

        for r in range(1, self.rows_count, 1):
            M[r][0] = M[r - 1][0] + down[r - 1][0]
        
        for r in range(1, self.rows_count, 1):
            for c in range(1, self.columns_count, 1):
                candidate_predecesor_top = M[r - 1][c] + down[r - 1][c]
                candidate_predecesor_left = M[r][c - 1] + right[r][c - 1]
                M[r][c] = max(candidate_predecesor_top, candidate_predecesor_left)

        return M[self.rows_count - 1][self.columns_count - 1]

if __name__ == "__main__":
    n,m = map(int, sys.stdin.readline().strip().split())
    down = [list(map(int, sys.stdin.readline().strip().split()))
            for _ in range(n)]
    sys.stdin.readline()
    right = [list(map(int, sys.stdin.readline().strip().split()))
            for _ in range(n+1)]

    s = Solution(n, m)
    print(s.longest_path(down, right))

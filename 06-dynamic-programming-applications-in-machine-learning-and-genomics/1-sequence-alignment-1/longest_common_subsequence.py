import sys

# 1. Express a solution mathematically:
#       Let's A be a matrix of alignments of (|s| + 1) x (|t| + 1)
#       A[0,0] = 0
#       A[0,c] = 0 for 1 <= c <= |s|
#       A[r,0] = 0 for 1 <= r <= |t|
#       A[r,c] = max(A[r-1,c-1] + 1 if s[c] = t[r] else 0, A[r-1,c] + 0, A[r,c-1] + 0) for 1 <= c <= |s| and 1 <= r <= |t|
# 2. Proof:
# 3. Implementation: buttom up solution
#    Running time: O(nm)
#    Space Complexity: O(nm)
class Solution:
    def __init__(self, s, t):
        self.rows_count = len(t) + 1
        self.columns_count = len(s) + 1

        A = self.built_lcs_matrix(s, t)
        self.lcs = self.get_lcs(A)

    def built_lcs_matrix(self, s, t):
        A = [ [0 for _ in range(self.columns_count)] for _ in range(self.rows_count)]

        for r in range(1, self.rows_count, 1):
            for c in range(1, self.columns_count, 1):
                alignment_score = A[r-1][c-1] + 1 if t[r-1] == s[c-1] else 0
                delete_score = A[r][c-1]
                insert_score = A[r-1][c]
                A[r][c] = max(alignment_score, delete_score, insert_score)

        return A

    def get_lcs(self, A):
        lcs_inverse_list = []

        r = self.rows_count - 1
        c = self.columns_count - 1
        while r > 0 and c > 0:
            
            if A[r][c] == A[r - 1][c - 1] + 1 and s[c - 1] == t[r - 1]:
                lcs_inverse_list.append(s[c - 1])
                c = c - 1
                r = r - 1

            elif A[r][c] == A[r - 1][c - 1]:
                c = c - 1
                r = r - 1

            elif A[r][c] == A[r][c - 1]:
                c = c - 1

            elif A[r][c] == A[r - 1][c]:
                r = r - 1
        
        return ''.join(lcs_inverse_list[::-1])


if __name__ == "__main__":
    s,t = sys.stdin.read().strip().splitlines()
    
    lcs_solution = Solution(s,t)

    print(lcs_solution.lcs)

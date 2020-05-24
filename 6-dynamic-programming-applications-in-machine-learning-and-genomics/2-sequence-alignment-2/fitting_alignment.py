import sys
import math

# 1. Express a solution mathematically:
#       Let's A be a matrix of alignments of (|s| + 1) x (|t| + 1)
#       A[0,0] = 0
#       A[0,c] = c * sigma for 1 <= c <= |s|
#       A[r,0] = r * sigma for 1 <= r <= |t|
#       A[1,c] = max(A[0,0] + match if s[c] = t[r] else mu, A[r-1,c-1] + match if s[c] = t[r] else mu, A[r-1,c] + sigma, A[r,c-1] + sigma) for 1 <= c <= |s| and r = 1
#       A[r,c] = max(A[r-1,c-1] + match if s[c] = t[r] else mu, A[r-1,c] + sigma, A[r,c-1] + sigma) for 1 <= c <= |s| and 1 <= r <= |t|
# 2. Proof:
# 3. Implementation: buttom up solution
#    Running time: O(nm)
#    Space Complexity: O(nm)
class Alignment:
    def __init__(self, match, mu, sigma):
        
        self.match = match
        self.mu = mu * (-1)
        self.sigma = sigma * (-1)
        self.fitting_alignment_score = 0

    def global_alignment(self, s, t):

        A, max_alignment_r, max_alignment_c = self.built_fitting_alignment_matrix(s, t)
        self.aligned_seq_1, self.aligned_seq_2 = self.get_fitting_alignment_backtrack(A, max_alignment_r, max_alignment_c)

        return self.fitting_alignment_score, self.aligned_seq_1, self.aligned_seq_2

    def built_fitting_alignment_matrix(self, s, t):

        rows_count = len(t) + 1
        columns_count = len(s) + 1

        A = []
        A.append([c * self.sigma for c in range(columns_count)])
        for r in range(1, rows_count, 1):
            A.append([(r * self.sigma if c == 0 else 0) for c in range(columns_count)])
        
        max_alignment_r = rows_count - 1
        max_alignment_c = 0
        for r in range(1, rows_count, 1):
            for c in range(1, columns_count, 1):
                
                alignment_score = A[r - 1][c - 1] + (self.match if s[c - 1] == t[r - 1] else self.mu)
                delete_score = A[r][c-1] + self.sigma
                insert_score = A[r-1][c] + self.sigma
                A[r][c] = max((self.match if s[c - 1] == t[r - 1] else self.mu) if r == 1 else -math.inf, alignment_score, delete_score, insert_score)

                if r == rows_count - 1 and A[r][c] > A[max_alignment_r][max_alignment_c]:
                    max_alignment_r = r
                    max_alignment_c = c

        self.fitting_alignment_score = A[max_alignment_r][max_alignment_c]
        #print(self.fitting_alignment_score)
        #for r in range(rows_count):
        #    print(A[r])

        return A, max_alignment_r, max_alignment_c

    def get_fitting_alignment_backtrack(self, A, max_alignment_r, max_alignment_c):
        aligned_seq_1_inverse = []
        aligned_seq_2_inverse = []

        r = max_alignment_r
        c = max_alignment_c
        while r > 0 and c > 0:
            
            if r == 1 and c > 1 and A[r][c] == (self.match if s[c - 1] == t[r - 1] else self.mu):
                aligned_seq_1_inverse.append(s[c - 1])
                aligned_seq_2_inverse.append(t[r - 1])
                c = 0
                r = 0

            elif A[r][c] == A[r - 1][c - 1] + (self.match if s[c - 1] == t[r - 1] else self.mu):
                aligned_seq_1_inverse.append(s[c - 1])
                aligned_seq_2_inverse.append(t[r - 1])
                c -= 1
                r -= 1

            elif A[r][c] == A[r][c - 1] + self.sigma:
                aligned_seq_1_inverse.append(s[c - 1])
                aligned_seq_2_inverse.append('-')
                c -= 1

            elif A[r][c] == A[r - 1][c] + self.sigma:
                aligned_seq_1_inverse.append('-')
                aligned_seq_2_inverse.append(t[r - 1])
                r -= 1
        
        return ''.join(aligned_seq_1_inverse[::-1]), ''.join(aligned_seq_2_inverse[::-1])

if __name__ == "__main__":
    m,mu,sigma = map(int,sys.stdin.readline().strip().split())
    s,t = [sys.stdin.readline().strip() for _ in range(2)]

    alignment = Alignment(m, mu, sigma)
    alignment.global_alignment(s, t)
    
    print(alignment.fitting_alignment_score)
    print(alignment.aligned_seq_1)
    print(alignment.aligned_seq_2)

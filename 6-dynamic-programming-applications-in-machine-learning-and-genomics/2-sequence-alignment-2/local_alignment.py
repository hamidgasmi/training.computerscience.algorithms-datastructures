import sys

# 1. Express a solution mathematically:
#       Let's A be a matrix of alignments of (|s| + 1) x (|t| + 1)
#       A[0,0] = 0
#       A[0,c] = 0 for 1 <= c <= |s|
#       A[r,0] = 0 for 1 <= r <= |t|
#       A[r,c] = max(0, A[r-1,c-1] + match if s[c] = t[r] else mu, A[r-1,c] + sigma, A[r,c-1] + sigma) for 1 <= c <= |s| and 1 <= r <= |t|
# 2. Proof:
# 3. Implementation: buttom up solution
#    Running time: O(nm)
#    Space Complexity: O(nm)
class Local_Alignment:
    def __init__(self, match, mu, sigma):
        self.match = match
        self.mu = mu * (-1)
        self.sigma = sigma * (-1)
        self.local_alignment_score = 0
    
    def local_alignment(self, s, t):

        A, max_alignment_r, max_alignment_c = self.built_local_alignment_matrix(s, t)
        self.aligned_seq_1, self.aligned_seq_2 = self.get_local_alignment_backtrack(A, max_alignment_r, max_alignment_c)

        return self.local_alignment_score, self.aligned_seq_1, self.aligned_seq_2

    def built_local_alignment_matrix(self, s, t):
        
        rows_count = len(t) + 1
        columns_count = len(s) + 1
        A = [ [0 for _ in range(columns_count)] for _ in range(rows_count) ]
        
        max_alignment_r = 0
        max_alignment_c = 0
        for r in range(1, rows_count, 1):
            for c in range(1, columns_count, 1):
                
                alignment_score = A[r - 1][c - 1] + (self.match if s[c - 1] == t[r - 1] else self.mu)
                delete_score = A[r][c-1] + self.sigma
                insert_score = A[r-1][c] + self.sigma
                A[r][c] = max(0, alignment_score, delete_score, insert_score)

                if A[r][c] > A[max_alignment_r][max_alignment_c]:
                    max_alignment_r = r
                    max_alignment_c = c
        
        self.local_alignment_score = A[max_alignment_r][max_alignment_c]

        return A, max_alignment_r, max_alignment_c

    def get_local_alignment_backtrack(self, A, max_alignment_r, max_alignment_c):
        aligned_seq_1_inverse = []
        aligned_seq_2_inverse = []

        r = max_alignment_r
        c = max_alignment_c
        while r > 0 and c > 0:
            
            if A[r][c] == A[r - 1][c - 1] + (self.match if s[c - 1] == t[r - 1] else self.mu):
                aligned_seq_1_inverse.append(s[c - 1])
                aligned_seq_2_inverse.append(t[r - 1])
                c -= 1
                r -= 1
            
            elif A[r][c] == 0:
                c = 0
                r = 0
            
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

    alignment = Local_Alignment(m, mu, sigma)
    alignment.local_alignment(s, t)
    
    print(alignment.local_alignment_score)
    print(alignment.aligned_seq_1)
    print(alignment.aligned_seq_2)
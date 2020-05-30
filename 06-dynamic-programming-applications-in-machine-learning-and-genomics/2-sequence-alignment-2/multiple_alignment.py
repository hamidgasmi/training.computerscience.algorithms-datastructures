import sys

class Alignment:
    def __init__(self, match, mu, sigma):
        
        self.match = match
        self.mu = mu * (-1)
        self.sigma = sigma * (-1)
        self.global_alignment_score = 0

    def global_alignment(self, r, s, t):

        A = self.built_global_alignment_matrix(r, s, t)
        self.aligned_seq_1, self.aligned_seq_2, self.aligned_seq_3 = self.get_alignment_backtrack(r, s, t, A)

        return self.global_alignment_score, self.aligned_seq_1, self.aligned_seq_2, self.aligned_seq_3

    def built_global_alignment_matrix(self, r, s, t):
        
        rows_count = len(r) + 1
        columns_count = len(s) + 1
        depth_count = len(t) + 1
        
        A = [[[0 for dep in range(depth_count)] for col in range(columns_count)] for row in range(rows_count)]
        for row in range(1, rows_count, 1):
            A[row][0][0] = row * self.sigma
        for col in range(1, columns_count, 1):
            A[0][col][0] = col * self.sigma
        for dep in range(1, depth_count, 1):
            A[0][0][dep] = dep * self.sigma
        
        for row in range(1, rows_count, 1):
            for col in range(1, columns_count, 1):
                for dep in range(1, depth_count, 1):
                    A[row][col][dep] = max(A[row - 1][col - 1][dep - 1] + self.match if r[row - 1] == s[col - 1] == t[dep - 1] else self.mu,
                                           max(A[row][col - 1][dep - 1], A[row][col - 1][dep], A[row][col][dep - 1], A[row - 1][col][dep - 1], 
                                               A[row - 1][col][dep], A[row - 1][col - 1][dep], A[row - 1][col][dep]) + self.sigma)
        
        self.global_alignment_score = A[rows_count - 1][columns_count - 1][depth_count - 1]
        
        return A

    def get_alignment_backtrack(self, r, s, t, A):

        aligned_seq_1_inverse = []
        aligned_seq_2_inverse = []
        aligned_seq_3_inverse = []
        
        row = len(r)
        col = len(s)
        dep = len(t)

        while row > 0 and col > 0 and dep > 0:
            if A[row][col][dep] == A[row - 1][col - 1][dep - 1] + (self.match if s[col - 1] == r[row - 1] == t[dep - 1] else self.mu):
                aligned_seq_1_inverse.append(r[row - 1])
                aligned_seq_2_inverse.append(s[col - 1])
                aligned_seq_3_inverse.append(t[dep - 1])
                col -= 1
                row -= 1
                dep -= 1

            elif A[row][col][dep] == A[row][col - 1][dep - 1] + self.sigma:
                aligned_seq_1_inverse.append('-')
                aligned_seq_2_inverse.append(s[col - 1])
                aligned_seq_3_inverse.append(t[dep - 1])
                col -= 1
                dep -= 1

            elif A[row][col][dep] == A[row][col - 1][dep] + self.sigma:
                aligned_seq_1_inverse.append('-')
                aligned_seq_2_inverse.append(s[col - 1])
                aligned_seq_3_inverse.append('-')
                col -= 1

            elif A[row][col][dep] == A[row][col][dep - 1] + self.sigma:
                aligned_seq_1_inverse.append('-')
                aligned_seq_2_inverse.append('-')
                aligned_seq_3_inverse.append(t[dep - 1])
                dep -= 1

            elif A[row][col][dep] == A[row - 1][col][dep - 1] + self.sigma:
                aligned_seq_1_inverse.append(r[row - 1])
                aligned_seq_2_inverse.append('-')
                aligned_seq_3_inverse.append(t[dep - 1])
                row -= 1
                dep -= 1

            elif A[row][col][dep] == A[row - 1][col][dep] + self.sigma:
                aligned_seq_1_inverse.append(r[row - 1])
                aligned_seq_2_inverse.append('-')
                aligned_seq_3_inverse.append('-')
                row -= 1

            elif A[row][col][dep] == A[row - 1][col - 1][dep] + self.sigma:
                aligned_seq_1_inverse.append(r[row - 1])
                aligned_seq_2_inverse.append(s[col - 1])
                aligned_seq_3_inverse.append('')
                col -= 1
                row -= 1
        
        while row > 0 and col > 0:
            
            if A[row][col][0] == A[row - 1][col - 1][0] + (self.match if s[col - 1] == r[row - 1] else self.mu):
                aligned_seq_1_inverse.append(r[row - 1])
                aligned_seq_2_inverse.append(s[col - 1])
                col -= 1
                row -= 1

            elif A[row][col][0] == A[row][col - 1][0] + self.sigma:
                aligned_seq_1_inverse.append('-')
                aligned_seq_2_inverse.append(s[col - 1])
                col -= 1

            elif A[row][col][0] == A[row - 1][col][0] + self.sigma:
                aligned_seq_1_inverse.append(r[row - 1])
                aligned_seq_2_inverse.append('-')
                row -= 1
            aligned_seq_3_inverse.append('-')

        while row > 0 and dep > 0:
            if A[row][0][dep] == A[row - 1][0][dep - 1] + (self.match if t[dep - 1] == r[row - 1] else self.mu):
                aligned_seq_1_inverse.append(r[row - 1])
                aligned_seq_3_inverse.append(t[dep - 1])
                dep -= 1
                row -= 1

            elif A[row][0][dep] == A[row][0][dep - 1] + self.sigma:
                aligned_seq_1_inverse.append('-')
                aligned_seq_3_inverse.append(t[dep - 1])
                dep -= 1

            elif A[row][0][dep] == A[row - 1][0][dep] + self.sigma:
                aligned_seq_1_inverse.append(r[row - 1])
                aligned_seq_3_inverse.append('-')
                row -= 1
            aligned_seq_2_inverse.append('-')

        while col > 0 and dep > 0:
            if A[0][col][dep] == A[0][col - 1][dep - 1] + (self.match if s[col - 1] == t[dep - 1] else self.mu):
                aligned_seq_2_inverse.append(s[col - 1])
                aligned_seq_3_inverse.append(t[dep - 1])
                col -= 1
                dep -= 1

            elif A[0][col][dep] == A[0][col - 1][dep] + self.sigma:
                aligned_seq_2_inverse.append(s[col - 1])
                aligned_seq_3_inverse.append('-')
                col -= 1

            elif A[0][col][dep] == A[0][col][dep - 1] + self.sigma:
                aligned_seq_2_inverse.append('-')
                aligned_seq_3_inverse.append(t[dep - 1])
                dep -= 1
            aligned_seq_1_inverse.append('-')

        while row > 0:
            aligned_seq_1_inverse.append(r[row - 1])
            aligned_seq_2_inverse.append('-')
            aligned_seq_3_inverse.append('-')
            row -= 1

        while col > 0:
            aligned_seq_1_inverse.append('-')
            aligned_seq_2_inverse.append(s[col - 1])
            aligned_seq_3_inverse.append('-')
            col -= 1

        while dep > 0:
            aligned_seq_1_inverse.append('-')
            aligned_seq_2_inverse.append('-')
            aligned_seq_3_inverse.append(t[dep - 1])
            dep -= 1
        
        return ''.join(aligned_seq_1_inverse[::-1]), ''.join(aligned_seq_2_inverse[::-1]), ''.join(aligned_seq_3_inverse[::-1])

if __name__ == "__main__":
    
    r,s,t = [sys.stdin.readline().strip() for _ in range(3)]
    
    alignment = Alignment(1, 0, 0)
    alignment.global_alignment(r,s, t)

    print(alignment.global_alignment_score)
    print(alignment.aligned_seq_1)
    print(alignment.aligned_seq_2)
    print(alignment.aligned_seq_3)

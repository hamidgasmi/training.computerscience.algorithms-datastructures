import sys
import math

class Alignment:
    def __init__(self, match, mu, sigma, epsilon):
        
        self.match = match
        self.mu = mu * (-1)
        self.sigma = sigma * (-1)
        self.epsilon = epsilon * (-1)

        self.global_alignment_score = 0

    def global_alignment(self, s, t):

        Lower, Middle, Upper = self.built_global_alignment_matrix(s, t)
        self.aligned_seq_1, self.aligned_seq_2 = self.get_alignment_backtrack(s, t, Lower, Middle, Upper)

        return self.global_alignment_score, self.aligned_seq_1, self.aligned_seq_2

    def built_global_alignment_matrix(self, s, t):

        rows_count = len(t) + 1
        columns_count = len(s) + 1

        Lower, Middle, Upper = [], [], []
        Lower.append([ -math.inf for c in range(columns_count)])
        Middle.append([ (0 if c == 0 else self.sigma + self.epsilon * (c - 1)) for c in range(columns_count)])
        Upper.append([ -math.inf for c in range(columns_count)])
        for r in range(1, rows_count, 1):
            Lower.append([ 0 for c in range(columns_count)])
            Middle.append([ (self.sigma + self.epsilon * (r - 1) if c == 0 else 0) for c in range(columns_count)])
            Upper.append([ (-math.inf if c == 0 else 0) for c in range(columns_count)])
        
        for r in range(1, rows_count, 1):
            for c in range(1, columns_count, 1):
                
                c = c
                Lower[r][c] = max(Lower[r - 1][c] + self.epsilon, Middle[r - 1][c] + self.sigma)
                Upper[r][c] = max(Upper[r][c - 1] + self.epsilon, Middle[r][c - 1] + self.sigma)
                alignment_score = Middle[r - 1][c - 1] + (self.match if s[c - 1] == t[r - 1] else self.mu)
                Middle[r][c] = max(Lower[r][c], alignment_score, alignment_score, Upper[r][c])
                
        self.global_alignment_score = Middle[rows_count - 1][columns_count - 1]
        
        return Lower, Middle, Upper

    def get_alignment_backtrack(self, s, t, Lower, Middle, Upper):
        
        aligned_seq_1_inverse = []
        aligned_seq_2_inverse = []

        r = len(t)
        c = len(s)
        matrix_no = 1
        while r > 0 and c > 0:
            
            if matrix_no == 1:
                if Middle[r][c] == Middle[r - 1][c - 1] + (self.match if s[c - 1] == t[r - 1] else self.mu):
                    aligned_seq_1_inverse.append(s[c - 1])
                    aligned_seq_2_inverse.append(t[r - 1])
                    c -= 1
                    r -= 1

                elif Middle[r][c] == Lower[r][c]:
                    matrix_no = 0

                elif Middle[r][c] == Upper[r][c]:
                    matrix_no = 2

            elif matrix_no == 0:
                if Lower[r][c] == Middle[r - 1][c] + self.sigma:
                    matrix_no = 1

                aligned_seq_1_inverse.append('-')
                aligned_seq_2_inverse.append(t[r - 1])
                r -= 1

            elif matrix_no == 2:
                if Upper[r][c] == Middle[r][c - 1] + self.sigma:
                    matrix_no = 1

                aligned_seq_1_inverse.append(s[c - 1])
                aligned_seq_2_inverse.append('-')
                c -= 1

        while c > 0:
            aligned_seq_1_inverse.append(s[c - 1])
            aligned_seq_2_inverse.append('-')
            c -= 1

        while r > 0:
            aligned_seq_1_inverse.append('-')
            aligned_seq_2_inverse.append(t[r - 1])
            r -= 1
        
        return ''.join(aligned_seq_1_inverse[::-1]), ''.join(aligned_seq_2_inverse[::-1])

if __name__ == "__main__":
    m, mu, sigma, epsilon = map(int,sys.stdin.readline().strip().split())
    s,t = [sys.stdin.readline().strip() for _ in range(2)]

    alignment = Alignment(m, mu, sigma, epsilon)
    alignment.global_alignment(s, t)
    
    print(alignment.global_alignment_score)
    print(alignment.aligned_seq_1)
    print(alignment.aligned_seq_2)

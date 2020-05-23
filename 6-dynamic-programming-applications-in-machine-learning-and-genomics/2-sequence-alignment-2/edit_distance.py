import sys

# 1. Express a solution mathematically:
#       Let's A be a matrix of alignments of (|s| + 1) x (|t| + 1)
#       A[0,0] = 0
#       A[0,c] = c for 1 <= c <= |s|
#       A[r,0] = r for 1 <= r <= |t|
#       A[r,c] = min(A[r-1,c-1] + 0 if s[c] = t[r] else 1, A[r-1,c] + 1, A[r,c-1] + 1) for 1 <= c <= |s| and 1 <= r <= |t|
# 2. Proof:
# 3. Implementation: buttom up solution
#    Running time: O(nm)
#    Space Complexity: O(nm)

def edit_distance(s, t):
   
    columns_count = len(s) + 1
    rows_count = len(t) + 1
    match = 0
    mu = 1
    sigma = 1

    D = []
    D.append([c for c in range(columns_count)])
        
    for r in range(1, rows_count, 1):
        D.append([(r if c == 0 else 0) for c in range(columns_count)])

    for r in range(1, rows_count, 1):
        for c in range(1, columns_count, 1):
            match_or_substitution = D[r - 1][c - 1] + (match if s[c - 1] == t[r - 1] else mu)
            deletion = D[r][c-1] + sigma
            insertion = D[r-1][c] + sigma
            D[r][c] = min(match_or_substitution, deletion, insertion)

    return D[len(t)][len(s)]

if __name__ == "__main__":

    print(edit_distance(input(), input()))

def edit_distance(s, t):
    D = [[0 for c in range(len(s) + 1)] for r in range(len(t) + 1)] 
    for c in range(1, len(s) + 1):
        D[0][c] = c
    for r in range(1, len(t) + 1):
        D[r][0] = r

    for c in range(1, len(s) + 1):
        for r in range(1, len(t) + 1):
            
            if s[c - 1] == t[r - 1]:
                D[r][c] = min(D[r - 1][c - 1], D[r][c - 1] + 1, D[r - 1][c] + 1)
            else:
                D[r][c] = min(D[r - 1][c - 1], D[r][c - 1], D[r - 1][c]) + 1

    for r in range(len(t) + 1):
        print(D[r])

    return D[len(t)][len(s)]

if __name__ == "__main__":
    print(edit_distance(input(), input()))

#python3 edit_distance.py <<< "ab", "ab"
#python3 edit_distance.py <<< "ab", "cb"
#python3 edit_distance.py <<< "ab", "ac"
#python3 edit_distance.py <<< "ab", "abc"
#python3 edit_distance.py <<< "abc", "ab"
#python3 edit_distance.py <<< "short", "ports"
#python3 edit_distance.py <<< "editing", "distance"
#python3 edit_distance.py <<< "axybc", "distance"
#python3 edit_distance.py <<< "bread", "really"

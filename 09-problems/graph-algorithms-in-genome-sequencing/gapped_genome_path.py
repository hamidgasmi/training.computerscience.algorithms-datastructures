import sys

# Running Time: O(|paired_comp|)
def reconstruct(k, d, paired_comp):
    prefixes, suffixes = [], []

    for pair in paired_comp:
        prefix, suffix = pair.split('|')
        if len(prefixes) == 0:
            prefixes.append(prefix)
        elif (len(prefixes) - 1) < d: 
            prefixes.append(prefix[k - 1])

        if len(suffixes) == 0:
            suffixes.append(suffix)
        else:
            suffixes.append(suffix[k - 1])
        
    return ''.join(prefixes + suffixes)

if __name__ == "__main__":
    k, d = map(int, sys.stdin.readline().strip().split())
    paired_comp = [line.strip() for line in sys.stdin if line.strip()]

    print(reconstruct(k, d, paired_comp))

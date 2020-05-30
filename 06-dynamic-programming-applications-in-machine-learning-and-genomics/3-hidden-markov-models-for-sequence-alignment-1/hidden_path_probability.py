import sys

def path_probability(pi, states, transition):
    if len(pi) == 0:
        return 0.0

    probability = 1/len(states)
    for p in range(1, len(pi)):
        probability *= transition[pi[p - 1]][ pi[p] ]

    return probability

if __name__ == "__main__":
    pi = sys.stdin.readline().strip()
    sys.stdin.readline() # delimiter

    states = sys.stdin.readline().strip().split()
    sys.stdin.readline() # delimiter

    chars = sys.stdin.readline().strip().split() # first row of trans mat
    transition = {line[0]: dict(zip(chars, map(float,line.strip().split()[1:]))) 
            for line in sys.stdin}

    print(path_probability(pi,states,transition))

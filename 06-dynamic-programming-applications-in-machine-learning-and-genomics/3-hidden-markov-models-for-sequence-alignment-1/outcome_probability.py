import sys

def outcome_probability(x, sigma, pi, states, emission):
    if len(pi) == 0:
        return 0.0

    probability = 1
    for p in range(len(pi)):
       probability *= emission[ pi[p] ][ x[p] ]

    return probability

if __name__ == "__main__":
    x = sys.stdin.readline().strip()
    sys.stdin.readline() # delimiter

    sigma = sys.stdin.readline().strip().split()
    sys.stdin.readline() # delimiter

    pi = sys.stdin.readline().strip()
    sys.stdin.readline() # delimiter

    states = sys.stdin.readline().strip().split()
    sys.stdin.readline() # delimiter

    chars = sys.stdin.readline().strip().split() 
    emission = [sys.stdin.readline().strip().split() for _ in range(len(states))]
    emission = {line[0]:dict(zip(chars, map(float,line[1:]))) for line in emission}

    print(outcome_probability(x,sigma,pi,states,emission))
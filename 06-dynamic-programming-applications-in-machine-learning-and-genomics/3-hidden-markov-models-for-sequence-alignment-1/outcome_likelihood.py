import sys

def outcome_likelihood(x, sigma, states, transition, emission):
    
    # The transitions from the initial state occur with equal probability: Prob(P0 = Si) = 1/|states| * Pr(x = x0 | P0)
    M = [ [ emission[ states[s] ][ x[0] ]/len(states) if p == 0 else 0 for p in range(len(x))] for s in range(len(states)) ]
        
    for p in range(len(x) - 1):
        next_x = x[p + 1]

        for s in range(len(states)):
            M[s][p + 1] = M[0][p] * transition[ states[0] ][ states[s] ] * emission[ states[s] ][ next_x ]

        for s in range(1, len(states)):
            for next_s in range(len(states)):
                M[next_s][p + 1] += M[s][p] * transition[ states[s] ][ states[next_s] ] * emission[ states[next_s] ][ next_x ]
    prob_x = 0
    for s in range(len(states)):
        prob_x += M[s][len(x) - 1]
    return prob_x

if __name__ == "__main__":
    x = sys.stdin.readline().strip()
    sys.stdin.readline() # delimiter

    sigma = sys.stdin.readline().strip().split()
    sys.stdin.readline() # delimiter

    states = sys.stdin.readline().strip().split()
    sys.stdin.readline() # delimiter

    chars = sys.stdin.readline().strip().split() 
    transition = [sys.stdin.readline().strip().split() for _ in range(len(states))]
    transition = {line[0]:dict(zip(chars, map(float,line[1:]))) for line in transition}
    sys.stdin.readline() # delimiter

    chars = sys.stdin.readline().strip().split() 
    emission = [sys.stdin.readline().strip().split() for _ in range(len(states))]
    emission = {line[0]:dict(zip(chars, map(float,line[1:]))) for line in emission}

    print(outcome_likelihood(x,sigma,states,transition,emission))

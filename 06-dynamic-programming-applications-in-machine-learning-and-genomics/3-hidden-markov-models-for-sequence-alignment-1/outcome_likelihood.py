import sys

def outcome_likelihood(x,sigma,states,transition,emission):
    
    return 0

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

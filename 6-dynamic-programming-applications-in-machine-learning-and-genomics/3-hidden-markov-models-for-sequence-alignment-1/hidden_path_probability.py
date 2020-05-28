import sys

def path_probability(pi, states, transition):
    """Computes probability of a path pi through a given HMM.

    Make sure that your output is to at least three significant figures.

    Args:
        pi: A string containg the path.
        states: A list of strings containing all possible states
        transition: A 2D dictionary s.t. transition[x][y] is the
            probability of transitioning from state x to state y.

    Returns:
        A float with the probability to at least three significant figures.
    """
    # TODO: your code here
    return 0.0

if __name__ == "__main__":
    pi = sys.stdin.readline().strip()
    sys.stdin.readline() # delimiter

    states = sys.stdin.readline().strip().split()
    sys.stdin.readline() # delimiter

    chars = sys.stdin.readline().strip().split() # first row of trans mat
    transition = {line[0]: dict(zip(chars, map(float,line.strip().split()[1:]))) 
            for line in sys.stdin}

    print(path_probability(pi,states,transition))

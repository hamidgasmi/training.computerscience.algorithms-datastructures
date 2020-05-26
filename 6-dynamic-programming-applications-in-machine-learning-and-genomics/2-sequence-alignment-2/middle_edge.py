import sys

def middle_edge(m,mu,sigma,s,t):
    """
    m, mu, and sigma are the scoring parameters
    s and t are the strings to be aligned

    return a string with the middle edge's nodes
    be sure to follow the output format for this problem
    """
    # TODO: your code here
    return ""

if __name__ == "__main__":
    m,mu,sigma = map(int, sys.stdin.readline().strip().split())
    s,t = [sys.stdin.readline().strip() for _ in range(2)]
    print(middle_edge(m,mu,sigma,s,t))

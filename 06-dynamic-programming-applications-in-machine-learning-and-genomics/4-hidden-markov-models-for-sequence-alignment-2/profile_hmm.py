import sys


def profile_hmm(theta, sigma, alignment):
    """Creates a profile HMM from a multiple alignment.

    Args:
        theta: A float threshold for the seed alignment
        sigma: A list of strings containing the HMM alphabet
        alignment: A list of strings containing the multiple alignment
            for which the profile HMM will be constructed

    Returns:
        A string with the emission and transition matrices formatted
            according to the problem output specification.
    """
    # TODO: your code here
    return ""


if __name__ == "__main__":
    theta = float(sys.stdin.readline().strip())
    sys.stdin.readline()  # delimiter

    sigma = sys.stdin.readline().strip().split()
    sys.stdin.readline()  # delimiter

    alignment = [line.strip() for line in sys.stdin]

    print(profile_hmm(theta, sigma, alignment))

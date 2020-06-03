import sys

def reconstruct(k, d, paired_comp):
    """Reconsructs a string from its gapped genome path

    Args:
        k:              length of the k-mers in each (k,d)-mer
        d:              length of the gap
        paired_comp:    (k,d)-mers that make up the target string

    Returns:
        a string that matches the gapped genome path
    """
    # TODO: your code here
    return ""

if __name__ == "__main__":
    k, d = map(int, sys.stdin.readline().strip().split())
    paired_comp = [line.strip() for line in sys.stdin if line.strip()]

    print(reconstruct(k, d, paired_comp))

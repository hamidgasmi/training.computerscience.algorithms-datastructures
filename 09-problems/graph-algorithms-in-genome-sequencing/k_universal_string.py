import sys
import itertools
import string_reconstruction

def k_universal(k):
    
    format = "{0:0=" + str(k) + "b}"
    patterns = [format.format(combination[0]) for combination in itertools.product(range(2**k))]
    
    de_bruijn_graph = string_reconstruction.De_Bruijn_Graph(k, patterns)
    text = de_bruijn_graph.string_reconstruct()
    
    return text[:len(text) - k + 1]
    
if __name__ == "__main__":
    k = int(sys.stdin.readline().strip())

    print(k_universal(k))

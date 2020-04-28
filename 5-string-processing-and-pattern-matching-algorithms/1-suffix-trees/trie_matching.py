import sys
import trie

if __name__ == "__main__":

    text = sys.stdin.readline ().strip ()
    n = int (sys.stdin.readline ().strip ())
    patterns = []
    for i in range (n):
	    patterns += [sys.stdin.readline ().strip ()]

    trie = trie.Trie(patterns)
    ans = trie.multi_pattern_matching(text)
    #ans = solve (text, n, patterns)

    sys.stdout.write (' '.join (map (str, ans)) + '\n')

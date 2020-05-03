# python3
import sys
import suffix_tree
from collections import namedtuple
import threading

# DFS traversal on the tree
def dfs_non_shared_substring(st, node):

	if len(st.nodes[node]) == 0:
		return (-1, 0, False)
	
	text_len = (len(suffix_tree.text) - 2) // 2
	shortest_substr_end = 0
	shortest_substr_len = 2001
	right_part = False
	for child in st.nodes[node]:
		
		if st.nodes[node][child].start >= text_len:
			right_part = True if st.nodes[node][child].start > text_len else right_part
			continue
		
		(substr_end, substr_len, subright_part) = dfs_non_shared_substring(suffix_tree, child)
		right_part = True if subright_part else right_part
		
		candidate_len = 1 if substr_len == 0 else st.nodes[node][child].len + substr_len
		candidate_end = st.nodes[node][child].start if substr_end == -1 else substr_end

		if shortest_substr_len > candidate_len:
			shortest_substr_end = candidate_end
			shortest_substr_len = candidate_len
	
	if not right_part:
		shortest_substr_end = -1
		shortest_substr_len = 0

	return (shortest_substr_end, shortest_substr_len, right_part)

def solve (p, q):
	pq_text = p + "#" + q + "$"

	st = suffix_tree.Suffix_Tree(pq_text)
	(shortest_substr_end, shortest_substr_len, right_part) = dfs_non_shared_substring(st, 0)

	return st.text[ shortest_substr_end -  shortest_substr_len + 1 : shortest_substr_end + 1 ]

def main():
	p = sys.stdin.readline ().strip ()
	q = sys.stdin.readline ().strip ()

	ans = solve (p, q)
	sys.stdout.write (ans + '\n')

if __name__ == "__main__":

	sys.setrecursionlimit(10**7)
	threading.stack_size(2**30)
	threading.Thread(target=main()).start()


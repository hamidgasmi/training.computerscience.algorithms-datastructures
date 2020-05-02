# python3
import sys
import suffix_tree
import queue
from collections import namedtuple

Edge = namedtuple('Edge', ['parent', 'node', 'start', 'len'])
max_len = 2001

# BFS traversal on the tree
def dfs_non_shared_substring(suffix_tree, node):

	if len(suffix_tree.nodes[node]) == 0:
		return (node, 0, False)
	
	text_len = (len(suffix_tree.text) - 2) // 2
	shortest_substr_start = 0
	shortest_substr_len = max_len
	right_part = False
	for child in suffix_tree.nodes[node]:
		
		if suffix_tree.nodes[node][child].start >= text_len:
			right_part = True if suffix_tree.nodes[node][child].start > text_len else right_part
			continue
		
		(substr_start, substr_len, subright_part) = dfs_non_shared_substring(suffix_tree, child)
		right_part = True if subright_part else right_part

		if shortest_substr_len > suffix_tree.nodes[node][child].len + substr_len:
			shortest_substr_start = suffix_tree.nodes[node][child].start
			shortest_substr_len = 1 if substr_len == 0 else suffix_tree.nodes[node][child].len + substr_len
	
	if not right_part:
		shortest_substr_len = 0
	elif shortest_substr_len == 0:
		shortest_substr_len = 1

	return (shortest_substr_start, shortest_substr_len, right_part)

def solve (p, q):
	pq_text = p + "#" + q + "$"
	
	suffixTree = suffix_tree.Suffix_Tree(pq_text)
	#print(suffixTree.nodes)

	(shortest_substr_start, shortest_substr_len, right_part) = dfs_non_shared_substring(suffixTree, 0)
	
	return suffixTree.text[ shortest_substr_start : shortest_substr_start + shortest_substr_len ]

if __name__ == "__main__":
	p = sys.stdin.readline ().strip ()
	q = sys.stdin.readline ().strip ()

	ans = solve (p, q)
	sys.stdout.write (ans + '\n')

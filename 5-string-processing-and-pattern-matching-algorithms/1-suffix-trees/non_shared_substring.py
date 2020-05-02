# python3
import sys
import suffix_tree
import queue
from collections import namedtuple

Edge = namedtuple('Edge', ['parent', 'node', 'start', 'len'])

# BFS traversal on the tree
def non_shared_substring(suffix_tree, len_text):

	fifo = queue.Queue()
	edge = Edge(-1, 0, 0, 0)
	fifo.put(edge)

	while not fifo.empty():

		parent_edge = fifo.get()
		node = parent_edge.node
		parent = parent_edge.parent

		right_part = False
		end_left_part = True
		for child in suffix_tree.nodes[node]:

			child_edge = suffix_tree.nodes[node][child]

			right_part = True if child_edge.start > len_text else right_part
			end_left_part = end_left_part if child_edge.start == len_text else False

			if child_edge.start >= len_text:
				continue
			
			current_len = 0 if parent == -1 else suffix_tree.nodes[parent][node].len
			edge = Edge(node, child, parent_edge.start, current_len + parent_edge.len)
			fifo.put(edge)

		if len(suffix_tree.nodes[node]) == 0:
			print("Over here 2")
			edge = Edge(parent, node, parent_edge.start, parent_edge.len + 1)
			break

		elif (not right_part) and end_left_part:
			print("Over here 1: ", suffix_tree.nodes[node])
			edge = Edge(parent, node, parent_edge.start, parent_edge.len)
			break

	return suffix_tree.text[edge.start:edge.start + edge.len]
	
def solve (p, q):
	pq_text = p + "#" + q + "$"
	
	suffixTree = suffix_tree.Suffix_Tree(pq_text)
	print(suffixTree.nodes)

	result = non_shared_substring(suffixTree, len(p))
	
	return result

if __name__ == "__main__":
	p = sys.stdin.readline ().strip ()
	q = sys.stdin.readline ().strip ()

	ans = solve (p, q)
	sys.stdout.write (ans + '\n')

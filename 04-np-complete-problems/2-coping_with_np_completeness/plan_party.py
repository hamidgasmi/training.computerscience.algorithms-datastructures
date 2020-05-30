#uses python3
import sys
import threading

# This problem can be reduced to Independent Set problem (ISP) which is an NP problem
# It's a special case of ISP 
# It's can be solved effeciently with Greedy Algorithm technique:
# Greedy Choice: Select all leaves of the tree and Remove all their parents + Iterate
# This choice is safe: 
#   since the number of leaves >= the leaves' parents
#   This choice guarantees to get an IS longer or equal to the IS that we would have got if we selected the parents

class Tree:
    def __init__(self, size, edges):
        self.size = size
        self.build_children_list(edges)

    def build_children_list(self, edges):
        self.children_list = [[] for _ in range(self.size)]
        for p, c in edges:
            self.children_list[p - 1].append(c - 1)
            self.children_list[c - 1].append(p - 1)

    def isp_dfs(self, v, parent):

        list = []
        return list
        
def main():
    
    size = int(input())
    edges = []
    for _ in range(1, size):
        edges.append(list(map(int, input().split())))
    tree = Tree(size, edges)

    isp_list = tree.isp_dfs(0, -1)
    print(len(isp_list))
    print(isp_list)

if __name__ == "__main__":
    
    # To avoid stack overflow issues
    sys.setrecursionlimit(10**6) # max depth of recursion
    threading.stack_size(2**26)  # new thread will get stack of such size

    # This is to avoid stack overflow issues
    threading.Thread(target=main).start()

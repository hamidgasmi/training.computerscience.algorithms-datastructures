#uses python3
import sys
import threading

# This problem can be reduced to Independent Set problem (ISP) which is an NP problem
# It's a special case of ISP 
# It's can be solved effeciently with Dynamic Programming technique:
# Let's W(v) reprensents the Total Fun (weight) in the party, then:
# F(v) = Max(weight(v) + sum(weight(u) for all u grand-children of v),
#                        sum(weight(u) for all u children of v))

class Vertex:
    def __init__(self, weight):
        self.weight = weight
        self.children = []

class Tree:
    def __init__(self, size, weights):
        self.size = size
        self.weights = [weights[i] for i in range(size)]

        
def ReadTree():
    
    

def dfs(tree, vertex, parent):
    for child in tree[vertex].children:
        if child != parent:
            dfs(tree, child, vertex)

    # This is a template function for processing a tree using depth-first search.
    # Write your code here.
    # You may need to add more parameters to this function for child processing.


def MaxWeightIndependentTreeSubset(tree):
    size = len(tree)
    if size == 0:
        return 0
    dfs(tree, 0, -1)
    # You must decide what to return.
    return 0


def main():
    tree = ReadTree()
    weight = MaxWeightIndependentTreeSubset(tree)
    print(weight)

if __name__ == "__main__":
    
    # To avoid stack overflow issues
    sys.setrecursionlimit(10**6) # max depth of recursion
    threading.stack_size(2**26)  # new thread will get stack of such size

    size = int(input())
    weights = map(int, input().split())
    print(weights)
    #tree = [Vertex(w) for w in map(int, input().split())]
    #for i in range(1, size):
    #    a, b = list(map(int, input().split()))
    #    tree[a - 1].children.append(b - 1)
    #    tree[b - 1].children.append(a - 1)
    #return tree

    # This is to avoid stack overflow issues
    #threading.Thread(target=main).start()

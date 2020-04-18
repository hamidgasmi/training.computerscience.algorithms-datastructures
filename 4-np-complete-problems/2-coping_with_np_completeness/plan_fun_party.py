import sys
import threading

# This problem can be reduced to Independent Set problem (ISP) which is an NP problem
# It's a special case of ISP 
# It's can be solved effeciently with Dynamic Programming technique:
# Let's W(v) reprensents the Total Fun (weight) in the party, then:
# F(v) = Max(weight(v) + sum(weight(u) for all u grand-children of v),
#                        sum(weight(u) for all u children of v))

class Tree:
    def __init__(self, size, weights, edges):
        self.size = size
        self.weights = weights.copy()
        self.build_children_list(edges)

    def build_children_list(self, edges):
        self.children_list = [[] for _ in range(self.size)]
        for p, c in edges:
            self.children_list[p - 1].append(c - 1)
            self.children_list[c - 1].append(p - 1)

    def total_weight_dfs(self, v, parent, total_weight):
        
        if total_weight[v] > 0:
            return

        if len(self.children_list[v]) == 0:
            total_weight[v] = self.weights[v]

        children_weight = 0
        grand_children_weight = 0
        for child in self.children_list[v]:
            if child == parent:
                continue
            
            self.total_weight_dfs(child, v, total_weight)
            children_weight += total_weight[child]

            for grand_child in self.children_list[child]:
                if grand_child == v:
                    continue

                grand_children_weight += total_weight[grand_child]

        if self.weights[v] + grand_children_weight < children_weight:
            total_weight[v] = children_weight
        else:
            total_weight[v] = self.weights[v] + grand_children_weight
        
def MaxWeightIndependentTreeSubset(tree):
    
    if tree.size == 0:
        return 0

    total_weight = [0] * tree.size
    tree.total_weight_dfs(0, -1, total_weight)
    
    return total_weight[0]

def main():
    
    size = int(input())
    weights = [w for w in map(int, input().split())]
    edges = []
    for _ in range(1, size):
        edges.append(list(map(int, input().split())))
    tree = Tree(size, weights, edges)

    weight = MaxWeightIndependentTreeSubset(tree)
    print(weight)

if __name__ == "__main__":
    
    # To avoid stack overflow issues
    sys.setrecursionlimit(10**6) # max depth of recursion
    threading.stack_size(2**26)  # new thread will get stack of such size

    # This is to avoid stack overflow issues
    threading.Thread(target=main).start()

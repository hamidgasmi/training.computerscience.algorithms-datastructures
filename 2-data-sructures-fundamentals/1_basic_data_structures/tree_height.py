import sys
import threading

class Node:
    def __init__(self, aKey):
        self.key = aKey
        self.height = 1
        self.parentNode = None
        self.children = []

    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def add_child(self, aChild):
        self.children.append(aChild)

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def add_child_with_height(self, aChild):
        self.children.append(aChild)
        aChild.parentNode = self

        if self.height <= aChild.height:
            self.height = aChild.height + 1
            aNode = self.parentNode
            aPreviousdNode = self
            while not aNode is None:
                aNode.height = max(aNode.height, aPreviousdNode.height + 1)
                aPreviousdNode = aNode
                aNode = aNode.parentNode

    # Time Complexity: O(n)
    #       Let m be the tree max child by node (E.g. 2 for binary tree)
    #       T(n) = m (n/m) + O(1)
    #       T(n) = [ 1 + m + m^2 + ... + m^log_m(n) ] * O(1)
    #       T(n) = {[1 - m * m^log_m(n)] / (1 - m)} * O(1)
    #       T(n) = {[1 - m * n] / (1 - m)} * O(1) = {1 + (n - 1) * m / (m - 1)} * O(1) m / m - 1 < 1 = C
    #       T(n) = O(n) * O(1) = O(n)
    # Space Complexity: O(log_m(n))
    def compute_height(self):
        maxheight = 0
        for i in range(len(self.children)):
            height = self.children[i].compute_height()
            if height > maxheight:
                maxheight = height
        
        return maxheight + 1

    def to_str(self):
        s = "Node: " + str(self.key) + ". Height: " + str(self.height) + ". Children: " 
        if len(self.children) == 0:
            s = s + "(None)"
        separator = ""
        for i in range(len(self.children)):
            s = s + separator + str(self.children[i].key)
            separator = ", "

        return s

# Time complexity: O(tree_max_child_by_node * n):
#       Each node is visited 1 time by the for loop and visited when its children are visited 1st time
#       This means that each node is visited at most: (tree_max_child_by_node + 1) time
#       For a binary tree, the complexity is O(n)
# Space complexity: O(n)
def build_tree(n, parents):
    nodes = [Node(-1) for i in range(n)]
    rootNode = -1
    for i in range(n):

        currentNode = i #a node
        previousNode = i #a node's child

        while currentNode != -1:
            if nodes[currentNode].key == -1:
                nodes[currentNode].key = currentNode
                parentNode = parents[currentNode]
            else:
                parentNode = -1
            
            if previousNode != currentNode:
                nodes[currentNode].add_child(nodes[previousNode])

            previousNode = currentNode
            currentNode = parentNode

        if parents[previousNode] == -1:
            rootNode = previousNode

    return nodes[rootNode]

# Time complexity: O(m * n^2):
# Space complexity: O(n) = O(n)
def build_tree_with_height(n, parents):
    nodes = [Node(-1) for i in range(n)]
    rootNode = -1
    for i in range(n):

        currentNode = i #a node
        previousNode = i #a node's child

        while currentNode != -1:
            if nodes[currentNode].key == -1:
                nodes[currentNode].key = currentNode
                parentNode = parents[currentNode]
            else:
                parentNode = -1
            
            if previousNode != currentNode:
                nodes[currentNode].add_child_with_height(nodes[previousNode]) #O(n)

            previousNode = currentNode
            currentNode = parentNode

        if parents[previousNode] == -1:
            rootNode = previousNode

    return nodes[rootNode]

#Time Complexity: O(n^2)
#Space Complexity: O(1)
def compute_height_naive(n, parents):

    max_height = 0
    for vertex in range(n):
        height = 0
        current = vertex
        while current != -1:
            height += 1
            current = parents[current]
        max_height = max(max_height, height)
    return max_height

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    #print(compute_height_naive(n, parents)) #O(n^2)
    #print(build_tree(n, parents).compute_height()) #Max time used: 0.70/3.00, max memory used: 138727424/536870912
    print(build_tree_with_height(n, parents).height) #Time used (case #18): 4.85/3.00, memory used: 42184704/536870912

if __name__ == "__main__":
    
    sys.setrecursionlimit(10**7)  # max depth of recursion
    threading.stack_size(2**27)   # new thread will get stack of such size
    threading.Thread(target=main).start()

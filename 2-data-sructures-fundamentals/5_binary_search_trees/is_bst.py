import sys, threading

# In Order Traversal of the Tree:
# Time Complexity: O(n)
# Space Complxity: O(height)
def IsBinarySearchTree(tree, v, inOrderTraversal):
  if len(tree) < 2:
    return True

  if tree[v][1] != -1 and not IsBinarySearchTree(tree, tree[v][1], inOrderTraversal):
    return False

  if len(inOrderTraversal) == 1 and inOrderTraversal[0] > tree[v][0]:
    return False
  
  if len(inOrderTraversal) == 0:
    inOrderTraversal.append(tree[v][0])
  else:
    inOrderTraversal[0] = tree[v][0]

  if tree[v][2] == -1:
    return True
  else:
    return IsBinarySearchTree(tree, tree[v][2], inOrderTraversal)

def main():
  nodes = int(sys.stdin.readline().strip())

  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))

  inOrderTraversal = []
  if IsBinarySearchTree(tree, 0, inOrderTraversal):
    print("CORRECT")
  else:
    print("INCORRECT")

if __name__ == '__main__':
  sys.setrecursionlimit(10**7) # max depth of recursion
  threading.stack_size(2**27)  # new thread will get stack of such size
  threading.Thread(target=main).start()

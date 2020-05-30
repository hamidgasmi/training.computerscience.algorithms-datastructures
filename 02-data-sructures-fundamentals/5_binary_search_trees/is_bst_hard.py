import sys, threading

# In Order Traversal of the Tree:
# Time Complexity: O(n)
# Space Complxity: O(height)
def IsBinarySearchTree(tree, v, subtreeMinMax):
  if len(tree) < 2:
    return True
  
  vSubtreeMinMax = []
  if tree[v][1] == -1:
    subtreeMinMax[0] = tree[v][0]
  else:
    vSubtreeMinMax = [0,0]
    if not IsBinarySearchTree(tree, tree[v][1], vSubtreeMinMax):
      return False
    elif vSubtreeMinMax[1] >= tree[v][0]:
      return False
    else:
      subtreeMinMax[0] = vSubtreeMinMax[0]

  if tree[v][2] == -1:
    subtreeMinMax[1] = tree[v][0]
  else:
    vSubtreeMinMax = [0,0]
    if not IsBinarySearchTree(tree, tree[v][2], vSubtreeMinMax):
      return False
    elif vSubtreeMinMax[0] < tree[v][0]:
      return False
    else:
      subtreeMinMax[1] = vSubtreeMinMax[1]
  
  return True

def main():
  nodes = int(sys.stdin.readline().strip())

  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))

  subtreeMinMax = [0,0]
  if IsBinarySearchTree(tree, 0, subtreeMinMax):
    print("CORRECT")
  else:
    print("INCORRECT")

if __name__ == '__main__':
  sys.setrecursionlimit(10**7) # max depth of recursion
  threading.stack_size(2**27)  # new thread will get stack of such size
  threading.Thread(target=main).start()

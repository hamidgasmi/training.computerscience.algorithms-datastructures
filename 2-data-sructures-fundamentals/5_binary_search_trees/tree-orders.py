import sys, threading

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  # Time Complexity: O(n)
  # Space Complexity: O(tree height)
  def inOrderTraversal(self, v):
    if v == -1:
        return
            
    if self.left[v] != -1:
        self.inOrderTraversal(self.left[v])
        
    self.result.append(self.key[v])
        
    if self.right[v] != -1:
        self.inOrderTraversal(self.right[v])
            
  def inOrder(self):
    self.result = []
    self.inOrderTraversal(0)
    return self.result

  # Time Complexity: O(n)
  # Space Complexity: O(tree height)
  def preOrderTraversal(self, v):
    if v == -1:
        return

    self.result.append(self.key[v])

    if self.left[v] != -1:
        self.preOrderTraversal(self.left[v])
        
    if self.right[v] != -1:
        self.preOrderTraversal(self.right[v])

  def preOrder(self):
    self.result = []
    self.preOrderTraversal(0)
    return self.result

  # Time Complexity: O(n)
  # Space Complexity: O(tree height)
  def postOrderTraversal(self, v):
    if v == -1:
        return

    if self.left[v] != -1:
        self.postOrderTraversal(self.left[v])
        
    if self.right[v] != -1:
        self.postOrderTraversal(self.right[v])

    self.result.append(self.key[v])

  def postOrder(self):
    self.result = []
    self.postOrderTraversal(0)
    return self.result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

if __name__ == '__main__':
    
    sys.setrecursionlimit(10**6) # max depth of recursion
    threading.stack_size(2**27)  # new thread will get stack of such size

    threading.Thread(target=main).start()

# python3
from sys import stdin

# Splay tree implementation

# Vertex of a splay tree
class Vertex:

  def str(self):
    return "(key, sum, left, right, parent) = (" + str(self.key) + "," + str(self.sum) + "," + \
      ("None" if self.left == None else str(self.left.key)) + "," + \
      ("None" if self.right == None else str(self.right.key)) + "," + \
      ("None" if self.parent == None else str(self.parent.key)) + ")"

  def __init__(self, key, sum, left, right, parent):
    (self.key, self.sum, self.left, self.right, self.parent) = (key, sum, left, right, parent)

def update(v):
  if v == None:
    return
  v.sum = v.key + (v.left.sum if v.left != None else 0) + (v.right.sum if v.right != None else 0)
  if v.left != None:
    v.left.parent = v
  if v.right != None:
    v.right.parent = v

def smallRotation(v):
  parent = v.parent
  if parent == None:
    return
  grandparent = v.parent.parent
  if parent.left == v:
    m = v.right
    v.right = parent
    parent.left = m
  else:
    m = v.left
    v.left = parent
    parent.right = m
  update(parent)
  update(v)
  v.parent = grandparent
  if grandparent != None:
    if grandparent.left == parent:
      grandparent.left = v
    else: 
      grandparent.right = v

def bigRotation(v):
  if v.parent.left == v and v.parent.parent.left == v.parent:
    # Zig-zig
    smallRotation(v.parent)
    smallRotation(v)
  elif v.parent.right == v and v.parent.parent.right == v.parent:
    # Zig-zig
    smallRotation(v.parent)
    smallRotation(v)    
  else: 
    # Zig-zag
    smallRotation(v)
    smallRotation(v)

# Makes splay of the given vertex and makes
# it the new root.
def splay(v):
  if v == None:
    return None
  while v.parent != None:
    if v.parent.parent == None:
      smallRotation(v)
      break
    bigRotation(v)
  return v

# Searches for the given key in the tree with the given root
# and calls splay for the deepest visited node after that.
# Returns pair of the result and the new root.
# If found, result is a pointer to the node with the given key.
# Otherwise, result is a pointer to the node with the smallest
# bigger key (next value in the order).
# If the key is bigger than all keys in the tree,
# then result is None.
def find(root, key): 
  v = root
  last = root
  next = None
  while v != None:
    if v.key >= key and (next == None or v.key < next.key):
      next = v    
    last = v
    if v.key == key:
      break    
    if v.key < key:
      v = v.right
    else: 
      v = v.left      
  root = splay(last)
  return (next, root)

def split(root, key):  
  (result, root) = find(root, key)  
  if result == None:    
    return (root, None)  
  right = splay(result)
  left = right.left
  right.left = None
  if left != None:
    left.parent = None
  update(left)
  update(right)
  return (left, right)
  
def merge(left, right):
  if left == None:
    return right
  if right == None:
    return left
  while right.left != None:
    right = right.left
  right = splay(right)
  right.left = left
  update(right)
  return right
  
# Code that uses splay tree to solve the problem
root = None

def insert(x):
  global root
  (left, right) = split(root, x)
  new_vertex = None
  if right == None or right.key != x:
    new_vertex = Vertex(x, x, None, None, None)  
  root = merge(merge(left, new_vertex), right)
  
def erase(x): 
  global root
  (left, right) = split(root, x)
  
  #print("left: ", left.str())
  
  if right == None:
    return
  elif right.key == x:
    (xleft, xright) = split(right, x + 1)
    right = xright
    
  root = merge(left, right)

def search(x): 
  global root
  (result, root) = find(root, x)

  if result == None:
    return False
  elif result.key == x:
    return True
  else:
    return False
  
def sum(fr, to): 
  global root

  if fr > to:
    return 0
  #print("fr:", fr)
  #print("to:", to)
  (left, middle) = split(root, fr)
  if middle == None:
    #print("middle 1: None")
    return 0
  #else:
  #  print("middle 1: ", middle.str())

  (middle, right) = split(middle, to + 1)
  #if right == None:
    #print("right: None")
  #else:
    #print("right: ", right.str())

  if middle == None:
    ans = 0
  else:
    ans = middle.sum
    #print("middle 2: ", middle.str())

  middle = merge(left, middle)

  root = merge(middle, right)

  return ans

MODULO = 1000000001
n = int(stdin.readline())
last_sum_result = 0
for i in range(n):
  line = stdin.readline().split()
  if line[0] == '+':
    x = int(line[1])
    #print("Command: ", "+ " + line[1] + " ===> + " + str((x + last_sum_result) % MODULO))
    insert((x + last_sum_result) % MODULO)
    #print("root ", "None" if root == None else root.str())
  elif line[0] == '-':
    x = int(line[1])
    #print("Command: ", "- " + line[1] + " ===> - " + str((x + last_sum_result) % MODULO))
    erase((x + last_sum_result) % MODULO)
    #print("root ", "None" if root == None else root.str())
  elif line[0] == '?':
    x = int(line[1])
    #print("Command: ", "? " + line[1] + " ===> ? " + str((x + last_sum_result) % MODULO))
    print('Found' if search((x + last_sum_result) % MODULO) else 'Not found')
    #print("root ", "None" if root == None else root.str())
  elif line[0] == 's':
    l = int(line[1])
    r = int(line[2])
    #print("Command: ", "s " + line[1] + " " + line[2] + " ===> s " + str((l + last_sum_result) % MODULO) + " " + str((r + last_sum_result) % MODULO))
    res = sum((l + last_sum_result) % MODULO, (r + last_sum_result) % MODULO)
    print(res)
    last_sum_result = res % MODULO
    #print("root ", "None" if root == None else root.str())
# python3
import sys

# Splay tree implementation

# Vertex of a splay tree
class Vertex:

  def __init__(self, key, left, right, parent):
    (self.key, self.left, self.right, self.parent) = (key, left, right, parent)
    self.rank = 1
    self.size = 1

  def str(self):
      return "(key, rank, size, left, right) = (" + str(self.key) + "," + str(self.rank) + ","  + str(self.size) + "," + \
      ("None" if self.left == None else str(self.left.key)) + "," + \
      ("None" if self.right == None else str(self.right.key)) + ")"
      
  def update(self):
      self.size = 1 + (self.left.size if self.left != None else 0) \
                    + (self.right.size if self.right != None else 0)
      self.rank = 1 + (self.left.size if self.left != None else 0)

      if self.left != None:
          self.left.parent = self

      if self.right != None:
          self.right.parent = self

  def smallRotation(self):
      parent = self.parent
      if parent == None:
          return
      grandparent = self.parent.parent
      if parent.left == self:
          m = self.right
          self.right = parent
          parent.left = m
      else:
          m = self.left
          self.left = parent
          parent.right = m
      parent.update()
      self.update()
      self.parent = grandparent
      if grandparent != None:
          if grandparent.left == parent:
              grandparent.left = self
          else: 
              grandparent.right = self
          grandparent.update()

  def bigRotation(self):
      if self.parent.left == self and self.parent.parent.left == self.parent:
        # Zig-zig
        self.parent.smallRotation()
        self.smallRotation()
      elif self.parent.right == self and self.parent.parent.right == self.parent:
        # Zig-zig
        self.parent.smallRotation()
        self.smallRotation()
      else: 
        # Zig-zag
        self.smallRotation()
        self.smallRotation()


class Rope:
  def __init__(self, s):
      self.s = s
      self.root = None
      for i in range(len(s)):
          self.insert(i)
  
  def update(self, v):
      if v == None:
          return
      else:
          v.update()
  
  def insert(self, i):
      new_vertex = Vertex(i, None, None, None)
      if self.root != None:
          new_vertex.left = self.root
          new_vertex.update()
      self.root = new_vertex
  
  def splay(self, v):
      if v == None:
          return None
      while v.parent != None:
          if v.parent.parent == None:
              v.smallRotation()
              break
          v.bigRotation()
      return v

  def find(self, root, index): 
      v = root
      last = root
      next = None
      while v != None:
          if v.rank >= index and (next == None or v.rank < next.rank):
              next = v    
          last = v
          if v.rank == index:
            break    
          if v.rank < index:
            index -= v.rank
            v = v.right
            
          else: 
              v = v.left      
      root = self.splay(last)
      return (next, root)

  def split(self, root, index):  
      (result, root) = self.find(root, index)
      if result == None:    
        return (root, None)

      right = self.splay(result)
      left = right.left
      right.left = None
      if left != None:
          left.parent = None
          left.update()
      right.update()
      return (left, right)
  
  def merge(self, left, right):
      if left == None:
          return right
      if right == None:
          return left
      while right.left != None:
          right = right.left
      right = self.splay(right)
      right.left = left
      right.update()
      return right
  
  def printRope(self, v, new_s):
      if v == None:
          return
      
      if v.left != None:
          self.printRope(v.left, new_s)
      
      new_s.append(self.s[v.key])

      if v.right != None:
          self.printRope(v.right, new_s)

  def result(self):
      new_s = []
      self.printRope(self.root, new_s)

      new_str = ""
      return new_str.join(new_s)

  def process(self, i, j, k):

      (left, middle) = self.split(self.root, i + 1)
      (middle, right) = self.split(middle, j - i + 2)
      self.root = self.merge(left, right)
      (left, right) = self.split(self.root, k + 1)
      self.root = self.merge(left, middle)
      self.root = self.merge(self.root, right)
      
if __name__ == '__main__':
    rope = Rope(sys.stdin.readline().strip())
    q = int(sys.stdin.readline())
    for _ in range(q):
        i, j, k = map(int, sys.stdin.readline().strip().split())
        rope.process(i, j, k)
        print(rope.result())
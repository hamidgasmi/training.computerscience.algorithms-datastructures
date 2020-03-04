# python3
import sys

class Vertex:
  def __init__(self, key, index, left, right, parent):
      self.key = key
      self.index = index
      self.left = left
      self.right = right
      self.parent = parent

  def grandParent(self):
      if self.parent == None:
          return None
      else:
          return self.parent.parent

  def update(self):
      if self.left != None:
          self.left.parent = self
      
      if self.right != None:
          self.right.parent = self

class Rope:
  def __init__(self, s):
      self.s = s
      self.root = None
      for i in range(len(s)):
          self.insert(i, s[i])
  
  def update(self, v):
      if v == None:
          return
      else:
          v.update()

  def smallRotation(self, v):
      if v == None:
          return
    
      parent = v.parent()
      if parent == None:
          return

      grandparent = v.grandParent()
      if parent.left == v:
          m = v.right
          v.right = parent
          parent.left = m
      else:
          m = v.left()
          v.left = parent
          parent.right = m
      parent.update()
      v.update()

      v.parent = grandparent
      if grandparent != None:
          if grandparent.left == parent:
              grandparent.left = v
          else: 
              grandparent.right = v

  def bigRotation(self, v):
      if v == None:
          return
          
      p = v.parent()
      q = v.grandParent()
      if p == None or q == None:
          return
      
      if (p == q.left() and v == p.left()) or \
         (p == q.right() and v == q.right()):
         # Zig-Zig
          self.smallRotation(p)
          self.smallRotation(v)
      elif (p == q.left() and v == q.right() or 
            p == q.right() and v == p.left()):
          # Zig-Zag
          self.smallRotation(v)
          self.smallRotation(v)

  def splay(self, v):
      if v == None:
        return None

      while v.parent != None:
        if v.parent.parent == None:
            self.smallRotation(v)
            break
        self.bigRotation(v)

      return v

  def find(self, key): 
      v = self.root
      last = self.root
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
      self.root = self.splay(last)
      return (next)

  def split(self, v, key):
      pass
  
  def split(self, key):  
      result = self.find(key)  
      if result == None:    
          return (self.root, None)
  
      right = self.splay(result)
      left = right.left
      right.left = None
      if left != None:
          left.parent = None
      self.update(left)
      self.update(right)
      return (left, right)

  def merge(self, v1, v2):
      pass

  def insert(self, i, c):
      (left, right) = self.split(self.root, i)
      new_vertex = None
      if right == None or right.key != i:
          new_vertex = Vertex(i, i, None, None, None)  
      self.root = merge(merge(left, new_vertex), right)

  def result(self):
      return self.s

  def process(self, i, j, k):
      pass

if __name__ == '__main__':         
    rope = Rope(sys.stdin.readline().strip())
    q = int(sys.stdin.readline())
    for _ in range(q):
        i, j, k = map(int, sys.stdin.readline().strip().split())
        rope.process(i, j, k)
    print(rope.result())

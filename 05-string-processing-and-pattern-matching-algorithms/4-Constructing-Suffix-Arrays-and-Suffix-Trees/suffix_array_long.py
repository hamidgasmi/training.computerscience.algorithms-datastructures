# python3
import sys

class Suffix_Array:
  def __init__(self, text):
    
    self.text = text
    self.text_len = len(text)
    self.alphabet = {"$":0, "A":1, "C":2, "G":3, "T":4}
    
    self.Order = [0 for _ in range(self.text_len)]
    self.Class = [0 for _ in range(self.text_len)]

    self.count = [0 for _ in range(self.text_len)]
    self.newOrder = [0 for _ in range(self.text_len)]
    self.newClass = [0 for _ in range(self.text_len)]

    self.build_suffix_array()

  def sort_characters(self):
    
    count = [0 for _ in range(len(self.alphabet))]
    for i in range(self.text_len):
      index = self.alphabet[self.text[i]]
      count[index] = count[index] + 1

    for i in range(1, len(self.alphabet), 1):
      count[i] += count[i-1]
    
    for i in range(self.text_len - 1, -1, -1):
      index = self.alphabet[self.text[i]]
      count[index] -= 1

      self.Order[ count[index] ] = i
  
  def compute_char_classes(self):
    
    self.Class[self.Order[0]] = 0
    for i in range(1, self.text_len, 1):
            
      self.Class[self.Order[i]] = self.Class[self.Order[i-1]]
      if self.text[self.Order[i]] != self.text[self.Order[i-1]]:
        self.Class[self.Order[i]] += 1

  def sort_doubled(self, L):
    
    for i in range(self.text_len):
      self.count[i] = 0

    for i in range(self.text_len):
      self.count[self.Class[i]] += 1

    for i in range(1, self.text_len, 1):
      self.count[i] += self.count[i-1]
    
    for i in range(self.text_len-1, -1, -1):
      start = (self.Order[i] - L + self.text_len) % self.text_len
      cl = self.Class[start] 
      self.count[cl] -= 1
      self.newOrder[self.count[cl]] = start

    tmp = self.Order
    self.Order = self.newOrder
    self.newOrder = tmp
  
  def update_classes(self, L):
    
    self.newClass[ self.Order[0] ] = 0

    for i in range(1, self.text_len, 1):
      cur = self.Order[i]
      mid = (cur + L) % self.text_len
      prev = self.Order[i - 1] 
      midPrev = (prev + L) % self.text_len

      self.newClass[cur] = self.newClass[prev]
      if not (self.Class[cur] == self.Class[prev] and self.Class[mid] == self.Class[midPrev]):
        self.newClass[cur] += 1

    tmp = self.Class
    self.Class = self.newClass
    self.newClass = tmp
      
  def build_suffix_array(self):

    self.sort_characters()
    self.compute_char_classes()
    L = 1
    while L < self.text_len:
      self.sort_doubled(L)
      self.update_classes(L)
      L *= 2

    return self.Order

if __name__ == '__main__':
  
  suffix_array = Suffix_Array(sys.stdin.readline().strip())

  print(" ".join(map(str, suffix_array.Order)))

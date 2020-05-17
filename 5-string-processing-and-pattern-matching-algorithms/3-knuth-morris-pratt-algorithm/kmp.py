import sys

class Knuth_Morris_Pratt:
  def __init__(self, text, pattern):
    self.pattern = pattern
    self.pattern_len = len(pattern)
    self.text = text

  def build_text(self):

    text_list = [ self.pattern[i] for i in range(len(self.pattern)) ]
    text_list.append("$")
    for i in range(len(self.text)):
      text_list.append(self.text[i])

    return text_list

  def compute_prefix(self, S):
    
    border = 0
    prefix = [0 for _ in range(len(S))]
    for i in range(1, len(S)):
      while border > 0 and S[i] != S[border]:
        border = prefix[border - 1]

      if S[i] == S[border]:
        border += 1
      else:
        border = 0
      prefix[i] = border
    
    return prefix
    
  def find_pattern(self):

    S = self.build_text()
    prefix = self.compute_prefix(S)

    result  = []
    for i in range(self.pattern_len + 1, len(S), 1):
      if prefix[i] == self.pattern_len:
        result.append(i - 2 * self.pattern_len)

    return result

if __name__ == '__main__':
  pattern = sys.stdin.readline().strip()
  text = sys.stdin.readline().strip()

  kmp = Knuth_Morris_Pratt(text, pattern)

  print(" ".join(map(str, kmp.find_pattern())))

import sys

class Burrows_Wheeler:

    def __init__(self, bwt_text):
        self.alphabet = dict()
        self.alphabet["$"] = 0
        self.alphabet["A"] = 1
        self.alphabet["C"] = 2
        self.alphabet["G"] = 3
        self.alphabet["T"] = 4

        #self.BWT_text_list = bwt_text
        self.last_column = [bwt_text[i] for i in range(len(bwt_text))]
        
        self.first_column = [bwt_text[i] for i in range(len(bwt_text))]
        self.count_sort(self.first_column)

        self.first_occurence = []
        self.compute_first_occurence()

        self.occ_counts_before = []
        self.compute_counts_before()
        
    # O(|Text|)
    def count_sort(self, char_list):
        count = [0 for _ in range(len(self.alphabet))]

        for c in char_list:
            i = self.alphabet[c]
            count[i] += 1
        
        i = 0
        for c in self.alphabet:
            index = self.alphabet[c]
            for _ in range(count[index]):
                char_list[i] = c
                i += 1
    # For each character C in bwt, first_occurence[C] is the 1st position of C in the sorted array of all characters of the text
    # O(|Text|)
    def compute_first_occurence(self):

      self.first_occurence = [-1 for i in range(len(self.alphabet))]
      for i in range(len(self.first_column)):
        c = self.first_column[i]
        alphabet_no = self.alphabet[c]
        if self.first_occurence[alphabet_no] == -1:
          self.first_occurence[alphabet_no] = i

    # occ_count_before: For each character C in bwt and each position P in bwt:
    #... occ_count_before[C][P] is the # of occurrences of C in bwt from position 0 to position P inclusive
    # O(|Text|)
    def compute_counts_before(self):
      
      count = [0 for _ in range(len(self.alphabet))]
      self.occ_counts_before.append(count.copy())

      for i in range(len(self.last_column)):

        c = self.last_column[i]
        alphabet_no = self.alphabet[c]

        count[alphabet_no] += 1
        self.occ_counts_before.append(count.copy())

    # Compute the # of occurrences of string pattern in the text given only Burrows-Wheeler Transform of the text
    # O(|Text|)
    def betterBWMatching(self, pattern):
      
      if len(pattern) == 0:
        return 0

      p = len(pattern) - 1

      top = 0
      bottom = len(self.last_column) - 1

      while top <= bottom:

        if p == -1:
          return bottom - top + 1

        pattern_c = pattern[p]
        p -= 1
        alphabet_no = self.alphabet[pattern_c]

        top = self.first_occurence[alphabet_no] + self.occ_counts_before[top][alphabet_no]
        bottom = self.first_occurence[alphabet_no] + self.occ_counts_before[bottom + 1][alphabet_no] - 1

      return 0
    
    def betterBW_MultipleMatching(self, patterns):

      occurrence_counts = []
      for pattern in patterns:
        occurrence_counts.append(self.betterBWMatching(pattern))

      return occurrence_counts

def CountOccurrences(pattern, bwt, starts, occ_counts_before):
  
  # Implement this function yourself
  return 0
     
if __name__ == '__main__':
  bwt_text = sys.stdin.readline().strip()
  pattern_count = int(sys.stdin.readline().strip())
  patterns = sys.stdin.readline().strip().split()

  bwt = Burrows_Wheeler(bwt_text)
 
  occurrence_counts = bwt.betterBW_MultipleMatching(patterns)
  print(' '.join(map(str, occurrence_counts)))

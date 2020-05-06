# python3
import sys

class Burrows_Wheeler:

    def __init__(self, text):
        self.BWT_Text = ""
        self.transofrm(text)

    def cycle_rotations(self, text):

        self.M = []
        self.M.append(text)
        text_len = len(text)

        for _ in range(text_len - 1):
            
            m_len = len(self.M)
            self.M.append(self.M[m_len - 1][-1] + self.M[m_len - 1][0 : text_len - 1])
    
    def transofrm(self, text):

        self.cycle_rotations(text)

        self.M.sort()

        self.BWT_Text = ''.join([self.M[i][-1] for i in range(len(self.M))])

def BWT(text):
    return ""

if __name__ == '__main__':
    text = sys.stdin.readline().strip()

    bwt = Burrows_Wheeler(text)
    
    print(bwt.BWT_Text)
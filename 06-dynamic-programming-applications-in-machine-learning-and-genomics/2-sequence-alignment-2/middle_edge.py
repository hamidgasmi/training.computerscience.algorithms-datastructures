import sys

# 1. Analysis:
#    Let FromSource(i) denote the length of the longest path from the source ending at (i, middle) and 
#    Let ToSink(i) denote the length of the longest path from (i, middle) to the sink. 
#    Length(i) = FromSource(i) + ToSink(i)
#    middle node = middle where length(middle) = max(length(i)) for i between 0 and m
# 2. Implementation: 
#    Running time: O(nm)
#    Space Complexity: O(m)
class Alignment:
    def __init__(self, match, mu, sigma):
        
        self.match = match
        self.mu = mu * (-1)
        self.sigma = sigma * (-1)
        self.global_alignment_score = 0
        self.middle_edge = ""

    def from_source(self, s, t, start_r, start_c, end_r, end_c):
        
        rows_count = end_r - start_r + 1
        columns_count = end_c - start_c + 1

        prev_from_source = [r * self.sigma for r in range(rows_count)]
        curr_from_source = [self.sigma if r == 0 else 0 for r in range(rows_count)]
        for c in range(1, columns_count, 1):
            curr_from_source[0] = prev_from_source[0] + self.sigma
            for r in range(1, rows_count, 1):
                diagonal_edge = prev_from_source[r - 1] + (self.match if s[c - 1] == t[r - 1] else self.mu)
                horizontal_edge = prev_from_source[r] + self.sigma
                vertical_edge = curr_from_source[r - 1] + self.sigma
                curr_from_source[r] = max(diagonal_edge, horizontal_edge, vertical_edge)
            
            tmp = prev_from_source
            prev_from_source = curr_from_source
            curr_from_source = tmp
        
        return prev_from_source

    def to_sink(self, s, t, start_r, start_c, end_r, end_c):

        next_to_sink = [(end_r - r) * self.sigma for r in range(end_r - start_r + 1)]
        curr_to_sink = [self.sigma if r == end_r else 0 for r in range(end_r - start_r + 1)]
        for c in range(end_c - 1, start_c - 1, -1):
            curr_to_sink[end_r - start_r] = next_to_sink[end_r - start_r] + self.sigma
            for r in range(end_r - 1, start_r - 1, -1):
                diagonal_edge = next_to_sink[r - start_r + 1] + (self.match if s[c] == t[r] else self.mu)
                horizontal_edge = next_to_sink[r - start_r] + self.sigma
                vertical_edge = curr_to_sink[r - start_r + 1] + self.sigma
                curr_to_sink[r - start_r] = max(diagonal_edge, horizontal_edge, vertical_edge)
            
            tmp = next_to_sink
            next_to_sink = curr_to_sink
            curr_to_sink = tmp

        return next_to_sink, curr_to_sink

    def find_middle_edge(self, s, t):
        
        middle = (len(s)) // 2
        
        from_source = self.from_source(s, t, 0, 0, len(t), middle)
        to_sink, next_to_sink = self.to_sink(s, t, 0, middle, len(t), len(s))
        
        max_path_r = 0
        self.global_alignment_score = from_source[0] + to_sink[0]
        for r in range(1, len(t) + 1, 1):
            path_r_len = from_source[r] + to_sink[r]
            if self.global_alignment_score < path_r_len:
                max_path_r = r
                self.global_alignment_score = path_r_len
        
        middle_edge = []
        middle_edge.append('(')
        middle_edge.append(str(max_path_r))
        middle_edge.append(',')
        middle_edge.append(' ')
        middle_edge.append(str(middle))
        middle_edge.append(')')
        middle_edge.append(' ')
        middle_edge.append('(')

        if max_path_r == len(t):
            middle_edge.append(str(max_path_r))
            middle_edge.append(',')
            middle_edge.append(' ')
            middle_edge.append(str(middle + 1))

        elif to_sink[max_path_r] == next_to_sink[max_path_r] + self.sigma:
            middle_edge.append(str(max_path_r))
            middle_edge.append(',')
            middle_edge.append(' ')
            middle_edge.append(str(middle + 1))

        elif to_sink[max_path_r] == to_sink[max_path_r + 1] + self.sigma:
            middle_edge.append(str(max_path_r + 1))
            middle_edge.append(',')
            middle_edge.append(' ')
            middle_edge.append(str(middle))

        elif to_sink[max_path_r] == next_to_sink[max_path_r + 1] + (self.match if t[max_path_r] == s[middle] else self.mu):
            middle_edge.append(str(max_path_r + 1))
            middle_edge.append(',')
            middle_edge.append(' ')
            middle_edge.append(str(middle + 1))
        middle_edge.append(')')

        self.middle_edge = ''.join(middle_edge)
    
if __name__ == "__main__":
    m,mu,sigma = map(int,sys.stdin.readline().strip().split())
    s,t = [sys.stdin.readline().strip() for _ in range(2)]

    alignment = Alignment(m, mu, sigma)
    alignment.find_middle_edge(s, t)
    
    print(alignment.middle_edge)

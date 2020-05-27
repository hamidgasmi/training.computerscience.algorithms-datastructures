import sys
from collections import namedtuple

Vertex = namedtuple("Vertex", ["row", "col"])

# Let FromSource(i) denote the length of the longest path from the source ending at (i, middle) and 
# Let ToSink(i) denote the length of the longest path from (i, middle) to the sink. 
# Length(i) = FromSource(i) + ToSink(i)


# 3. Implementation: 
#    Running time:
#    Space Complexity:
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
            for r in range(1, rows_count, 1):
                diagonal_edge = prev_from_source[r - 1] + (self.match if s[r - 1] == t[c - 1] else self.mu)
                horizontal_edge = prev_from_source[r] + self.sigma
                vertical_edge = curr_from_source[r - 1] + self.sigma
                curr_from_source[r] = max(diagonal_edge, horizontal_edge, vertical_edge)
            #print(curr_from_source)
            tmp = prev_from_source
            prev_from_source = curr_from_source
            curr_from_source = tmp
        
        return curr_from_source

    def to_sink(self, s, t, start_r, start_c, end_r, end_c):
        
        rows_count = end_r - start_r + 1
        columns_count = end_c - start_c + 1

        next_to_sink = [r * self.sigma for r in range(rows_count)]
        print(next_to_sink)
        curr_to_sink = [(r - 1) * self.sigma if r == end_r else 0 for r in range(rows_count)]
        for c in range(end_c - 1, start_c - 1, -1):
            for r in range(end_r - 1, start_r - 1, -1):
                print("r, c", r, c, r - start_r + 1)
                diagonal_edge = next_to_sink[r - start_r + 1] + (self.match if s[r] == t[c] else self.mu)
                horizontal_edge = next_to_sink[r - start_r] + self.sigma
                vertical_edge = curr_to_sink[r - start_r + 1] + self.sigma
                curr_to_sink[r - start_r] = max(diagonal_edge, horizontal_edge, vertical_edge)
            print(curr_to_sink)
            tmp = next_to_sink
            next_to_sink = curr_to_sink
            curr_to_sink = tmp

        return curr_to_sink, next_to_sink

    def find_middle_edge(self, s, t):
        
        middle_column_index = len(t) // 2 #+ len(s) % 2
        from_source = self.from_source(s, t, 0, 0, len(s), middle_column_index)
        print("0, middle_column_index, len(s), len(t): ", 0, middle_column_index, len(s), len(t))
        to_sink, next_to_sink = self.to_sink(s, t, 0, middle_column_index, len(s), len(t))

        middle_column = []
        max_path_r = 0
        for r in range(len(s)):
            path_r_len = from_source[r] + to_sink[r]
            middle_column.append(path_r_len)
            if middle_column[max_path_r] < path_r_len:
                max_path_r = len(middle_column) - 1
        
        middle_edge = '(' + str(max_path_r) + ', ' + str(middle_column_index) + ') '
        print("Middle Edge: ", middle_edge, to_sink, next_to_sink)   

        if max_path_r == len(s):
            middle_edge += '(' + str(max_path_r) + ', ' + str(middle_column_index + 1) + ')'

        elif to_sink[max_path_r] == next_to_sink[max_path_r + 1] - (self.match if s[max_path_r] == t[middle_column_index] else self.mu):
            middle_edge += '(' + str(max_path_r + 1) + ', ' + str(middle_column_index + 1) + ')'
        
        elif to_sink[max_path_r] == next_to_sink[max_path_r] - self.sigma:
            middle_edge += '(' + str(max_path_r) + ', ' + str(middle_column_index + 1) + ')'

        elif to_sink[max_path_r] == next_to_sink[max_path_r + 1] - self.sigma:
            middle_edge += '(' + str(max_path_r + 1) + ', ' + str(middle_column_index) + ')'
        
        print("Middle Edge: ", middle_edge)   

if __name__ == "__main__":
    m,mu,sigma = map(int,sys.stdin.readline().strip().split())
    s,t = [sys.stdin.readline().strip() for _ in range(2)]

    alignment = Alignment(m, mu, sigma)
    alignment.find_middle_edge(s, t)
    
    print(alignment.middle_edge)


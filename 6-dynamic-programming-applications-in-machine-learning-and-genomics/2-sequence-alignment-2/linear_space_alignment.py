import sys
from collections import namedtuple

Vertex = namedtuple("Vertex", ["row", "col"])

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
        self.aligned_seq_1 = ""
        self.aligned_seq_2 = ""

    def from_source(self, s, t, v_start, v_end):
        
        rows_count = v_end.row - v_start.row + 1
        columns_count = v_end.col - v_start.col + 1

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

    def to_sink(self, s, t, v_start, v_end):
        
        next_to_sink = [(v_end.row - r) * self.sigma for r in range(v_end.row - v_start.row + 1)]
        curr_to_sink = [self.sigma if r == v_end.row else 0 for r in range(v_end.row - v_start.row + 1)]
        for c in range(v_end.col - 1, v_start.col - 1, -1):
            curr_to_sink[v_end.row - v_start.row] = next_to_sink[v_end.row - v_start.row] + self.sigma
            for r in range(v_end.row - 1, v_start.row - 1, -1):
                diagonal_edge = next_to_sink[r - v_start.row + 1] + (self.match if s[c] == t[r] else self.mu)
                horizontal_edge = next_to_sink[r - v_start.row] + self.sigma
                vertical_edge = curr_to_sink[r - v_start.row + 1] + self.sigma
                curr_to_sink[r - v_start.row] = max(diagonal_edge, horizontal_edge, vertical_edge)
            
            tmp = next_to_sink
            next_to_sink = curr_to_sink
            curr_to_sink = tmp

        return next_to_sink, curr_to_sink

    def find_middle_node(self, s, t, v_start, v_end):
        
        middle_node_c = (v_end.col - v_start.col) // 2
        
        from_source = self.from_source(s, t, Vertex(v_start.row, v_start.col), Vertex(v_end.row, middle_node_c))
        to_sink, next_to_sink = self.to_sink(s, t, Vertex(v_start.row, middle_node_c), Vertex(v_end.row, v_end.col))
         
        middle_node_r = 0
        alignment_score = from_source[0] + to_sink[0]
        for r in range(1, len(t) + 1, 1):
            path_len = from_source[r] + to_sink[r]
            if alignment_score < path_len:
                middle_node_r = r
                alignment_score = path_len

        middle_node = Vertex(middle_node_r, middle_node_c)
        aligned_seq_1 = ''
        aligned_seq_2 = ''

        if middle_node_r == len(t):
            aligned_seq_1 = s[middle_node_c]
            aligned_seq_2 = '-'
        
        elif to_sink[middle_node_r] == next_to_sink[middle_node_r] + self.sigma:
            aligned_seq_1 = '-'
            aligned_seq_2 = t[middle_node_r]
        
        elif to_sink[middle_node_r] == to_sink[middle_node_r + 1] + self.sigma:
            aligned_seq_1 = s[middle_node_c]
            aligned_seq_2 = '-'
        
        elif to_sink[middle_node_r] == next_to_sink[middle_node_r + 1] + (self.match if t[middle_node_r] == s[middle_node_c] else self.mu):
            aligned_seq_1 = s[middle_node_c]
            aligned_seq_2 = t[middle_node_r]

        return alignment_score, middle_node, aligned_seq_1, aligned_seq_2

    def _global_alignment(self, s, t, source_node, sink_node):
        
        aligned_seq_1 = []
        aligned_seq_2 = []
        score_alignment = 0
        if sink_node.row == source_node.row and sink_node.col ==  source_node.col:
            score_alignment = max(self.match if t[sink_node.row] == s[sink_node.col] else self.mu, self.sigma)
            if score_alignment == self.match if t[sink_node.row] == s[sink_node.col] else self.mu:
                aligned_seq_1.append(s[sink_node.col])
                aligned_seq_2.append(s[sink_node.row])
            else:
                aligned_seq_1.append(s[sink_node.col])
                aligned_seq_2.append('-')
            
            return score_alignment, aligned_seq_1, aligned_seq_2

        elif sink_node.row == source_node.row:
            for c in range(sink_node.col, source_node.col, -1):
                aligned_seq_1.append(s[c])
                aligned_seq_2.append('-')
                score_alignment -= self.sigma

            return score_alignment, aligned_seq_1, aligned_seq_2

        elif sink_node.col ==  source_node.col:
            for r in range(sink_node.row, source_node.row, -1):
                aligned_seq_1.append(s[r])
                aligned_seq_2.append('-')
                score_alignment -= self.sigma
            
            return score_alignment, aligned_seq_1, aligned_seq_2

        score_alignment, middle_node, middle_seq1, middle_seq2 = self.find_middle_node(s, t, source_node, sink_node)

        _, aligned_seq1_upper, aligned_seq2_upper = self._global_alignment(s, t, source_node, middle_node)
        _, aligned_seq1_lower, aligned_seq2_lower = self._global_alignment(s, t, middle_node, sink_node)

        aligned_seq_1.extend(aligned_seq1_upper)
        aligned_seq_1.append(middle_seq1)
        aligned_seq_1.extend(aligned_seq1_lower)

        aligned_seq_2.extend(aligned_seq2_upper)
        aligned_seq_2.append(middle_seq2)
        aligned_seq_2.extend(aligned_seq2_lower)

        return score_alignment, aligned_seq_1, aligned_seq_2
        
    def global_alignment(self, s, t):

        self.global_alignment_score = self._global_alignment(s, t, Vertex(0, 0), Vertex(len(t), len(s)))
        
        #if (source_node.row, source_node.col, sink_node.row, sink_node.col) == (0, 0, len(t), len(s)):
        # self.global_alignment_score = score_alignment        

        
                    
if __name__ == "__main__":
    m,mu,sigma = map(int,sys.stdin.readline().strip().split())
    s,t = [sys.stdin.readline().strip() for _ in range(2)]

    alignment = Alignment(m, mu, sigma)
    alignment.global_alignment(s, t)
    
    print(alignment.global_alignment_score)
    print(alignment.aligned_seq_1)
    print(alignment.aligned_seq_2)
    
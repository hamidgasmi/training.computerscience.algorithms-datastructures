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
        curr_from_source = [0 for r in range(rows_count)]
        for c in range(1, columns_count, 1):
            curr_from_source[0] = prev_from_source[0] + self.sigma
            for r in range(1, rows_count, 1):
                diagonal_edge = prev_from_source[r - 1] + (self.match if s[c + v_start.col - 1] == t[r + v_start.row - 1] else self.mu)
                horizontal_edge = prev_from_source[r] + self.sigma
                vertical_edge = curr_from_source[r - 1] + self.sigma
                curr_from_source[r] = max(diagonal_edge, horizontal_edge, vertical_edge)
            tmp = prev_from_source
            prev_from_source = curr_from_source
            curr_from_source = tmp
        
        return prev_from_source

    def to_sink(self, s, t, v_start, v_end):
        
        next_to_sink = [(v_end.row - v_start.row - r) * self.sigma for r in range(v_end.row - v_start.row + 1)]
        curr_to_sink = [0 for r in range(v_end.row - v_start.row + 1)]

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
        
        middle_node_c = v_start.col + (v_end.col - v_start.col) // 2
        
        from_source = self.from_source(s, t, v_start, Vertex(v_end.row, middle_node_c))
        to_sink, next_to_sink = self.to_sink(s, t, Vertex(v_start.row, middle_node_c), v_end)
        
        max_path_row = 0
        rows_count = v_end.row - v_start.row + 1
        alignment_score = from_source[0] + to_sink[0]
        for r in range(1, rows_count, 1):
            path_len = from_source[r] + to_sink[r]
            if alignment_score < path_len:
                max_path_row = r
                alignment_score = path_len
        middle_edge_start_node = Vertex(max_path_row + v_start.row, middle_node_c)
        
        middle_seq_s = []
        middle_seq_t = []
        if middle_edge_start_node.row == v_end.row:
            middle_seq_s.append(s[middle_node_c])
            middle_seq_t.append('-')
            middle_edge_end_node = Vertex(middle_edge_start_node.row, middle_edge_start_node.col + 1)

        elif to_sink[max_path_row] == next_to_sink[max_path_row + 1] + (self.match if t[middle_edge_start_node.row] == s[middle_node_c] else self.mu):
            middle_seq_s.append(s[middle_node_c])
            middle_seq_t.append(t[middle_edge_start_node.row])
            middle_edge_end_node = Vertex(middle_edge_start_node.row + 1, middle_edge_start_node.col + 1)

        elif to_sink[max_path_row] == next_to_sink[max_path_row] + self.sigma:
            middle_seq_s.append(s[middle_node_c])
            middle_seq_t.append('-')
            middle_edge_end_node = Vertex(middle_edge_start_node.row, middle_edge_start_node.col + 1)

        elif to_sink[max_path_row] == to_sink[max_path_row + 1] + self.sigma:
            middle_seq_s.append('-')
            middle_seq_t.append(t[middle_edge_start_node.row])
            middle_edge_end_node = Vertex(middle_edge_start_node.row + 1, middle_edge_start_node.col)

        return alignment_score, middle_edge_start_node, middle_edge_end_node, middle_seq_s, middle_seq_t

    def _global_alignment(self, s, t, source_node, sink_node):
        
        aligned_seq_1 = []
        aligned_seq_2 = []
        score_alignment = 0
        if sink_node.row < source_node.row or sink_node.col <  source_node.col:
            return 0, aligned_seq_1, aligned_seq_2

        elif sink_node == source_node:
            return 0, aligned_seq_1, aligned_seq_2
        
        elif sink_node.row == source_node.row:
            for c in range(source_node.col, sink_node.col, +1):
                aligned_seq_1.append(s[c])
                aligned_seq_2.append('-')
                score_alignment -= self.sigma

            return score_alignment, aligned_seq_1, aligned_seq_2

        elif sink_node.col ==  source_node.col:
            for r in range(source_node.row, sink_node.row, +1):
                aligned_seq_1.append('-')
                aligned_seq_2.append(t[r])
                score_alignment -= self.sigma
            
            return score_alignment, aligned_seq_1, aligned_seq_2

        score_alignment, middle_edge_start_node, middle_edge_end_node, middle_seq_s, middle_seq_t = self.find_middle_node(s, t, source_node, sink_node)

        part_alignment_seq1, part_alignment_seq2 = [], []
        if sink_node != middle_edge_start_node:
            _, part_alignment_seq1, part_alignment_seq2 = self._global_alignment(s, t, source_node, middle_edge_start_node)
        aligned_seq_1.extend(part_alignment_seq1)
        aligned_seq_2.extend(part_alignment_seq2)

        aligned_seq_1.extend(middle_seq_s)
        aligned_seq_2.extend(middle_seq_t)

        part_alignment_seq1, part_alignment_seq2 = [], []
        if middle_edge_end_node != source_node:
            _, part_alignment_seq1, part_alignment_seq2 = self._global_alignment(s, t, middle_edge_end_node, sink_node)
        aligned_seq_1.extend(part_alignment_seq1)
        aligned_seq_2.extend(part_alignment_seq2)

        return score_alignment, aligned_seq_1, aligned_seq_2
        
    def global_alignment(self, s, t):

        self.global_alignment_score, aligned_seq_1, aligned_seq_2 = self._global_alignment(s, t, Vertex(0, 0), Vertex(len(t), len(s)))

        self.aligned_seq_1 = ''.join(aligned_seq_1)
        self.aligned_seq_2 = ''.join(aligned_seq_2)        
                    
if __name__ == "__main__":
    m,mu,sigma = map(int,sys.stdin.readline().strip().split())
    s,t = [sys.stdin.readline().strip() for _ in range(2)]

    alignment = Alignment(m, mu, sigma)
    alignment.global_alignment(s, t)
    
    print(alignment.global_alignment_score)
    print(alignment.aligned_seq_1)
    print(alignment.aligned_seq_2)
    
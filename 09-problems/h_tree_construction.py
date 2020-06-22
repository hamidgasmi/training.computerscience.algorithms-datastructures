import math

# Analysis:
#   H-Tree is a 4-ary tree
#   Each node of the tree is defined by its (x, y, length, depth) and 4 children
#   Its 4 children are defined as follow:
#       Upper right child:  (x + length/2, y + length/2, length/√2, depth + 1))
#       Upper left child:   (x - length/2, y + length/2, length/√2, depth + 1))
#       Buttom right child: (x + length/2, y - length/2, length/√2, depth + 1))
#       Buttom left child:  (x - length/2, y - length/2, length/√2, depth + 1))
# Assumptions:
#   We assume that the drawing order isn't important
# Solution:
#   To draw the tree we just need to do a recursive DFS traversal of the tree
#   We visit a node N (draw it)
#   We call the DFS function for each its chidren
#
#   We start with the root defined by the input (depth > 1)
#   We call the dfs function by decreasing depth by 1 (depth - 1)
#   We stop when we reach depth = 0

class H_Tree:
    
    def _draw_line(self, x1, y1, x2, y2):
        print("(%.1f, %.1f) - (%.1f, %.1f)" % (x1, y1, x2, y2))

    # Time and Space Analysis:
    #   Depth Problem #         Work                Space
    #    1         1             O(1)               O(1)
    #    2       4**1           4**1 O(1)           O(1)
    #   ...      ...
    #    i       4**(i-1)       4**(i-1) O(1)       O(1)
    #   ...
    #  depth=d   4**(d - 1)     4**(d - 1) O(1)     O(1)
    # Time complexity: (1 + 4 + 4**2 + ... + 4**(d-1)) * O(1) = ((4**d - 4) / 3) O(1) = O(4**d)
    # Space complexity: O(d)
    def draw_dfs(self, x, y, length, depth):
        if depth <= 0:
            return

        mid_len = length / 2
        self._draw_line(x - mid_len, y, x + mid_len, y)                     # Horizontal segment
        self._draw_line(x - mid_len, y - mid_len, x - mid_len, y + mid_len) # Left vertical segment
        self._draw_line(x + mid_len, y - mid_len, x + mid_len, y + mid_len) # Right vertical segment

        # draw the node's children:
        children_len = length / math.sqrt(2)

        # Upper Right
        self.draw_dfs(x + mid_len, y + mid_len, children_len, depth - 1)

        # Upper Left
        self.draw_dfs(x - mid_len, y + mid_len, children_len, depth - 1)
        
        # Buttom right
        self.draw_dfs(x - mid_len, y + mid_len, children_len, depth - 1)

        # Buttom left
        self.draw_dfs(x - mid_len, y - mid_len, children_len, depth - 1)
 
if __name__ == '__main__':

    h_tree = H_Tree()
    
    h_tree.draw_dfs(0, 0, math.sqrt(2), 2)
    #h_tree.draw_dfs(0, 0, 2, 3)
    #h_tree.draw_dfs(0, 0, 2, 4)
    #h_tree.draw_dfs(0, 0, 2, 5)
    #h_tree.draw_dfs(0, 0, 2, 6)

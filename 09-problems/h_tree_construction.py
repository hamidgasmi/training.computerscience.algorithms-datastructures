import math

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
    def draw(self, x, y, length, depth):
        if depth <= 0:
            return

        self._draw_line(x - length / 2, y, x + length / 2, y)
        self._draw_line(x - length/2, y - length/2, x - length/2, y + length/2)
        self._draw_line(x + length/2, y - length/2, x + length/2, y + length/2)

        # Top Left
        self.draw(x - length/2, y + length/2, length / math.sqrt(2), depth - 1)
        
        # Top Right
        self.draw(x + length/2, y + length/2, length / math.sqrt(2), depth - 1)
        
        # Buttom left
        self.draw(x - length/2, y - length/2, length / math.sqrt(2), depth - 1)
        
        # Buttom right
        self.draw(x - length/2, y + length/2, length / math.sqrt(2), depth - 1)
 
if __name__ == '__main__':

    h_tree = H_Tree()
    
    #h_tree.draw(0, 0, math.sqrt(2), 2)
    #h_tree.draw(0, 0, 2, 3)
    #h_tree.draw(0, 0, 2, 4)
    #h_tree.draw(0, 0, 2, 5)
    #h_tree.draw(0, 0, 2, 6)

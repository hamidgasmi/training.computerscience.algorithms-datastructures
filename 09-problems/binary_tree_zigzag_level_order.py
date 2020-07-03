# Definition for a binary tree node.
class Tree_Node:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:

    # Time Complexity: O(|V|)
    # Space Complexity: O(|V|)
    def zigzag_Level_order(self, root: Tree_Node) -> List[List[int]]:
        
        zigzag_order = []
        
        if root is None:
            return zigzag_order        
        
        curr_level = [root]
        d = 0
        while curr_level:
            
            next_level = []
            zigzag_order.append([])
            
            for i in range(len(curr_level) - 1, -1, -1):
                
                zigzag_order[d].append(curr_level[i].val)
                
                if d % 2 == 0:
                    if curr_level[i].left is not None:
                        next_level.append(curr_level[i].left)
                        
                    if curr_level[i].right is not None:
                        next_level.append(curr_level[i].right)
                
                else:
                    if curr_level[i].right is not None:
                        next_level.append(curr_level[i].right)
                        
                    if curr_level[i].left is not None:
                        next_level.append(curr_level[i].left)
            
            curr_level = next_level
            d += 1
        
        return zigzag_order
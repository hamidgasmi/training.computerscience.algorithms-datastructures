# Definition for a binary tree node.
class Tree_Node:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    
    # Time Complexity: O(|V|)
    # Space Complexity: O(|V|)
    def verticalOrder(self, root: Tree_Node) -> List[List[int]]:
        
        if root is None:
            return []
        
        return self._bfs(root)
    
    def _bfs(self, root: Tree_Node):
        
        # Tuple(node, column)
        curr_level = [(root, 0)]
        
        left = []
        right = []
        
        while curr_level:
            
            next_level = []
            
            for (node, col) in curr_level:
                
                if col >= 0:
                    if len(right) <= col:
                        right.append([])
                        
                    right[col].append(node.val)
            
                else:
                    if len(left) <= abs(col) - 1:
                        left.append([])
                    
                    left[abs(col) - 1].append(node.val)
                                
                if node.left is not None:
                    next_level.append((node.left, col - 1))
                    
                if node.right is not None:
                    next_level.append((node.right, col + 1))
                
            curr_level = next_level
        
        return left[::-1] + right
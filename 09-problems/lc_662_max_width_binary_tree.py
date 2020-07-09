# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution_1:
    
    # Time complexity: O(2**depth)
    # Space Complexity: O(2**depth-1)
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        
        if root is None:
            return 0
        
        curr_level_nodes = [root]
        
        max_width = 0
        
        while curr_level_nodes:
            
            max_width = max(max_width, len(curr_level_nodes))
            
            next_level_nodes = []
            
            right_none_nodes = []
            for node in curr_level_nodes:
                
                if len(next_level_nodes) == 0 and (node is None or (node.left is None and node.right is None)):
                    continue
                
                if node is None:
                    right_none_nodes.append(node)
                    right_none_nodes.append(node)
                    continue
                
                if node.left is None and len(next_level_nodes) != 0:
                    right_none_nodes.append(node.left)
                    
                elif node.left is not None:
                    next_level_nodes.extend(right_none_nodes)
                    right_none_nodes = []
                    next_level_nodes.append(node.left)
                    
                if node.right is None:
                    right_none_nodes.append(node.right)
                    
                else:
                    next_level_nodes.extend(right_none_nodes)
                    right_none_nodes = []
                    next_level_nodes.append(node.right)
                        
            curr_level_nodes = next_level_nodes
                
        return max_width
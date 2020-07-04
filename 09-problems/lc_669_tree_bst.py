class Tree_Node:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    
    # Time Complexity: O(N)
    # Space Complexity: O(1)
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        
        # 1. Find a common parent
        node = root
        while node is not None:
            if node.val > R:
                node = node.left
                
            elif node.val < L:
                node = node.right
            
            else:
                break
        root = node
        
        # 2. Trim the left subtree
        parent = root
        node = root.left
        while (node is not None):      
            if node.val < L:
                parent.left = node.right
                node = node.right
                
            else:
                parent = node
                node = node.left
        parent.left = None
        
        # 3. Trim the right subtree:
        parent = root
        node = root.right
        while (node is not None):
            if node.val > R:
                parent.right = node.left
                node = node.left
            
            else:
                parent = node
                node = node.right
        parent.right = None
        
        return root
    
    def trimBST_recursive(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if not root:
            return None
        
        elif root.val > R:
            return self.trimBST(root.left, L, R)
        
        elif root.val < L:
            return self.trimBST(root.right, L, R)
        
        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)
            
        return root

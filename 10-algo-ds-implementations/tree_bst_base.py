import tree_binary_tree_node

class BinarySearchTree:
    """
    
    """
    def __init__(self):
        pass

    # Time Analysis: O(|V|) 
    # Space Analysis: O(|V|)
    # Worst case: the binary tree is a linked list
    def find(self, val, root: BinaryTreeNode = None) -> BinaryTreeNode:
        if root is None:
            return None

        if val == root.val:
            return root
        
        elif val < root.val:
            return root if root.left is None else self.find(val, root.left)
        
        else: # val > root.val
            return root if root.right is None else self.find(val, root.right)
        
    
    def next(self, node: BinaryTreeNode) -> BinaryTreeNode:
        pass

    def left_descendant(self, node: BinaryTreeNode) -> BinaryTreeNode:
        pass

    def right_ancestor(self, node: BinaryTreeNode) -> BinaryTreeNode:
        pass
    
    def find_range(self, val_from, val_to, node: BinaryTreeNode = None) -> list[BinaryTreeNode]:
        pass

    def insert(self, val, node: BinaryTreeNode = None) -> BinaryTreeNode:
        pass

    def delete(self, node: BinaryTreeNode):
        pass

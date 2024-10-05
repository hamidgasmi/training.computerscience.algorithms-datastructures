
class BinaryTreeNode:
    def __init__(self, val, left=None, right=None):

        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        
        return (f"val: {self.val}, left: {None if self.left is None else self.left.val}"
                            + f", right : {None if self.right is None else self.right.val}")

class BinaryTreeNodeParent(BinaryTreeNode):
    def __init__(self, val, parent:BinaryTreeNodeParent=None, left:BinaryTreeNodeParent=None, rigth:BinaryTreeNodeParent=None):
        
        super().__init__(val, left, rigth)
        self.parent = parent
    
    def __repr__(self):

        return ( super().__repr() + f", parent : {None if self.parent is None else self.parent.val}")
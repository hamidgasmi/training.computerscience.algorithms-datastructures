
class BinaryTreeNode:
    def __init__(self, val, left=None, right=None):

        self.val = val
        self.left = left
        self.right = right

class BinaryTreeNodeParent(BinaryTreeNode):
    def __init__(self, val, parent:BinaryTreeNodeParent=None, left:BinaryTreeNodeParent=None, rigth:BinaryTreeNodeParent=None):
        
        super().__init__(val, left, rigth)
        self.parent = parent
        
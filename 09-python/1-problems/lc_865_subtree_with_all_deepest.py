class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
    1. Problem Summary / Clarifications / TDD:
        Case 1: Return 2
            1
           / \
          2   3
         / \   \        
        4   5   6
       / \   \
      7  8    9

        Case 2: Return 10
            1
           / \
          2   3
         / \   \        
        4   5   6
       / \   \
      7  8    9
        /
       10

    2. Inuition
        - DFS traversal: for each branch, return its height and its subtree with all deepest nodes
        - If left height == right hight, return root
        - If left height > right height, return left substree
        - If left height < right height, return right substree
    
    3. Implementation:
    4. Tests:
            - All cases above
            - Edge cases: empty tree, a tree with one node
            - Special cases: Tree as a linked list, balanced tree
                1               1
                 \             /
                  2           2
                   \         /
                    3       3

    4. Complexity Analysis:
        Time Complexity: O(N): we need to visit all nodes
        Space Complexity: 
            - Worst case: O(N): when the tree looks like a linked-list.
            - Best case: O(height): when the tree is balanced.

"""

class SolutionDFS:
    
    def subtree_with_all_deepest(self, root: TreeNode) -> TreeNode:
        
        return self.dfs(root)[1]        
        
    def dfs(self, root: TreeNode) -> (int, TreeNode):
        if root is None:
            return 0, None
        
        l_height, l_subtree = self.dfs(root.left)
        r_height, r_subtree = self.dfs(root.right)
            
        return max(l_height, r_height) + 1, l_subtree if l_height > r_height else r_subtree if l_height < r_height else root

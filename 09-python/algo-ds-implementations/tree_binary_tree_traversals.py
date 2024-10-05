import tree_binary_tree_node

class BinaryTree:
    """
    
    """
    def __init__(self):
        pass
    
    def visit(self, node: Binary_Tree_Node):
        print(node.val)

    # Analysis: Use 2 lists as a queue:
    #   1st. list will contain all nodes of a current level
    #   2nd. list will contain all children of the current level nodes
    #   When the 1st. list is empty, we assign the 2nd list to the 1st. list and loop
    # Time Complexity: O(|V|)
    # Space Complexity: O(|V| / 2) = O(|V|)
    def bfs(self, root: Binary_Tree_Node):
        if root is None:
            return

        curr_level = [root]
        while curr_level:

            next_level = []
            for node in curr_level:

                self.visit(node)

                if node.left is not None:
                    next_level.append(node.left)

                if node.left is not None:
                    next_level.append(node.right)
            
            curr_level = next_level

    def dfs(self, node: Binary_Tree_Node):
        if node is None:
            return

        
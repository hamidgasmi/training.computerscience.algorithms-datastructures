# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution_2:
    """
    This solution uses a BFS traversal
    The BFS queue is a queue of tuples of (nodes, none nodes count at the end of the node)
    On each tree level, it computes the next level width:

    """
    
    # Time Complexity: O(|V|)
    # Space Complexity: O(|V|)
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        
        if root is None:
            return 0
        
        max_width = 0
        curr_level_width = 1
        
        curr_level_nodes = [(root, 0)]
        
        while curr_level_nodes:
            
            max_width = max(max_width, curr_level_width)
            
            next_level_width = 0
            next_level_none_nodes_count = 0
            
            next_level_nodes = []            
            for (node, left_none_node_count) in curr_level_nodes:
                
                if len(next_level_nodes) == 0 and (node is None or (node.left is None and node.right is None)):
                    continue
                
                if len(next_level_nodes) != 0:
                    next_level_none_nodes_count += 2 * left_none_node_count
                
                if node is None:
                    next_level_none_nodes_count += 2
                    continue
                
                if node.left is None and len(next_level_nodes) != 0:
                    next_level_none_nodes_count += 1
                    
                elif node.left is not None:
                    next_level_nodes.append((node.left, next_level_none_nodes_count))
                    next_level_width += next_level_none_nodes_count + 1
                    none_nodes_count = 0
                    
                if node.right is None and len(next_level_nodes) != 0:
                    next_level_none_nodes_count += 1
                    
                else:
                    next_level_nodes.append((node.right, next_level_none_nodes_count))
                    next_level_width += next_level_none_nodes_count + 1
                    next_level_none_nodes_count = 0
            
            curr_level_nodes = next_level_nodes
            curr_level_width = next_level_width
            
        return max_width

class Solution_1:
    """
    This solution uses a BFS traversal
    On each tree level, 
        - It enqueues all nodes of the next level even those that are None
        - The width of the level is the length of its corresponding queue
    - The max_width is updated at the end of a level traversal

    - This solution isn't efficient because its time complexity and space complexity are those of full binary tree BFS traversal

    """
    
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
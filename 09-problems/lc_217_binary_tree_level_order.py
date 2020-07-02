# Definition for a binary tree node.
class Tree_Node:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

from queue import Queue

class Solution:
    
    # Time Complexity: O(|V|) (number of nodes)
    # Space Complexity: 
    #   By including the output: O(|V| / 2) = O(|V|) (last level nodes = |V| // 2 + 1)
    def level_order_bottom_1(self, root: Tree_Node) -> List[List[int]]:

        level_order_top = []
        
        if root is None:
            return level_order_top

        curr_level = [root]

        while curr_level:

            level_order_top.append([node.val for node in curr_level])
            
            next_level = []
            for node in curr_level:
                if node.left is not None:
                    next_level.append(node.left)

                if node.right is not None:
                    next_level.append(node.right)

            curr_level = next_level

        return level_order_top[::-1]
    
    def level_order_bottom_2(self, root: Tree_Node) -> List[List[int]]:
        
        level_order_top = []
        
        if root is None:
            return level_order_top
        
        nodes_q = Queue()
        depth_q = Queue()
        
        nodes_q.put(root)
        depth_q.put(0)
        
        while not nodes_q.empty():
            
            node = nodes_q.get()
            depth = depth_q.get()
            
            if len(level_order_top) <= depth:
                level_order_top.append([])
                
            level_order_top[depth].append(node.val)
            
            if node.left is not None:
                nodes_q.put(node.left)
                depth_q.put(depth + 1)
                
            if node.right is not None:
                nodes_q.put(node.right)
                depth_q.put(depth + 1)                
        
        return level_order_top[::-1]

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class CodecSolution3:
    """
    2. Intuition:
        - Serialize Recursively with a DFS preorder traversal
        
            1
           / \
          2   3     --------------> 1,2,$,$,3,4,6,$,$,7,$,$,5,$,$
             / \     Serialization
            4   5
           / \
          6   7

    3. Complexity Analysis:
        - Let's n be the number of nodes
        - Time complexity: O(n + n) = O(n)
        - Space complexity: O(n + n) = O(n)
    
    """

    def __init__(self):
        self.separator = ','
        self.serialized_none = '$'

    def serialize(self, root):
        
        serialized_tree = []
        self.serialize_dfs_preorder(root, serialized_tree)
        
        return self.separator.join(serialized_tree)
    
    def serialize_dfs_preorder(self, root, serialized_tree):
        if not root:
            return
        
        serialized_tree.append(str(root.val))
        
        if root.left:
            self.serialize_dfs_preorder(root.left, serialized_tree)
        
        else:
            serialized_tree.append(self.serialized_none)
            
        if root.right:
            self.serialize_dfs_preorder(root.right, serialized_tree)
        
        else:
            serialized_tree.append(self.serialized_none)
    
    def deserialize(self, data):
        if not data:
            return None
        
        values = data.split(self.separator)
        
        return self.deserialize_dfs_preorder(values, 0)[0]
    
    def deserialize_dfs_preorder(self, values:[str], idx: int):
        if idx >= len(values):
            return None, idx
        
        elif values[idx] == self.serialized_none:
            return None, idx + 1
        
        root = TreeNode(int(values[idx]))
        root.left, idx = self.deserialize_dfs_preorder(values, idx + 1)
        root.right, idx = self.deserialize_dfs_preorder(values, idx)
        
        return root, idx

class CodecSolution2:
    """
    2. Intuition:
        - Serialize level by level with a BFS traversal
        - Serialize None nodes only when necessary: they're between two not null nodes
        - Compress None nodes serialization: if there're 5 consecutive None node: compress them to: $5
            1
           / \
          2   3     --------------> 1,2,3,$2,4,5,6,7
             / \     Serialization
            4   5
           / \
          6   7

    3. Complexity Analysis:
        - Let's n be the number of nodes
        - Time complexity: O(n)
        - Space complexity: O(n)
    """

    def __init__(self):
        
        self.separator = ','
        self.serialized_none = '$'

    def serialize(self, root):
        
        serialization = []
        
        curr_level = [root] if root else []
        next_serialization = [str(root.val)] if root else []
        none_count = 0
        while curr_level:
            
            next_level = []
            serialization.extend(next_serialization)
            next_serialization = []
            for node in curr_level:
                if node.left:
                    if none_count:
                        next_serialization.append(self.serialized_none + str(none_count))
                        none_count = 0
                    
                    next_level.append(node.left)
                    next_serialization.append(str(node.left.val))
                else:
                    none_count += 1
                    
                if node.right:
                    if none_count:
                        next_serialization.append(self.serialized_none + str(none_count))
                        none_count = 0
                    
                    next_level.append(node.right)
                    next_serialization.append(str(node.right.val))
                  
                else:
                    none_count += 1
            
            curr_level = next_level
        
        return self.separator.join(serialization)
    
    def deserialize(self, data):
        if not data:
            return None
        
        values = data.split(self.separator)
                
        parent = 0
        child_no = 0
        nodes = [TreeNode(values[0])]
        for i in range(1, len(values)):
            
            if values[i][0] == self.serialized_none:
                none_count = int(values[i][1:])
                
                for _ in range(none_count):
                    (parent, child_no) = self.connect_to_parent(nodes, parent, child_no, None)
                
            else:
                nodes.append(TreeNode(int(values[i])))
                (parent, child_no) = self.connect_to_parent(nodes, parent, child_no, nodes[-1])               
        
        return nodes[0]
    
    def connect_to_parent(self, nodes, parent_idx, child_no, node):
        
        if child_no:
            nodes[parent_idx].right = node
                        
            return parent_idx + 1, 0
                
        else:
            nodes[parent_idx].left = node
            return parent_idx, 1

class CodecSolution1:
    """
    2. Inuition:
        - To consider the tree as a complete binary tree
        Serialization:
        - Generate an array with the tree values as a heap:
            - left child (i) = 2 * i + 1
            - right child(i) = 2 * i + 2
        - join all values with ',' as a separator

        Deserialization:
        - Split the serialized heap
        - Creates nodes for each value in the heap
        - for each node (i):
            - parent idx = (i - 1) // 2
            - Attach node of parent.left or parent.right
            1
           / \
          2   3     --------------> 1,2,3,$,$,4,5,$,$,$,$,6,7
             / \     Serialization
            4   5
           / \
          6   7
        
    3. Complexity Analysis:
        - Let's n be the number of nodes
        - Time complexity: O(2^n) in the worst case: the tree is a linked-list
        - Space complexity: O(2^n)
        - It's not efficient!

    """
    def __init__(self):
        self.serialized_none = '$'
        self.separator = ','
    
    def serialize(self, root):
        
        serialization = []
        self.serialize_heap(root, serialization, 0)
        
        return self.separator.join(serialization)
    
    def serialize_heap(self, root, serialization, node_no):
        if not root:
            return
        
        nodes_count = len(serialization)
        for i in range(nodes_count, node_no + 1):
            serialization.append(self.serialized_none)
        serialization[node_no] = str(root.val)
        
        if root.left:
            self.serialize_heap(root.left, serialization, 2 * node_no + 1)
        
        if root.right:
            self.serialize_heap(root.right, serialization, 2 * node_no + 2)
            
    def deserialize(self, data):
        if not data:
            return None
        
        values_heap = data.split(self.separator)

        nodes_heap = [None if val == self.serialized_none else TreeNode(int(val)) for val in values_heap]
        for i in range(1, len(values_heap)):
            parent_idx = (i - 1) // 2
            
            if parent_idx * 2 + 1 == i:
                if nodes_heap[parent_idx]:
                    nodes_heap[parent_idx].left = nodes_heap[i]
                
            else:
                if nodes_heap[parent_idx]:
                    nodes[parent_idx].right = nodes_heap[i]
        
        return nodes_heap[0]
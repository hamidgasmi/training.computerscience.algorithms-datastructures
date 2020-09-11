# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class SolutionBFS:
    """ 
    2. Intuition: cloning with a BFS traversal
        1 --- 2
        |     | 
        4 --- 3
        1. clone(1)
            1.2. clone(2), add it as a neighbor and add it in the BFS queue
            1.3. clone(4), add it as a neighbor and add it in the BFS queue
        2. clone(2):
            2.2. add clone(1) as a neighbor
            2.3. clone(3), add it as a neighbor and add it in the BFS queue
        3. clone(4):
            3.2. add clone(1) as a neighbor
            3.3. add clone(3) as a neighbor
        4. clone(3):
            3.2. add clone(2) as a neighbor
            3.3. add clone(4) as a neighbor

    3. Complexity Analysis
        Let |V|, |E| the number of vertices and edges respectively
        Time Complexity: O(|V| + |E|)
        Space Complexity: O(|E|)

    """
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node:
            return None        
        
        output_node = Node(node.val)
        cloned_nodes = {node.val: output_node}
        
        curr_level = [node]        
        while curr_level:
            
            next_level = []
            for node in curr_level:
                
                clone = cloned_nodes[node.val]

                for neighbor in node.neighbors:

                    if neighbor.val in cloned_nodes:
                        clone.neighbors.append(cloned_nodes[neighbor.val])

                    else:
                        clone.neighbors.append(Node(neighbor.val))
                        cloned_nodes[neighbor.val] = clone.neighbors[-1]
                        next_level.append(neighbor)
            
            curr_level = next_level
            
        return output_node

class SolutionDFSIterative:
    """ 
    2. Intuition: cloning with an iterative DFS preorder traversal 
        1 --- 2
        |     | 
        4 --- 3
        0. push(1) to a stack
        1. pop(1):
            1.1. clone(1)
            1.2. clone(2), add it as a neighbor and push it to the stack
            1.3. clone(4), add it as a neighbor and push it to the stack
        2. pop(4):
            2.1. clone(4)
            2.2. add clone(1) as a neighbor
            2.3. clone(3), add it as a neighbor and push it to the stack
        3. pop(3):
            3.1. clone(3)
            3.2. add clone(2) as a neighbor
            3.3. add clone(4) as a neighbor
        4. pop(2)
            4.1. clone(2):
            2.2. add clone(1) as a neighbor
            2.3. add clone(4) as a neighbor            

    3. Complexity Analysis
        Let |V|, |E| the number of vertices and edges respectively
        Time Complexity: O(|V| + |E|)
        Space Complexity: O(|E|)

    """
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node:
            return None
                
        cloned_nodes = {node.val: Node(node.val)}
        output = cloned_nodes[node.val]
        
        stack = [node] if node else []
        while stack:
            
            node = stack.pop()
            clone = cloned_nodes[node.val]
            
            for neighbor in node.neighbors:
                
                if neighbor.val in cloned_nodes:
                    clone.neighbors.append(cloned_nodes[neighbor.val])
                    
                else:
                    clone.neighbors.append(Node(neighbor.val))
                    stack.append(neighbor)
                    cloned_nodes[neighbor.val] = clone.neighbors[-1]
                
        return output

class SolutionDFSRecursive:
    """ 
    2. Intuition: cloning with an iterative DFS preorder traversal 
        1 --- 2
        |     | 
        4 --- 3           

    3. Complexity Analysis
        Let |V|, |E| the number of vertices and edges respectively
        Time Complexity: O(|V| + |E|)
        Space Complexity: O(|E|)

    """
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        return self.clone_graph_dfs(node, {})
            
    def clone_graph_dfs(self, node: 'Node', cloned_nodes: dict) -> 'Node':
        if not node:
            return None
        
        elif node.val in cloned_nodes:
            return cloned_nodes[node.val]
        
        clone = Node(node.val)
        cloned_nodes[node.val] = clone
        for adjacent in node.neighbors:
            clone.neighbors.append(self.clone_graph_dfs(adjacent, cloned_nodes))
            
        return clone
        
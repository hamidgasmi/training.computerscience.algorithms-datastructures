#!/usr/bin/env python3.7
import list_node
import list_singly_linked_list
import utility_devel

# Analysis:
#   To detect a cycle in a linked list, we just need to loop on the list nodes with 2 pointers: slow and fast pointers:
#   If there is a cycle, then slow and fast pointers will meet at some position in the cycle
#   If there is no cycle, then faster point will reach the tail node
#
#   There're 2 main scenarios regarding cycles:
#   1. A cycle could include all the list nodes. In this case, the 1st. cycle node is the list head
#   2. A cycle could include only some of the list nodes. In this case, the 1st. nodes of the list aren't in the cyle
#      This means that the predecessor of the 1st. cycle node isn't part of the cycle.
#
#   Solution is:
#   1st. We'll use slow and fast pointers to detect if there is a cycle or not. We'll store predecessors of each node.
#   2nd. We'll find all nodes in the cycle
#   3rd. For each node in the cycle, 
#       if its predecessor isn't in the cycle, then return node
#       if all predecessors are also in the cycle, then return the lsit head

class Linked_List_Cycle:
    
     # Running Time: O(|List|)
     # Space Complexity: O(|List|)
     def detect_cycle(self, head: list_node.Singly_Linked_List_head_tail) -> list_node.Singly_Linked_List_head_tail:
         
        (node_in_cycle, predecessors) = self.has_cycle(head)
        
        if node_in_cycle is None:
            return None
        
        else:
            return self._cycle_start_node(head, node_in_cycle, predecessors)

     # Running Time: O(|List|)
     # Space Complexity: O(|List|)
     def has_cycle(self, head: list_node.Singly_Linked_Node) -> (list_node.Singly_Linked_Node, dict):
        
        if head is None:
            return (None, None)
        
        predecessors = dict()
        
        fast_node = head.next
        slow_node = head
        node = head
        predecessors[fast_node] = node
        while not (fast_node is None or fast_node.next is None):
                        
            if slow_node == fast_node:
                return (slow_node, predecessors)
            
            # Increment fast node            
            node = fast_node.next
            if not node in predecessors:
                predecessors[node] = fast_node
            
            fast_node = node.next
            if not fast_node in predecessors:
                predecessors[fast_node] = node
            
            # Increment slow node
            slow_node = slow_node.next
        
        return (None, None)
     
     # Running Time: O(|cycle|)
     # Space Complexity: O(|cycle|)
     def _cycle_start_node(self, head: list_node.Singly_Linked_Node, node_in_cycle: list_node.Singly_Linked_Node, predecessors: dict) -> list_node.Singly_Linked_Node:
        
        # Find all nodes of the cycle
        cycle_nodes = set()
        node = node_in_cycle
        while not node in cycle_nodes:
            cycle_nodes.add(node)
            
            node = node.next
        
        # Find the 1st. node of the cycle: there're 2 cases:
        # 1. All nodes of the list are in the cycle, then the 1st node of the cycle is the list's head
        # 2. Otherwise, it's the node in the cycle which predecessor isn't in the cycle
        for node in node_in_cycle:

            if not predecessors[node] in cycle_nodes:
                return node
        
        return head

if __name__ == '__main__':

    # Get the arguments
    unit_test = utility_devel.Unit_Tests_Utility()
    unit_test.get_inputs()

    pos = unit_test.inputs[0][0]
    list_values = unit_test.inputs[1]

    # Create the singly linked list
    singly_linked_list = list_singly_linked_list.Singly_Linked_List_head_tail(list_values)
    # Create the cycle if necessary
    if pos >= 0:
        singly_linked_list.tail. next = singly_linked_list.get_node_at_pos(pos)

    # Find the cycle first node
    solution = Linked_List_Cycle()
    cycle_start_node = solution.detect_cycle(singly_linked_list.head)
    
    if cycle_start_node is None:
        print('No cycle')

    else:
        print('tail connects to node index: %.1f' % singly_linked_list.get_node_position(cycle_start_node))

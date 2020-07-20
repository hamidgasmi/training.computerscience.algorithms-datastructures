"""
    1. Problem Summary / Clarifications / TDD:
        
        E.g.1. 
            Input: 1->2->6->3->4->5->6, val = 6
            Output: 1->2->3->4->5

        E.g.2. 
            Input: 6->6->6->1->2->6->3->4->5->6, val = 6
            Output: 
        
        E.g.3. 
            Input: 1->2->3->4->5, val = 6
            Output: 1->2->3->4->5
        
        E.g.4. 
            Input: 1->1->1->1->1, val = 1
            Output: None
        
        E.g.5. 
            Input: 1->1->2->1->1, val = 1
            Output: 2
        
    2. Intuition:
       Case 1: The node to delete is in the middle of the linked-list:
        E.g. 1->2->6->3->4->5->6, val = 6
       
       Case 2: The node to delete is the middle head of the linked-list:
       E.g. 6->6->6->1->2->6->3->4->5->6, val = 6

       Create a pseudo head to make all cases the same and return pseudo head next node
       E.g.2. 6->6->6->1->2->6->3->4->5->6, val = 6
        1. Insert pseudo head: 0->6->6->6->1->2->6->3->4->5->6
        2. Delete node with value 6 in the middile of the linked-list: 0->1->2->3->4->5
        3. Return pseudo head next node: 1

    3. Implementation
    4. Tests: Use the examples of step 1 (TDD).
    5. Analysis:
       Time Complexity: O(|ListNode|)
       Space Compexity: O(1)

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    
    def remove_elements(self, head: ListNode, val: int) -> ListNode:
        
        # 1. Insert pseudo head: 0
        head = ListNode(0, head)
            
        # 2. Remove all val items in the middle of the the list
        node, prev_node = head, head
        while node is not None:
            
            if node.val == val:
                prev_node.next = node.next 
                
            else:
                prev_node = node
            
            node = node.next

        # 3. Return pseudo head next node
        return head.next

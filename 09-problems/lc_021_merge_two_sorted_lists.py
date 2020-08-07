"""
    1. Problem Summary / Clarifications / TDD:
        1.  Output(1->2->4, 1->3->4): 1->1->2->3->4->4
        2.  Output(1->2->3, 4->5->6): 1->2->3->4->5->6
        3.  Output(4->5->6, 1->2->3): 1->2->3->4->5->6
        4.  Output(1->3->5, 2->4->6->8->10): 1->2->3->4->5->6->8->10
        6.  Output(1->3->5, 2->4->6->8->10): 1->2->3->4->5->6->8->10
        
        Edges Cases:
        1.  Output(None, None): None
        2.  Output(1->2->3, None): 1->2->3
        3.  Output(None, 1->2->3): 1->2->3
            
    2. Intuition:
        - How to find the head of the merge list?
        - To use a sentinel node
    
    3. Implementation
        ...
    4. Tests:
        ...

    5. Complexity Analysis:
       Time Complexity: O(|l1| + |l2|)
       Space Compexity: O(1)

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        prehead = ListNode(-1)    
        node = prehead
        while l1 and l2:
            
            if l1.val <= l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next            
        
        node.next = l1 if l1 else l2
                    
        return prehead.next
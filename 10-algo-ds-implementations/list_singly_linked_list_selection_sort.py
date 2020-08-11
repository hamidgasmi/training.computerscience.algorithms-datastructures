"""
    1. Problem Summary / Clarifications / TDD:
        4->2->1->3
        
    2. Complexity Analysis:
        Time Complexity: O(n^2)
        Space Complexity: O(1)
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def insertion_sort(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        head.next, unsorted_list = None, head.next
        while unsorted_list:
            node, unsorted_list = unsorted_list, unsorted_list.next
            node.next = None
            
            head = self._insert_in_sorted_list(head, node)            
        
        return head
    
    def _insert_in_sorted_list(self, sorted_head: ListNode, node: ListNode) -> ListNode:
        assert(node is not None)

        prehead = ListNode(0, sorted_head)
        
        sorted_head = prehead
        while sorted_head and sorted_head.next and sorted_head.next.val < node.val:
            sorted_head = sorted_head.next
        
        node.next = sorted_head.next
        sorted_head.next = node        
        
        return prehead.next
    
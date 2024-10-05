"""
    1. Problem Summary / Clarifications / TDD:
        0→1→2→3 =>0→3→1→2
        0→1→2→3→4 => 0→4→1→3→2
        
    2. Intuition:
    
        1. Middle of the list:
            0→1  2→3
            0→1  2→3→4
            
        2. Reverse the 2nd half:
            0→1  3→2
            0→1  4→3→2
            
        3. Merge the two lists:
            0→3→1→2
            0→4→1→3→2
            
    3. Implementation:
    4. Complexity Analysis:
        Time Complexity: O(n), n is the list size
        Space Complexity: O(1)        
        
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return
        
        # 1. Middle of the list:
        node_1 = node_2 = head
        while node_1 and node_1.next:
            node_1 = node_1.next.next
            node_2 = node_2.next
        
        # 2. Reverse the 2nd half of the list
        prev = None
        while node_2:
            node_2.next, prev, node_2  = prev, node_2, node_2.next
        node_2 = prev
        
        # 3. Merge 2 lists
        node_1 = head
        while node_2.next:
            node_1.next, node_1 = node_2, node_1.next
            node_2.next, node_2 = node_1, node_2.next
        
        return head
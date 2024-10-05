"""
    1. Problem Summary / Clarifications / TDD:
        [2,1]
        [5,4,2,1,3]
        [5,4,3,2,1]
        [5,1,4,2,3,4,2,5,1,3]
        [1,1,1,0,0,0]
        [1,1,1]
        [1,0,1,0,1,0]

    2. Intuition:
        1. Divide into 2 unsorted lists by using Fast-Slow-Pointers technique
        2. Sort the 2 lists by recursion
        3. Merge the 2 sorted lists
        
    3. Complexity Analaysis:
        Split a list l into 2 lists:
            Time Complexity:  O(|l|/2)
            Space Complexity: O(1)

        Merge two sorted lists:
            Time Complexity:  O(min(|l1| + |l2|)) = O(|l|/2) since |l1| ~ |l2| ~ |l|/2
            Space Complexity: O(1)

        Let's n = |l|
        Split + Merge:
            Time Complexity:  O(|l|/2) + O(|l|/2) = O(|l|) = O(n)
            Space Complexity: O(1)

        Merge Sort:
        Recursion level         | Nbr of problem #   | Level time complexity | Level Space Complexity
            0   l               | 1 of size n        |  1 * O(n)              |     O(1)
            1   l1, l2          | 2 of size n/2      |  2 * O(n/2)            |     O(1)
            3   l11,l12,l21,l22 | 4 of size n/4      |  4 * O(n/4)            |     O(1)
            ...                   ...                   ...                         ...
            i   l11...li-1i-1   | 2^i-1 of size n/i-1|  2i-1 * O(n/2^i-1)     |     O(1)
            ...
            logn+1              | 2^logn=n of size 1 |  n * O(1)              |     O(1)
            Total Time Complexity = n + 2 * n/2 + ... + 2^logn * n/2^logn = n + ... + n (logn+2 time)
                            = O(nlogn)
            Total Space Complexity = 1 + ... + 1 (logn+2 time) = O(logn)
        
        - Time Complexity: O(nlogn)
        - Space Complexity: O(nlogn)
    
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    
    def merge_sort(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        # 1. Find middle list: Fast-Slow-Pointers
        prev_node = None
        slow = fast = head
        while fast and fast.next:
            prev_node = slow
            slow = slow.next
            fast = fast.next.next
        prev_node.next = None
        
        # 2. Sort the 2 lists:
        l1 = self.merge_sort(head)
        l2 = self.merge_sort(slow)
        
        # 3. Merge 2 lists:
        return self._merge_sorted_lists(l1, l2)
    
    def _merge_sorted_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        prehead = ListNode(0)
        node = prehead
        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
                
            else:
                node.next = l2
                l2 = l2.next
                
            node = node.next
            node.next = None
            
        if l1:
            node.next = l1
        
        elif l2:
            node.next = l2
        
        return prehead.next
        
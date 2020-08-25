# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        values = []
        curr = self
        while curr:
            values.append(str(curr.val))

            curr = curr.next
        values.append('Null')

        return '->'.join(values)

"""
    1. Problem Summary / Clarifications / TDD:
        Output(1->2->3->4->5->6->7->8->Null, 2): 2->1->3->4->6->5->7->8->Null

    2. Inuition:
        - Scan every k nodes
        - Reverse alternatively every k nodes

    3. Tests:
        Output(1->2->3->4->5->6->7->8->Null, 2): 2->1->3->4->6->5->7->8->Null
        Output(1->2->3->4->5->6->7->8->9->Null, 3): 3->2->1->4->5->6->8->7-9->Null

        the last group size < k:
        Output(1->2->3->4->5->6->7->8->Null, 3): 3->2->1->4->5->6->8->7->Null

        Edge cases:
        Empty list: Output(Null, 0): Null
        list with 1 node: Output(1->Null, 1): 1->Null
        k = 1: Output(1->2->3->4->5->6->7->8->Null, 1): 1->2->3->4->5->6->7->8->Null
        k = len(list): Output(1->2->3->4->5->6->7->8->Null, 8): 8->7->6->5->4->3->2->1->Null

    4. Complexity Analysis:
        Time Complexity: O(n)
        Space Complexity: O(1)
    
"""

class Solution:

    def reverse_k_group(self, head:ListNode, k: int) -> ListNode:
        if not head or not head.next or k <= 1:
            return head
        
        prehead = ListNode(0, head)
        prev_tail = prehead
        reverse = True
        while head:
            
            tail = self.__get_kth_node(head, k)
            
            if reverse:
                next_ = tail.next
                tail.next = None
                
                prev_tail.next = self.__reverse(head)
                head.next = next_
            
            else:
                head = tail
                
            prev_tail = head    
            head = head.next
                            
            reverse = not reverse
            
        return prehead.next

    def __get_kth_node(self, head: ListNode, k: int):
        
        k -= 1
        while k and head.next:
            head = head.next
            k -= 1

        return head
    
    def __reverse(self, head: ListNode):
        
        curr = head
        prev = None
        while curr:
            next_ = curr.next
            
            curr.next = prev
            prev = curr
            curr = next_
            
        return prev

def buid_list(node_count):

    prehead = ListNode()

    tail = prehead
    for i in range(1, node_count + 1):
        tail.next = ListNode(i)
        tail = tail.next

    return prehead.next

if __name__ == '__main__':

    k = 0
    print("Edge Case 1. Empty list, k =", k)
    head = buid_list(0)
    print("Nodes of original LinkedList are: ", end='')
    print(head)
    print("Nodes of reversed LinkedList are: ", end='')
    print(Solution().reverse_k_group(head, k))

    k = 1
    print("Edge Case 2. List with 1 node, k =", k)
    head = buid_list(1)
    print("Nodes of original LinkedList are: ", end='')
    print(head)
    print("Nodes of reversed LinkedList are: ", end='')
    print(Solution().reverse_k_group(head, k))

    k = 1
    print("Edge Case 3. k =", k)
    head = buid_list(8)
    print("Nodes of original LinkedList are: ", end='')
    print(head)
    print("Nodes of reversed LinkedList are: ", end='')
    print(Solution().reverse_k_group(head, k))

    k = 2
    print("Case 1. List size % k = 0 and k even, k =", k)
    head = buid_list(8)
    print("Nodes of original LinkedList are: ", end='')
    print(head)
    print("Nodes of reversed LinkedList are: ", end='')
    print(Solution().reverse_k_group(head, k))

    k = 3
    print("Case 2. List size % k = 0 and k odd, k =", k)
    head = buid_list(9)
    print("Nodes of original LinkedList are: ", end='')
    print(head)
    print("Nodes of reversed LinkedList are: ", end='')
    print(Solution().reverse_k_group(head, k))

    k = 4
    print("Case 3. List size % k != 0 and k odd, k =", k)
    head = buid_list(11)
    print("Nodes of original LinkedList are: ", end='')
    print(head)
    print("Nodes of reversed LinkedList are: ", end='')
    print(Solution().reverse_k_group(head, k))

    k = 11
    print("Special Case: k = len(list), k =", k)
    head = buid_list(11)
    print("Nodes of original LinkedList are: ", end='')
    print(head)
    print("Nodes of reversed LinkedList are: ", end='')
    print(Solution().reverse_k_group(head, k))

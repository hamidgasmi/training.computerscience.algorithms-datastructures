# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution_3:
    """ 
        1. It finds the rightmost node (digit) that is not equal to 9
        2. If such a node doesn't exist (all digits are equal to 9), this node is then the list new head with 0 value
        3. Increase this node value by 1
        4. Update its next nodes value to 0

        This solution is the BCR and BCS (Best Conceivale Runtime and Space): O(n) and O(1)
        
    """
    
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def plusOne(self, head: ListNode) -> ListNode:
                
        # 1. Find the rightmost digit < 9
        node = head
        latest_node_less_9 = None
        while node is not None:
            if node.val != 9:
                latest_node_less_9 = node
            
            node = node.next
        
        # 2. If such a node doesn't exist: create a new head
        if latest_node_less_9 is None:
            head = ListNode(0, head)
            latest_node_less_9 = head
        
        # 3. Increase this node value by 1
        latest_node_less_9.val += 1
        
        # 4. Update its next nodes value to 0
        while latest_node_less_9.next is not None:
            latest_node_less_9 = latest_node_less_9.next
            latest_node_less_9.val = 0          
                    
        return head

class Solution_2:
    
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def plusOne(self, head: ListNode) -> ListNode:
        
        # Find all nodes of the linked list
        node = head
        stack = []
        while node is not None:
            stack.append(node)
            node = node.next
            
        # Plus carry
        carry = 1
        while stack:
            
            node = stack.pop()
            
            carry = (node.val + 1) // 10
            node.val = (node.val + 1) % 10            
            
            if carry == 0:
                break
        
        return ListNode(1, head) if carry == 1 else head
        
class Solution_1:
    
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def plusOne(self, head: ListNode) -> ListNode:
        
        carry = self._plus_one_recursive(head, 1)       
        return ListNode(1, head) if carry == 1 else head

    def _plus_one_recursive(self, head: ListNode, carry: int) -> int:
        
        if head.next is not None:
            carry = self._plus_one_recursive(head.next, carry)
            
        if carry == 0:
            return 0
        
        carry = (head.val + 1)// 10
        head.val = (head.val + 1) % 10       
                
        return carry
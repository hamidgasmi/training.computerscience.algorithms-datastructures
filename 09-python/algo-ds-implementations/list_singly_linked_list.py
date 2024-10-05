from list_node import Singly_Linked_Node

class Singly_Linked_List_head:
    def __init__(self, values):
        self.head = self._build_linked_list(values)

    def _build_linked_list(self, values):
        return None

    def get_node_at_pos(self, pos: int):
        assert(pos >= 0)

        node = self.head
        i = 0
        while (not node is None) and (i < pos):
            i += 1
            node = node.next
        
        return node

    def get_node_position(self, node: list_node.Singly_Linked_Node):

        list_node = self.head
        pos = -1
        while not (list_node is None or list_node is node):
            pos += 1
            list_node = list_node.next
        
        return pos

class Singly_Linked_List_head_tail(Singly_Linked_List_head):
    def __init__(self, values):
        (self.head, self.tail) = self._build_linked_list(values)

    def _build_linked_list(self, values):
        return None
class Doubly_Linked_Node:
    def __init__(self, key: int):
        self.prev = None
        self.next = None
        self.key = key
        
class Doubly_Linked_List:
    def __init__(self, head: Doubly_Linked_Node, tail: Doubly_Linked_Node):
        self.head = head
        self.tail = tail
    
    def add(self, node: Doubly_Linked_Node):
        if self.tail == None:
            self.head = node
            self.tail = node
        
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
    
    def remove(self, node: Doubly_Linked_Node):
        if node == self.head == self.tail:
            self.head = None
            self.tail = None
        
        elif node == self.head:
            self.head = self.head.next
            self.head.prev = None
        
        elif node == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        
        elif node.prev and node.next:
            node.prev.next = node.next
            node.next.prev = node.prev

class LRUCache:
    def __init__(self, capacity: int):
        self.__capacity = capacity
        
        self.__key_node_dict = {}
        self.__key_value_dict = {}
        self.__linked_list = Doubly_Linked_List(None, None)
    
    def get(self, key: int) -> int:
        val = self.__key_value_dict.get(key, -1)
        if val == -1:
            return -1
        
        key_node = self.__key_node_dict[key]
        
        self.__linked_list.remove(key_node)
        self.__linked_list.add(key_node)

        return val
    
    def put(self, key: int, value: int) -> None:
        
        self.__key_value_dict[key] = value
        
        key_node = self.__key_node_dict.get(key, None)
        if (key_node):
            self.__linked_list.remove(key_node)
        else:
            key_node = Doubly_Linked_Node(key)
            self.__key_node_dict[key] = key_node
        self.__linked_list.add(key_node)
        
        if len(self.__key_value_dict) > self.__capacity:
            self.__key_node_dict.pop(self.__linked_list.head.key)
            self.__key_value_dict.pop(self.__linked_list.head.key)
            self.__linked_list.remove(self.__linked_list.head)
        
        
class LRU_Cache:
    def __init__(self, capacity: int):
        self.__capacity = capacity
        
        self.__key_node_dict = {}
        self.__key_value_dict = {}
        self.__doubly_linked_list = None
    
    def get(self, key: int) -> int:
        val = self.__dict.get(key, -1)
        if val == -1:
            return -1
        
        key_node = self.__key_node_dict[key]
        
        self.__doubly_linked_list.remove(key_node)
        self.__doubly_linked_list.add(key_node)
        
        return val
    
    def put(self, key: int, value: int) -> None:
        
        self.__key_value_dict[key] = value
        
        if self.__doubly_linked_list.tail.key == key:
            return
        
        key_node = self.__key_node_dict(key, None)
        if (key_node):
            self.__doubly_linked_list.remove(key_node)
            self.__doubly_linked_list.add(key_node)
            return
        
        key_node = Doubly_Linked_Node(key)
        if len(self.__key_value_dict) > self.__capacity:
            self.__doubly_linked_list.remove(self.__doubly_linked_list.head)
        
        self.__doubly_linked_list.add(key_node)
        self.__doubly_linked_list[key] = key_node
    
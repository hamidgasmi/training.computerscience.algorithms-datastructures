#!/usr/bin/env python3.7

class Singly_Linked_Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Doubly_Linked_Nonde(Singly_Linked_Node):
    def __init__(self, val):
        self.prev = None
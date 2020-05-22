import sys

class Queue_Circular_Array:
    def __init__(self, capacity, default_value):
        
        # The array will contain capacity + 1 elements
        self.capacity = capacity
        self._real_capacity = self.capacity + 1
        self.array = [default_value for i in range(self._real_capacity)]
        
        self.read_index = 0
        self.write_index = 0
    
    def size(self):
        return (self.write_index + self._real_capacity - self.read_index) % self._real_capacity

    def empty(self):
        return self.read_index == self.write_index

    def full(self):
        return self.read_index == self.next(self.write_index)

    def next(self, index):
        return 0 if index == self._real_capacity - 1 else index + 1
    
    def enqueue(self, value):

        if self.full():
            return

        self.array[self.write_index] = value
        self.write_index = self.next(self.write_index)

    def dequeue(self):
        
        if self.empty():
            return None
        
        value = self.array[self.read_index]
        self.read_index = self.next(self.read_index)
        
        return value
        
    def get(self, index):
        if index >= self.size():
            return None

        return self.array[(index + self.read_index) % self._real_capacity]

if __name__ == "__main__":

    print("Test Queue Creation: Empty")
    q = Queue_Circular_Array(5, -1)
    print("Read, Write, Array: ", q.read_index, q.write_index, q.array)
    print("Empty: ", q.empty())
    print("Full: ", q.full())
    print("Get {0, 1, 2, 3, 4, 5}: ", [q.get(i) for i in range(q._real_capacity)])
    print("----------------------------------------------------------")

    print("Test Queue 1st. insertion")
    q.enqueue(1)
    print("Read, Write, Array: ", q.read_index, q.write_index, q.array)
    print("Empty: ", q.empty())
    print("Full: ", q.full())
    print("Get {0, 1, 2, 3, 4, 5}: ", [q.get(i) for i in range(q._real_capacity)])
    print("----------------------------------------------------------")

    print("Test Queue last deletion: Empty")
    q.dequeue()
    print("Read, Write, Array: ", q.read_index, q.write_index, q.array)
    print("Empty: ", q.empty())
    print("Full: ", q.full())
    print("Get {0, 1, 2, 3, 4, 5}: ", [q.get(i) for i in range(q._real_capacity)])
    print("----------------------------------------------------------")

    print("Test Queue is Full:")
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    print("Read, Write, Array: ", q.read_index, q.write_index, q.array)
    print("Empty: ", q.empty())
    print("Full: ", q.full())
    print("Get {0, 1, 2, 3, 4, 5}: ", [q.get(i) for i in range(q._real_capacity)])
    print("----------------------------------------------------------")

    print("Test Queue Insertion after it's full")
    q.enqueue(6)
    print("Read, Write, Array: ", q.read_index, q.write_index, q.array)
    print("Empty: ", q.empty())
    print("Full: ", q.full())
    print("Get {0, 1, 2, 3, 4, 5}: ", [q.get(i) for i in range(q._real_capacity)])
    print("----------------------------------------------------------")

    print("Test Queue deletion after it's full:")
    q.dequeue()
    print("Read, Write, Array: ", q.read_index, q.write_index, q.array)
    print("Empty: ", q.empty())
    print("Full: ", q.full())
    print("Get {0, 1, 2, 3, 4, 5}: ", [q.get(i) for i in range(q._real_capacity)])
    print("----------------------------------------------------------")

    print("Test Queue Insertion after it's full and deletion:")
    q.enqueue(6)
    print("Read, Write, Array: ", q.read_index, q.write_index, q.array)
    print("Empty: ", q.empty())
    print("Full: ", q.full())
    print("Get {0, 1, 2, 3, 4, 5}: ", [q.get(i) for i in range(q._real_capacity)])
    print("----------------------------------------------------------")

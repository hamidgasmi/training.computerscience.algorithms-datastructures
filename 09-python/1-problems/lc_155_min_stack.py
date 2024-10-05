# Summary:
#   1. Input: a list of actions
#   2. Output: a value from the stack(Getmin time complexity must be O(1))
#   3. Constraints: pop, top and getMin operations will always be called on non-empty stacks.
# Questions:
#   1. getMin(): Should I remove the item from the stack after the item is retrieved.
# Build my intuition:
#   1. I could use a list to implement the stack:
#      push, pop and top: time complexity O(1)
#      getMin(): time complexity O(|stack|)
#      I won't implement it
import heapq
import math
from collections import namedtuple

# Solution 2: data-structures: a stack in a list and a sorted array
#   Push: O(nlogn) (sorting at each time)
#   Pop: O(n)
#   Top: O(1)
#   GetMin: O(1)
#   Space complexity: O(2 * n) = O(n)
class Min_Stack_Sort:

    def __init__(self):
        self.size = 0
        self.stack = []
        self.sorted_stack = []      

    # Time Complexity: O(nlogn)
    # Space Complexity: O(1)
    def push(self, x: int) -> None:
        self.sorted_stack.append(self.size)
        
        if self.size < len(self.stack):
            self.stack[self.size] = x
        else:
            self.stack.append(x)
        self.size += 1

        self.sorted_stack.sort(key=lambda i: self.stack[i])
    
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def pop(self) -> None:
        self.sorted_stack.remove(self.size - 1)
        self.size -= 1
    
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def top(self) -> int:
        return self.stack[self.size - 1]
    
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def get_min(self) -> int:
        return self.stack[ self.sorted_stack[0] ]

# Solution 3: 2 data-structures: 1 usual stack + a sorted array
#   Push: O(n) (binary search + insertion)
#   Pop: O(n)
#   Top: O(1)
#   getMin: O(1)
#   Space complexity: O(2 * n) = O(n)
class Min_Stack_Binary_Search:

    def __init__(self):
        self.size = 0
        self.stack = []
        self.sorted_stack = []      

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def push(self, x: int) -> None:

        pos = self._binary_search(x) #O(logn)
        if pos >= self.size:
            self.sorted_stack.append(self.size) #O(1)

        else:
            self.sorted_stack.insert(pos, self.size) #O(n)
        
        if self.size < len(self.stack):
            self.stack[self.size] = x #O(1)
        else:
            self.stack.append(x) #O(1)
        self.size += 1

    # Time Complexity: O(logn)
    # Time Complexity: O(1)
    def _binary_search(self, val):

        start = 0
        end = self.size - 1

        while start <= end:

            mid = (start + end) // 2
            mid_stack_pos = self.sorted_stack[mid]
            if self.stack[mid_stack_pos]  == val:
                return mid

            elif self.stack[mid_stack_pos] < val:
                start = mid + 1

            else:
                end = mid - 1

        return start
    
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def pop(self) -> None:
        self.sorted_stack.remove(self.size - 1)
        self.size -= 1
    
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def top(self) -> int:
        return self.stack[self.size - 1]
    
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def get_min(self) -> int:
        return self.stack[ self.sorted_stack[0] ]

# Solution 4: 2 data-structures: a stack + priority queue
#   Push: O(longn)
#   Pup: (logn): I need to pop the item from stack ds and from the priority queue
#   Top: O(1)
#   GetMin: O(1)
#   Space Complexity: O(2 * n) = O(n)
class Min_Stack_Priority_Queue:

    def __init__(self):
        self.size = 0
        self.stack = []
        self.priority_stack = []

    # Time Complexity: O(logn)
    # Space Complexity: O(1)
    def push(self, x: int) -> None:

        heapq.heappush(self.priority_stack, x) #O(logn)
        
        if self.size < len(self.stack):
            self.stack[self.size] = x #O(1)
        else:
            self.stack.append(x) #O(1)
        self.size += 1
    
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def pop(self) -> None:

        pos = self.priority_stack.index(self.top())
        if pos != 0:
            self.priority_stack[pos] = - math.inf
            #heapq._siftup(self.priority_stack, pos)
            heapq._siftdown(self.priority_stack, 0, pos)
        
        heapq.heappop(self.priority_stack)
        
        self.size -= 1
    
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def top(self) -> int:
        return self.stack[self.size - 1]
    
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def get_min(self) -> int:
        return self.priority_stack[ 0 ]


# Solution 5: 1 stack of val - minimum value
#   Push: O(1)
#   Pop: O(1)
#   Top: O(1)
#   GetMin: O(1)
#   Space Complexity: O(2 * n) = O(n) the min value is duplicated on each stack element
Stack_Element = namedtuple('Stack_Element', ['val', 'min'])
class Min_Stack_5:

    def __init__(self):
        self.size = 0
        self.stack = []

    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def push(self, x: int) -> None:
        
        stack_element = None
        if self.size == 0:
            stack_element = Stack_Element(x, x)

        else:
            stack_element = Stack_Element(x, x if x <= self.get_min() else self.get_min())

        if self.size < len(self.stack):
            self.stack[self.size] = stack_element
        else:
            self.stack.append(stack_element) #O(1)
        self.size += 1
    
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def pop(self) -> None:
        
        self.size -= 1
    
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def top(self) -> int:
        return self.stack[self.size - 1].val

    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def _top_element(self) -> Stack_Element:
        return self.stack[self.size - 1]
    
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def get_min(self) -> int:
        return self._top_element().min

# Solution 6. 2 stacks: an usual stack of value + a stack that tracks the position of min value
#   Push: O(1)
#   Pop: O(1)
#   Top: O(1)
#   GetMin: O(1)
#   Space Complexity: Θ(2 * n) = Ω(n)
#       The worst case (O(2 * n)): the stack values are ordered in ascending order
#       The "best" case (O(n)): the stack values are ordered in descending order (there is only 1 min for the whole stack)
class Min_Stack_6:
    
    def __init__(self):
        self.stack_size = 0
        self._min_stack_size = 0
        self.stack = []
        self._min_stack = []

    def push(self, x: int) -> None:
        
        # 1. Push x into the stack
        if self.stack_size < len(self.stack):
            self.stack[self.stack_size] = x

        else:
            self.stack.append(x)
        self.stack_size += 1

        # 2. Check if x is the new min
        if self._min_stack_size > 0:
            stack_min = self.get_min()

        else:
            # The stack is empty, x is the new min
            stack_min = x + 1
        
        if x >= stack_min:
            return

        # 3. Push the new min position in the min stack (tracker)
        if self._min_stack_size < len(self._min_stack):
            self._min_stack[self._min_stack_size] = self.stack_size - 1

        else:
            self._min_stack.append(self.stack_size - 1)

        self._min_stack_size += 1
    
    def pop(self) -> None:
        
        # 1. Pop the value from the stack
        self.stack_size -= 1

        # 2. If the value popped was stack min, pop its position from min_stack
        if self.stack_size == self._min_stack[self._min_stack_size - 1]:
            self._min_stack_size -= 1
    
    def top(self) -> int:
        return self.stack[self.stack_size - 1]
    
    def get_min(self) -> int:
        # 1. Get the min position from min_stack
        min_pos = self._min_stack[self._min_stack_size - 1]

        # 2. return the value of the min
        return self.stack[min_pos]
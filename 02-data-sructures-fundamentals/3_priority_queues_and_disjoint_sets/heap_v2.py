
class Min_Heap:
    # Time Complexity: O(n)
    def __init__(self, arr:[int] = []):
        self.__tree = arr
        self.__heapify()
    
    # Time Complexity: O(1)
    def get_min(self):
        return self.__tree[0]
    
    # Time Complexity: O(logn)
    def extract_min(self):
        min_value = self.__tree[0]
        latest_value = self.__tree.pop()
        if len(self.__tree) == 1:
            return min_value

        self.__tree[0] = latest_value
        self.__sift_down(0)
    
    # Time Complexity: O(logn)
    def change_priority(self, i: int, new_priority: int):
        if i < 0 or i > len(self.__tree):
            return
        
        self.__tree[i] = new_priority

        p = self.__get_parent(i)
        if p != -1 and self.__tree[p] < self.__tree[i]:
            return self.__sift_up(i)
        
        l = self.__get_left(i)
        if l != -1 and self.__tree[l] < self.__tree[i]:
            return self.__sift_down(i)
        
        r = self.__get_left(i)
        if r != -1 and self.__tree[r] < self.__tree[i]:
            return self.__sift_down(i)
    
    # Time Complexity: O(logn)
    def __heapify(self):
        for i in range(len(self.__tree) // 2, -1, -1):
            self.__sift_down(i)
    
    # Time Complexity: O(logn)
    def __sift_down(self, i: int):
        min_idx = i
        node_val = self.__tree[i]
        
        l = self.__get_left(i)
        if l != -1 and self.__tree[l] < self.__tree[min_idx]:
            min_idx = l

        r = self.__get_right(i)
        if r != -1 and self.__tree[r] < self.__tree[min_idx]:
            min_idx = r

        if min_idx != i:
            self.__tree[i], self.__tree[min_idx] = self.__tree[min_idx], self.__tree[i]
            self.__sift_down(min_idx)
    
    # Time Complexity: O(logn)
    def __sift_up(self, i: int):
        p = self.__get_parent(i)
        if p == -1:
            return
        
        if self.__tree[p] < self.__tree[i]:
            self.__tree[i], self.__tree[p] = self.__tree[p], self.__tree[i]
            self.__sift_up(p)

    def __get_parent(self, i):
        parent = (i - 1) // 2

        return parent if parent >= 0 else -1

    def __get_left(self, i):
        left = i * 2 + 1
        return left if left < len(self.__tree) else -1

    def __get_right(self, i):
        right = i * 2 + 1
        return right if right < len(self.__tree) else -1

    def __repr__(self) -> str:
        str_tree = [ '[' ]
        str_tree.append(', '.join([str(val) for val in self.__tree]))
        str_tree.append(']')

        return ' '.join(str_tree)

if __name__ == "__main__":
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    min_heap = Min_Heap(data)

    print(min_heap)

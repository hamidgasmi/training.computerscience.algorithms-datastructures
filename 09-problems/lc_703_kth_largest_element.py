import heapq
class KthLargest_Python_Heap:
    """
        Analysis:
    """
    
    # Time Complexity: O(nlogn + klogk) = O(nlogn)
    # Space Complexity: O(n)
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.max_heap = [(-1) * num for num in nums]
        heapq.heapify(self.max_heap)
        
        self.min_heap = []
        for i in range(self.k - 1):
            heapq.heappush(self.min_heap, (-1) * heapq.heappop(self.max_heap))
            
            
    # Time Complexity: O(logn) for 1 operation
    # Amortized Running Time for p operations (1 initialization + p - 1 add operations)
    #     T = [nlogn + log(n + 1) + ... + log(n + p - 1)]/p
    #     if p ~ n, then T(n) = O(logn)
    #     if p << logn, then T(n) = O(nlogn)
    # Space Complexity: O(1)
    def add(self, val: int) -> int:
        
        # O(logk)
        if len(self.min_heap) > 0 and val > self.min_heap[0]:
            val = heapq.heapreplace(self.min_heap, val)
        
        # O(logn)
        heapq.heappush(self.max_heap, (-1) * val)
        
        return self.max_heap[0] * (-1)


class KthLargest_Binary_Search:
    
    # Time Complexity: O(nlogn)
    # Space Complexity: O(n)
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.sorted_stream = nums.sort(reverse=True)
    
    # Time Complexity: O(n + logn) = O(n) for 1 operation
    # Amortized Running Time for p operations (1 initialization + p - 1 add operations)
    #     T = [nlogn + n + 1 + ... + (n + p - 1)]/p 
    #       = [nlogn + (p - 1)n + (1 + ... + p - 1)]/p = [nlogn + (p - 1)n + p(p - 1)/2]/p
    #       = [nlogn + (p - 1) (n + p/2)]/p
    #     if p >= logn, then T(n) = O(n): linear
    #     if p << logn, then T(n) = O(nlogn)
    # Space Complexity: O(1)
    def add(self, val: int) -> int:
        
        self.sorted_stream.insert(self._binary_search_iterative(val), val)
        #print(self.sorted_stream)
        return self.sorted_stream[self.k - 1]
    
    # Time Complexity: O(logn)
    # Space Complexity: O(1)
    def _binary_search_iterative(self, val: int) -> int:
        
        l = 0
        r = len(self.sorted_stream) - 1
        res = -1
        while l <= r:
            mid = (l + r) // 2
            #print(l, r, mid)
            if val == self.sorted_stream[mid]:
                res = mid
                break
            
            elif val > self.sorted_stream[mid]:
                r = mid - 1
                
            else:
                l = mid + 1
                
            res = l
        
        return res

class KthLargest_Naive:
    
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.sorted_stream = nums

    # Time Complexity: O(nlogn)
    # Amortized Running Time for p operations (1 initialization + p - 1 add operations)
    #     T = [n + (n + 1)logn+1 + ... + (n + p - 1)logn+p-1]/p
    #     if n ~ p, then T(n) = O(nlogn)
    #     if p << n, then T(n) = O(nlogn)
    # Space Complexity: O(1)
    def add(self, val: int) -> int:
        
        self.sorted_stream.append(val)
        self.sorted_stream.sort(reverse=True)

        return self.sorted_stream[self.k - 1]

#["KthLargest","add","add","add","add","add"]
#[[3,[4,5,8,2]],[9],[10],[11],[12],[13]]
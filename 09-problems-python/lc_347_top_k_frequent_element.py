import random

class SolutionQuickSelect:
    
    # Time Complexity: O(n) on average
    # Space Complexity: O(n) due to the dict
    def top_k_frequent(self, nums: List[int], k: int) -> List[int]:
        
        occur_dict = dict()
        unique = []
        for n in nums:
            if not n in occur_dict:
                unique.append(n)
                occur_dict[n] = 0
                
            occur_dict[n] += 1
            
        self._quick_select(unique, occur_dict, k, 0, len(unique) - 1)
        
        return unique[:k]
            
    def _quick_select(self, unique: List[int], occur_dict, k: int, left: int, right: int) -> None:
        
        if left > right:
            return
        
        pivot = self._two_partitions(unique, occur_dict, left, right)
        if pivot == k:
            return
        
        elif pivot < k:
            self._quick_select(unique, occur_dict, k, pivot + 1, right)
            
        else:
            self._quick_select(unique, occur_dict, k, left, pivot - 1)
            
    def _two_partitions(self, unique: List[int], occur_dict, left: int, right: int) -> None:
                
        pivot = random.randint(left, right)
        unique[pivot], unique[right] = unique[right], unique[pivot]
        
        pivot = left - 1
        for i in range(left, right):
            if occur_dict[ unique[i] ] >= occur_dict[ unique[right] ]:
                pivot += 1
                unique[pivot], unique[i] = unique[i], unique[pivot]
        
        pivot += 1
        unique[pivot], unique[right] = unique[right], unique[pivot]
        
        return pivot    

import heapq

class SolutionHeap:

    # Time Complexity: O(n + k + (n-k)logk) = O(n + (n-k)logk)
    # Space Complexity: O(n + k) = O(n)
    def top_k_frequent(self, nums: List[int], k: int) -> List[int]:
        # O(n)  
        occur_dict = dict()
        for n in nums:
            if not n in occur_dict:
                occurence_dict[n] = 0
            
            occur_dict[n] += 1
        
        # O(k + (n-k)logk)
        heap = []     
        for (n, occur) in occur_dict.items():
            len_heap = len(heap)
            if len_heap == k:
                # O(2 * (n - k)logk) = O((n - k)logk)
                if occur > heap[0][0]:
                    heapq.heapreplace(heap, (occur, n))
                    
            else:
                # O(k * 1)
                heap.append((occur, n))
                
                if len_heap == k - 1:
                    # 1 * O(k)
                    heapq.heapify(heap)
        
        # O(k)
        return [n for (occur, n) in heap]
        
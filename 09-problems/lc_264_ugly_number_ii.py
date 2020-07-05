import heapq

class Solution:
    """
    This solution is implemented with a Dynamic Programming approach + bottom up:
    n-th ugly number = min(n previous ugly numbers)

    Ugly numbers are stored in 3 lists: ugly_nbrs_2, ugly_nbrs_3, ugly_nbrs_5
    A list i contains all ugly numbers computed by multiplying a previous ugly number by i

    the min is computed by the min of the 1st unseen number from each list

    """
    
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def nthUglyNumber(self, n: int) -> int:
        
        if n == 0:
            return n
        
        ugly_nbrs_2 = [2]
        ugly_nbrs_3 = [3]
        ugly_nbrs_5 = [5]

        # Indexes to keep track of unseen numbers    
        idx_2 = 0
        idx_3 = 0
        idx_5 = 0
        
        # prev_ugly_nbr is to skip duplicate values
        ugly_nbr = 1
        prev_ugly_nbr = 1
        while n > 1:
            
            ugly_nbr = min(ugly_nbrs_2[idx_2], ugly_nbrs_3[idx_3], ugly_nbrs_5[idx_5])
            if ugly_nbr == ugly_nbrs_2[idx_2]:
                idx_2 += 1
                
            elif ugly_nbr == ugly_nbrs_3[idx_3]:
                idx_3 += 1
                
            else:
                idx_5 += 1
            
            if ugly_nbr == prev_ugly_nbr:
                continue
                
            ugly_nbrs_2.append(ugly_nbr * 2)
            ugly_nbrs_3.append(ugly_nbr * 3)
            ugly_nbrs_5.append(ugly_nbr * 5)
            
            n -= 1
            prev_ugly_nbr = ugly_nbr
        
        return ugly_nbr

class SolutionHeapQ:
    """
        The solution is implemented with a Dynamic Programming approach + bottom up:
        n-th ugly number = min(n previous ugly numbers)

        The min operation is implemented with a min-heap

        The issue in this solution is min operation running time: O(logn)
        See time analysis below

    """
    # Time Complexity: T(n) = Sum(i in [1:n]) T(pop) + 3 T(push)
    #   T(n) = (0 + 0 + 0 + log2) + (log3 + log2 + log3 + log4) + ... + log2i-1 + log(2i - 2) + log(2i - 1) + log(2i) + ...
    #   T(n) < Sum(i in [1:n]) 4 log2i
    #   T(n) < 4 log(2 * 4 * ... * 2i * ... 2n) < 4 log(2**n * 1 * 2 * ... * i * ... * n)
    #   T(n) < 4n + 4 logn!
    #   T(n) = O(n + logn!) = O(nlogn)
    # Space Complexity: S(n) = (3 - 1) + (3 - 1) + ... + (3 - 1) = O(n)
    #   At each iteration, we push 3 items and we pop 1 item.
    def nth_ugly_number(self, n: int) -> int:
        
        if n == 0:
            return n
        
        ugly_nbrs = []
        heapq.heappush(ugly_nbrs, 1)
        
        ugly_nbr = -1
        prev_ugly_nbr = -1
        while n > 0:
            
            ugly_nbr = heapq.heappop(ugly_nbrs)
            if ugly_nbr == prev_ugly_nbr:
                continue
                
            heapq.heappush(ugly_nbrs, ugly_nbr * 2)
            heapq.heappush(ugly_nbrs, ugly_nbr * 3)
            heapq.heappush(ugly_nbrs, ugly_nbr * 5)
            
            n -= 1
            prev_ugly_nbr = ugly_nbr
        
        return ugly_nbr

class SolutionBFS:
    """
        Ugly numbers could be seen as a 3-ary tree which the number 1 is the root
                        1
                     /  |  \
                    2   3    5
                / / |  /|\   \  \  \
               4 6 10 6 9 15 10 15 25
              /|
             8 12
        This 3-ary tree could be traversed with a BFS approach
        For all node of a level (i), we compute the node of level (i + 1)

        Even though, nodes values is increasing, they aren't sorted neither inside levels nor between levels

        The challenge is therefore how to find the nth ugly number.

        My solution is to store all ugly numbers sorted.
        I stop when I reach a length of n and the last item is less than the min ugly number visited in the current level

        It's not efficient!
        I shouldn't split nodes by level.
        I should have all tree nodes together and get the next value as the min of all node.
        Solution: Min Heap.

    """
    def nth_ugly_number(self, n: int) -> int:
        
        if n <= 1:
            return n
        
        n_ugly_nbrs = [1]
        curr_level = [1]
        while n > 0:
            
            next_level = []
            curr_min_ugly = math.inf
            for ugly_n in curr_level:
                
                next_ugly = ugly_n * 2
                if not next_ugly in next_level:
                    next_level.append(next_ugly)
                    curr_min_ugly = min(curr_min_ugly, next_ugly)
                
                next_ugly = ugly_n * 3
                if not next_ugly in next_level:
                    next_level.append(next_ugly)
                    curr_min_ugly = min(curr_min_ugly, next_ugly)
                               
                next_ugly = ugly_n * 5
                if not next_ugly in next_level:
                    next_level.append(next_ugly)
                    curr_min_ugly = min(curr_min_ugly, next_ugly)
            
            curr_level = next_level
            n_ugly_nbrs.extend(next_level)
            n_ugly_nbrs.sort()
            if len(n_ugly_nbrs) >= n and n_ugly_nbrs[n - 1] <= curr_min_ugly:
                break               
        
        return n_ugly_nbrs[n - 1]
                
        
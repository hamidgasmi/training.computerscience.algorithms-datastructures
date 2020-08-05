class Solution_3_Pointers_Count:
        
    def three_sum_multi(self, A: List[int], target: int) -> int:
        
        mod = 10**9 + 7
        
        count = collections.Counter(A)
        keys = sorted(count)
        
        keys_len = len(keys)
        
        three_sum_count = 0
        for i in range(keys_len):
            
            a = keys[i]
            
            two_sum_target = target - keys[i]

            l, r = i, keys_len - 1
            while l <= r:
                
                candidate_two_sum = keys[l] + keys[r]
                if candidate_two_sum < two_sum_target:
                    l += 1
                
                elif candidate_two_sum > two_sum_target:
                    r -= 1
                
                else:
                    b, c = keys[l], keys[r]
                    if i < l < r:
                        three_sum_count += count[a] * count[b] * count[c]
                        
                    elif i == l < r:
                        three_sum_count += ((count[a] * (count[a] - 1)) // 2) * count[c]
                        
                    elif i < l == r:
                        three_sum_count += count[a] * (count[b] * (count[b] - 1)) // 2
                        
                    else:  # i == l == r
                        three_sum_count += count[a] * (count[a] - 1) * (count[a] - 2) // 6

                    l += 1
                    r -= 1
        
        return three_sum_count % mod

class Solution_3_Pointers:
        
    def three_sum_multi(self, A: List[int], target: int) -> int:
        
        A_len = len(A)
        mod = 10**9 + 7    
                
        A.sort()
        
        three_sum_count = 0
        for i in range(A_len):

            two_sum_target = target - A[i]

            l, r = i + 1, A_len - 1
            while l < r:

                candidate_two_sum = A[l] + A[r]
                if candidate_two_sum < two_sum_target:
                    l += 1

                elif candidate_two_sum > two_sum_target:
                    r -= 1
                    
                elif A[l] == A[r]:
                    three_sum_count += (r - l + 1) * (r - l) // 2
                    three_sum_count %= mod
                    break
                    
                else:
                    val = A[l]
                    l_val_count = 1
                    while l + 1 < r and A[l + 1] == val:
                        l += 1
                        l_val_count += 1
                    
                    val = A[r]
                    r_val_count = 1
                    while l < r - 1 and A[r - 1] == val:
                        r -= 1
                        r_val_count += 1
                    
                    three_sum_count += l_val_count * r_val_count
                    three_sum_count %= mod
                    
                    l += 1
                    r -= 1
        
        return three_sum_count
'''
Problem: Exact pattern matching
    - Input: a text (T), a pattern (P)
    - Output: 1 or all occurences of P in T

Algorithm:
    - Hashing function: H(S: str, n: int, m: int) = Sum(S[i] * x^i-n % p) for n <= i < m
    - Compute H(P, 0, |P|)
    - Compute H(T, 0, |P|)
    - H(S, n + 1, m + 1) = (H(S, n, m) - S[n]) / x + S[m] * x^m-n-1 % p
    - Loop through T:
        - Compute H(T, i + 1, i + 1 + |P|) by using H(T, i, i + |P|) in O(1) time complexity
        - Compare it with H(P)

Questions:
    - How to choose the multiplier and the prime numbers?
    - How to make the trade-off between collision numbers and performance of recurrence calculation for H[i]?
    - More the prime is bigger, less false positive we gets. This is supposed to make our code faster.
    - In the other hand, more the prime is bigger, the related division and multiplication operations get slower.

'''

class Rabin_Karp:
    def __init__(self):
        self.__multiplier = 31
        self._prime = 1000000007

        self.__multiplier_power_prime = self.__multiplier ** self._prime % self._prime

    def __abs_hash__(self, s: str, length: int) -> int:
        assert(length < len(s))
        
        hash, power_x = 0, 1
        for idx in range(length):
            hash += ord(s[idx]) * power_x
            hash %= self.__prime

            power_x *= self.__multiplier
        
        return hash

    def __rel_hash(self, s: str, prev_hash: int, idx: int, length: int) -> int:
        assert(0 < idx < len(s))

        return (prev_hash - s[idx - 1]) // self.__multiplier + s[idx + length - 1] * self.__multiplier

    def find(self, t: str, p: str) -> List[int]:
        len_t = len(t)
        len_p = len(p)
        if len_p > len_t:
            return []

        # 1. find hash functions for t and p
        hash_p = self.__abs_hash__(p, len_p)
        hash_t = self.__abs_hash__(t, len_p)

        # 2. find all occurences
        occurences = []
        if hash_p == hash_t:
            occurences.append(0)
        for idx in range(1, len_t):
            hash_t = self.__rel_hash(t, hash_t, idx, len_p)
            if hash_p == hash_t and p == t[idx:idx+len_p]:
                occurences.append(idx)
        
        return occurences



    
        
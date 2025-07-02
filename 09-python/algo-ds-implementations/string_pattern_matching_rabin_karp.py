'''
    Rabin-Karp (rolling hash)
        1. Problem Summary / Clarifications / TDD:
            - inputs: (text, pattern) 2 strings containing lowercase English letters. 
            - Output: count all occurences of pattern in text

            p: pattern length
            m: multiplier (263)
            prime: (1000000007)

            - Hashing familly: 
                H(i): hash function (Polynomial) of a substring of S from i to i + p
            
            - Rolling Hash:
                H(0) = S0 * m^p-1 + S1 * m^p-2 + ... + Sp-1 * m^0
                H(1) =              S1 * m^p-1 + ... + Sp-1 * m^1 + Sp * m^0
                H(1) = F(0) * m - S0 * m^p + Sp * m^0

            - Details (how did we choose the hashing function and the rolling hash method?)
                - Option 1: 
                    H(0) = S0 * M^p-1 + S1 * M^p-2 + S2 * M^p-3 + ... + Sp-1 * M^0
                    H(1) =              S1 * M^p-1 + S2 * M^p-2 + ... + Sp-1 * M^1 + Sp * M^0
                    Rolling hash: remove Si * M^p-1 when moving from H(i) to H(i+1)
                        Option 1.1: H(1) = (H(0) - S0 * M^p-1) * M + Sp
                        Option 1.2: H(1) = H(0) * M - S0 * M^p + Sp
                    
                - Option 2:
                    H(0) = S0 * M^0 + S1 * M^1 + S2 * M^2 + ... + Sp-1 * M^p-1
                    H(1) =          + S1 * M^0 + S2 * M^1 + ... + Sp-1 * M^p-2 + Sp * M^p-1
                    H(1) = (H(0) - S0 * M^0) / M + Sp * M^p-1
                    Rolling hash: remove Si when moving from H(i) to H(i+1)
                    Requires to divide F(i-1)

                - Go with Option 1.2

        5. Complexity Analysis:
            - Time Complexity: O(|text| * |Pattern|)
            - Space Compexity: O(|Pattern|)
'''
import utility_devel

class Rabin_Karp:
    def __init__(self):
        self.__m = 263
        self.__prime = 1000000007
        self.__encode = lambda c: ord(c) - 96
    
    def count_occurrences(self, text: str, pattern: str) -> int:
        n, p = len(text), len(pattern)
        if n < p or p == 0: return 0

        # O(p)
        m_pow_p = m
        rolling_hash, pattern_hash = self.__encode(text[0]), self.__encode(pattern[0])
        for i in range(1, p):
            m_pow_p = (m_pow_p * self.__m) % prime
            rolling_hash = (rolling_hash * self.__m + self.__encode(text[i])) % prime
            pattern_hash = (pattern_hash * self.__m + self.__encode(pattern[i])) % prime

        # O(p)
        occurences = 1 if rolling_hash == pattern_hash and s[:p] == pattern else 0

        # O((n - 1) * p)
        for r in range(p, n):
            rolling_hash = (rolling_hash * m - self.__encode(s[r - p]) * m_pow_p + self.__encode(s[r])) % prime

            if rolling_hash == pattern_hash and s[r - p + 1 : r + 1] == pattern: occurences += 1

        return occurences

if __name__ == "__main__":
    unit_test = utility_devel.Unit_Tests_Utility()
    unit_test.get_inputs()
    unit_test.get_outputs()

    rabin_karp = Rabin_Karp()

    for i in range(len(unit_test.inputs)):
        [text, pattern] = unit_test.inputs[i]
        [expected] = unit_test.outputs[i]
        print(f'Occurences of "{pattern}" in "{text}": (expected, output) = ({expected}, {rabin_karp.count_occurrences(text, pattern)})')

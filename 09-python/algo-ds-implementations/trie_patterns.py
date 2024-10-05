'''
    Multiple Exact Patterns Matching
    Input: 
        - A list of strings Patterns = [ P0, P1, ..., Pn ]
        - A string S
    
    Output: 
        - All positions in S where a string Pi from Patterns appears as a substring in S
    
    Time and Space Complexity:
        - Time Complexity: O(|S| * max(|Pi|) + Sum(|Pi|)) for for 0 <= i <= n
            - T(build Trie) = O(Sum(|Pi|) for 0 <= i <= n) = O(|Patterns|)
            - T(Search in Trie) = (|S| * max(|Pi|))
        - Space Complexity:
            - S(Trie) + S(Output) = O(Sum(|Pi|) for 0 <= i <= n) + O(|S|) = O(|S| + |Patterns|)
            - S(Output): in the worst case, output contains all positions in |S|
    
    Implementation Assumptions:
        - Trie is a dictionary of a dictionary
        - A leaf has '$' as a child

        Patterns: aba, aa, baa
              Trie
              /  \
            a     b
           / \     \
          b   a     a
         /    |      \
        a     $       a
        |             |
        $             $

'''

class Trie:
    # Time: O(1)
    # Space: O(1)
    def __init__(self):
        self.__root = dict()
        self.__leaf_character = '$'
    
    # Time: O(1) in average
    # Space: O(1)
    def is_leaf(self, node: dict) -> bool:
        return True if node and self.__leaf_character in node else False

    # Time: O(|pattern|)
    # Space: O(|pattern|)   
    def add(self, pattern: str):
        if not pattern:
            return
        
        node = self.__root
        for c in pattern:
            if not c in node:
                node[c] = dict()
            node = node[c]
        if not self.is_leaf(node):
            node[ self.__leaf_character ] = None
    
    # Time: P(max(|Pi|))
    # Space: O(1)
    def search(self, s: str, start: int) -> bool:

        node = self.__root
        for idx in range(start, len(s)):
            node = node.get(s[idx], None)
            if not node:
                break
        
        return True if self.is_leaf(node) else False


class Exact_Patterns_Matching_Solution:
    def __init__(self, patterns: list[str]):
        self.__patterns_trie = self.__build_trie(patterns)
    
    # Time Complexity: O(sum(|Pi|))
    # Space Complexity: O(sum(|Pi|))
    def __build_trie(self, patterns: list[str]) -> Trie:
        trie = Trie()
        for pattern in patterns:
            trie.add(pattern)
        
        return trie
    
    # Time complexity: O(|s| * max(|Pi|))
    # Space Complexity: O(|s|)
    def multi_pattern_matching(self, s: str) -> list[int]:
        matching_positions = []
        for p in range(len(s)):
            if self.__patterns_trie.search(s, p):
                matching_positions.append(p)
        
        return matching_positions


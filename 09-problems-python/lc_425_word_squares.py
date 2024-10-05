"""
    1. Problem Summary / Clarifications / TDD:
    
    2. Intuition:
        - All words have the same length => the word square length must have the words length
        
        wall
        area
        lead
        lean
        lady
        
    3. Complexity Analysis:
        W the size of a word
        N the size of the list of words
        
        W^W
        
        
"""

class Trie:
    def __init__(self, words: List[str]):
        self.root = {}
        
        for i in range(len(words)):
            self.append(words[i], i)
        
    def append(self, word: str, idx: int):
        
        trie_node = self.root
        for c in word:
            if c in trie_node:
                print(c, idx, trie_node)
                trie_node['$'].append(idx)
            else:
                trie_node[c] = {'$': [idx]}
            trie_node = trie_node[c]
        
    def find(self, pattern:[str]) -> List[str]:
        
        node = self.root
        for c in pattern:
            if c not in node:
                return []
            node = node[c]
        
        return node['$']
                
class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        
        self.square_len = len(words[0])
        
        trie = Trie(words)
        #print(trie.root)
        #print(trie.find(['b']))
        
        all_words_squares = []
        for word in words:
            self.find_word_squares(trie, 1, [word], all_words_squares)
                
        return all_words_squares
    
    def find_word_squares(self, trie: Trie, k: int, square: List[str], all_words_squares: List[List[str]]):
        if k == self.square_len:
            all_words_squares.append(square.copy())
            
            return
        
        prefix = []
        for word in square:
            prefix.append(word[k])
        kth_word_candidates = trie.find(prefix)
        
        for word in kth_word_candidates:
            square.append(word)
            self.find_word_squares(trie, k + 1, square, all_words_squares)
            square.pop()
        
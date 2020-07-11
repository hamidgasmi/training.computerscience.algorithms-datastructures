
class T9:
    """
        Question 1: What should I return if there are a big number of matching words?

    """
    def __init__(self, digit_char_mapping: List[str]=None):
        
        self.trie_root = None

        self.digit_char_dict = self._initialize_mapping(digit_char_mapping)
    
    def _initialize_mapping(self, digit_char_mapping: List[str]=None) -> dict:

        if digit_char_mapping is None:
            self.digit_char_dict = {0:['w', 'x', 'y', 'z'],
                                    1:[], 
                                    2:['a', 'b', 'c'], 
                                    3:['d', 'e', 'f'], 
                                    4:['g', 'h', 'i'], 
                                    5:['j', 'k', 'l'], 
                                    6:['m', 'n', 'o'], 
                                    7:['p', 'q', 'r','s'], 
                                    8:['t', 'u', 'v'], 
                                    9:['w', 'x', 'y', 'z']}
        else:
            assert(len(digit_char_mapping) == 10)

            for i in range(10):
                self.digit_char_dict[i] = []
                
                for char in digit_char_mapping[i]:
                    assert(len(char) == 1)

                    self.digit_char_dict[i].append(char)


    def matching_words(self, input: str) -> List[str]:
        input_len = len(input)

        if input_len == 0:
            return []

        # 1. Get all trie nodes that are matching to the input
        trie_nodes = self.matching_words(input, 0, self.trie_root, [])

        # 2. Get all words 
        words_list = []
        for node in trie_nodes:
            words_list.extend(self._extract_words_from_trie(node))

        return words_list

    def _search_trie(self, input: str, start:int, root, word_prefix: List[str]):

        input_len = len(input)
        if start >= input_len:
            return []

        elif root is None:
            return []
        
        trie_nodes = []
        for c in self.digit_char_dict[ input[start] ]:

            c_node = self._search_char_trie(c, root)
            if c_node is None:
                continue

            if start == input_len - 1:
                trie_nodes.append((word_prefix, c_node))
            
            else:
                trie_nodes.extend(self._search_trie(input, start + 1, c_node, word_prefix + [c]))
        
        return trie_nodes
    
    def _extract_words_from_trie(self, node) -> List[str]:
        return []

    def _search_char_trie(self, root, c: str):
        return None
        

        





import sys

class Burrows_Wheeler_Inverse:
    def __init__(self):
        self.alphabet = dict()
        self.alphabet["$"] = 0
        self.alphabet["A"] = 1
        self.alphabet["C"] = 2
        self.alphabet["G"] = 3
        self.alphabet["T"] = 4

    # O(|text|)
    def inverse(self, bwt_text):

        # O(|text|)
        last_column = [c for c in bwt_text]

        # O(|text|)
        first_column = [c for c in bwt_text]
        self.count_sort(first_column)

        # O(|text|)
        last_to_first = self.build_last_to_first(first_column, last_column)

        origin_text_list = []
        origin_text_list.append(first_column[0])

        # O(|text|)
        i = 0
        while last_to_first[i] != 0:
            i = last_to_first[i]
            origin_text_list.append(first_column[i])

        # O(|text|)
        origin_text_list.reverse()

        # O(|text|)
        return ''.join(origin_text_list)

    # O(Text)
    def count_sort(self, char_list):
        count = [0 for _ in range(len(self.alphabet))]

        for c in char_list:
            i = self.alphabet[c]
            count[i] += 1
        
        i = 0
        for c in self.alphabet:
            index = self.alphabet[c]
            for _ in range(count[index]):
                char_list[i] = c
                i += 1

    def build_last_to_first(self, first_column, last_column):
        last_to_first = []

        first_occurence = dict()
        for i in range(len(first_column)):
            c = first_column[i]
            if not c in first_occurence:
                first_occurence[c] = i

        char_count = dict()
        for i in range(len(last_column)):
            c = last_column[i]

            if c in char_count:
                count = char_count[c]
                char_count[c] += 1
            else:
                char_count[c] = 1
                count = 0

            last_to_first.append(first_occurence[c] + count)
        
        return last_to_first

if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    
    bwt_inverse = Burrows_Wheeler_Inverse()

    print(bwt_inverse.inverse(bwt))

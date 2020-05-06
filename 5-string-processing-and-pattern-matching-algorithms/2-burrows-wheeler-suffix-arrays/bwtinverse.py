# python3
import sys

class Burrows_Wheeler_Inverse:

    def inverse(self, bwt_text):

        last_column = [c for c in bwt_text]
        first_column = [c for c in bwt_text]
        first_column.sort()
        last_to_first = self.build_last_to_first(first_column, last_column)

        origin_text_list = []
        origin_text_list.append(first_column[0])

        i = 0
        while last_to_first[i] != 0:
            i = last_to_first[i]
            origin_text_list.append(first_column[i])

        origin_text_list.reverse()

        return ''.join(origin_text_list)

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

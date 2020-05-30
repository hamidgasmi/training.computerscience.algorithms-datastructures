import sys

def naive_solution(text):

    suffix_list = [i for i in range(len(text))]
    
    suffix_list.sort(key=lambda i: text[i:])

    return suffix_list
        
if __name__ == '__main__':
  
    text = sys.stdin.readline().strip()

    print(" ".join(map(str, naive_solution(text))))

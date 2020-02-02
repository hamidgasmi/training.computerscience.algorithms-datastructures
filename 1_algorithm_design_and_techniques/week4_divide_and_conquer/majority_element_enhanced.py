import sys

# O(n) 
def get_majority_element(a):
    
    #Dictionary with (Key, Occurences) pairs
    dic = {}
    for i in range(len(a)):
        if a[i] in dic: dic[a[i]] += 1
        else: dic[a[i]] = 1

    for val in dic.values():
        if val > len(a) // 2: return 1

    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    
    print(get_majority_element(a))
        
#python3 majority_element_enhanced.py <<< "5 2 3 9 2 2"
#python3 majority_element_enhanced.py <<< "4 1 2 3 4"
#python3 majority_element_enhanced.py <<< "4 1 2 3 1"
#python3 majority_element_enhanced.py <<< "10 512766168 717383758 5 126144732 5 573799007 5 5 5 405079772"
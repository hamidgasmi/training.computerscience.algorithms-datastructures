from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])

def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

#Time complexity: O(n)
#Space complexity: O(n)
def find_mismatch(text):
    
    opening_brackets_stack = []
    
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(i)

        elif next in ")]}":
            stackCount = len(opening_brackets_stack)
            if  stackCount == 0:
                return i + 1
            
            index = opening_brackets_stack[stackCount - 1]
            if not are_matching(text[index], next):
                return i + 1

            opening_brackets_stack.pop(stackCount - 1)

    stackCount = len(opening_brackets_stack)
    if  stackCount == 0:
        return 0
    else:
        return opening_brackets_stack[stackCount - 1] + 1
                
def main():
    text = input()
    mismatch = find_mismatch(text)

    if mismatch == 0:
        print("Success")
    else:
        print(mismatch)

if __name__ == "__main__":
    main()

#python3 check_brackets.py <<< "a+b"
#python3 check_brackets.py <<< "[]{}()"
#python3 check_brackets.py <<< "{[()]}"
#python3 check_brackets.py <<< "{[(a+b)]}(skjhweu83-0239*/+)"
#python3 check_brackets.py <<< "{"
#python3 check_brackets.py <<< "{]"
#python3 check_brackets.py <<< "{])"
#python3 check_brackets.py <<< "{}[()"
#python3 check_brackets.py <<< "{}[(){"
#python3 check_brackets.py <<< "{}[(){()}a+b"
#python3 check_brackets.py <<< "{[}"
"""
    1. Problem Summary / Clarifications / TDD:
        ["2", "1", "+", "3", "*"]
            9
            5
            -208
            
    
"""

class Solution:
    def __init__(self):
                
        self.operators = {
            "+": lambda b, a: a + b,
            "-": lambda b, a: a - b,
            "/": lambda b, a: int(a / b),
            "*": lambda b, a: a * b
        }
        
    def evalRPN(self, tokens: List[str]) -> int:
                
        stack = []
        for token in tokens:
            
            if token in self.operators:                
                stack.append(self.operators[token](stack.pop(), stack.pop()))
                
            else:
                stack.append(int(token))               
        
        return stack[-1]
    
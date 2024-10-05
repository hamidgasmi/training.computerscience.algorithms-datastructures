class Solution:
    """ 
    Clarifications:
       1. The division (/) corresponds to the floor division (//)
       2. The integers could have multiple digits
       3. The operators precedence is: (/,*), (+,-), from left to right

    Intuition:
        1. Extract expressions terms one by one
        2. Compute 1st.: (*, /) and then (+,-)
        3. To compute *,/ operators use a stack
        4. To compute +,- operators use a queue (because of left, right precedence)
            E.g. 4 * 3 + 20 / 2:
            _Operation: * /|__Stack of Nbrs__|__Stack of Operators__
             1.Extract: 4  | None            | None
             2.Push(4)     | 4               | None
             3.Extract: *  | 4               | None
             4.Extract: 3  | 4               | None
             5.Pop: 4      | 4               | None
             6.Push: 4 * 3 | 12              | None
             7.Extract: +  | 12              | None
             8.Push: +     | 12              | +
             9.Push: +     | 12              | +
            10.Extract: 20 | 12              | +
            11.Push: 20    | 12 20           | +
            12.Extract: /  | 12 20           | +
            13.Extract: 2  | 12 20           | +
            14.Pop: 20     | 12              | +
            15.Push: 20 / 2| 12 10           | +

            _Operation: + -|__Stack of Nbrs__|__Stack of Operators__
            16.Dequeue a=12| 10              | +
            17.Dequeue +   | 10              | None
            18.Dequeue 10  | None            |
            19.a +=10      | None            |
            19.Return a=22 | None            |
        
        E.g. 1-1+1:
            _Operation: * /|__Stack of Nbrs__|__Stack of Operators__
             1.Extract: 1  | None            | None
             2.Push(1)     | 1               | None
             3.Extract: -  | 1               | None
             4.Push(-)     | 1               | -
             5.Extract: 1  | 1               | -
             6.Push(1)     | 1 1             | -
             7.Extract: +  | 1 1             | -
             8.Push(+)     | 1 1             | - +
             9.Extract(1)  | 1 1 1           | - +

            _Operation: + -|__Stack of Nbrs__|__Stack of Operators__
            10.Dequeue a=1 | 1 1             | - +
            11.Dequeue -   | 1 1             | +
            12.Dequeue 1   | 1               | +
            13.a -= 1 = 0  | 1               | +
            14.Dequeue +   | 1               | None
            15.Dequeue 1   | None            | None
            16.a += 1      | None            | None
            17. Return a=1 | None            | None

    Time and Space Analysis:
        Time Complexity: O(|s|)
        Space Complexity: O(|s|)
    """
    def calculate(self, s: str) -> int:

        # 1. Computes * and /        
        nbr_stack = []
        opr_stack = []
        
        len_s = len(s)

        i, a = self._extract_term(s, 0)
        nbr_stack.append(int(a))
        while i < len_s:
            i, opr = self._extract_term(s, i)
            if opr in '-+':
                opr_stack.append(opr)
                
                i, a = self._extract_term(s, i)
                nbr_stack.append(int(a))
                
            else:
                a = nbr_stack.pop()
                i, b = self._extract_term(s, i)
                
                if opr == '/':
                    nbr_stack.append(a //int(b))
                    
                else:
                    nbr_stack.append(a * int(b))
        
        # 2. Compute + and -
        opr_idx = 0
        nbr_idx = 1
        a = nbr_stack[0]
        while nbr_idx < len(nbr_stack) and opr_idx < len(opr_stack):
            if opr_stack[opr_idx] == '+':
                a += nbr_stack[nbr_idx]
            else:
                a -= nbr_stack[nbr_idx]
                
            nbr_idx += 1
            opr_idx += 1           
        
        return a
            
    def _extract_term(self, s: str, start: int) -> (int, str):
        
        s_len = len(s)

        # 1. Skip spaces
        while start < s_len and s[start] == ' ':
            start += 1
        
        if start == s_len:
            return (start, '')
        
        # 2. Extract an operator
        if s[start] in '-+*/':
            return (start + 1, s[start])
        
        # 3. Extract a number
        i = start
        while i < s_len and not s[i] in '-+*/':
            i += 1
        
        return (i, s[start:i])
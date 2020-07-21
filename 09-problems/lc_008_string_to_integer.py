"""
    1. Problem Summary / Clarifications / TDD:

        Q1. What if is there is a space between the sign and the number? (see cases 5 and 6).
        Q2.  What if the result is not an int. Python manages overflow issues. (see case 12 and 14).
    
        Case.01. myAtoi("           ") = 0          (a non valid number with spaces only)
        Case.02. myAtoi("words      ") = 0          (a non valid number only)
        Case.03. myAtoi("words12365 ") = 0          (a non valid number is followed by a valid number I)
        Case.04. myAtoi("words 1236 ") = 0          (a non valid number is followed by a valid number II)
        Case.05. myAtoi("+ 4193"     ) = 0          (a non valid number: space between sign and number I)
        Case.06. myAtoi("- 4193    " ) = 0          (a non valid number: space between sign and number II)
        
        Case.07. myAtoi("4193"       ) = 4193       (a valid number only)
        Case.08. myAtoi("4193word"   ) = 4193       (a valid number is followed by a non valid number I)
        Case.09. myAtoi("4193 word"  ) = 4193       (a valid number is followed by a non valid number II)
        Case.10. myAtoi("4193 12 wo" ) = 4193       (a valid number is followed by a another valid number)
        Case.11. myAtoi("+4193"      ) = 4193       (a positive valid number with the sign +)
        Case.12. myAtoi("+2147483648") = 2147483647 (positive number greater than int max value)
        Case.13. myAtoi("-4193"      ) = -4193      (a negatve valid number with the sign -)
        Case.14. myAtoi("-2147483649") = -2147483648(negative number less than int min value)
        
    2. Intuition:
        1. Extract the number (str_num) from s
        2. Extract the sign from str_num
        3. Loop on each digit of str_num and compute the conversion in num
        4. Break when a non digit char is found or num reach max/min int
        5. Return num * sign
        
    3. Implementation: See below
    4. Tests: Use all tests created in step 1 (TDD)
    5. Analysis:
        
        Time Complexity: O(|s|)
        Space Complexity: O(|s|)
        
        Could we do better:
            Time Complexity: 
                We can't in term of asymptotique analysis
                But if we don't use the split function and "break" as soon as a non valid digit is found, the code may be faster 
            Space Complexity:
                Yes, we could make it O(1) if we loop on each character of s 
    
"""

class Solution:
    
    def atoi(self, s: str) -> int:
        str_list = s.split()
        
        if not str_list:
            return 0
                
        num_str = str_list[0]
        sign = -1 if num_str[0] == '-' else +1
        start = 1 if num_str[0] in '-+' else 0
        
        num = 0
        int_boundary =  0x80000000 if sign == -1 else 0x7fffffff # 2147483648 or 2147483647
        
        for i in range(start, len(num_str)):
            
            ord_digit = ord(num_str[i])
            if ord_digit < 48 or ord_digit > 57:
                break
            
            num *= 10
            num += ord_digit - 48
            
            if num >= int_boundary:
                num = int_boundary
                break
        
        return num * sign

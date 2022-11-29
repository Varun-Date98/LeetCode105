'''
20. Valid Parentheses | Easy
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']'
determine if the input string is valid.
An input string is valid if:
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.
    3. Every close bracket has a corresponding open bracket of the same type.
---------------------------------------------------------------------------------

'''


def isValid(s: str) -> bool:
    stack = []

    for c in s:
        if c == '(':
            stack.append(')')
        elif c == '[':
            stack.append(']')
        elif c == '{':
            stack.append('}')
        elif not stack or stack.pop() != c:
            return False
    
    return len(stack) == 0

from typing import List

'''
17. Letter Combinations of a Phone Number | Medium
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number
could represent. Return the answer in any order. A mapping of digits to letters (just like on the telephone buttons)
is given below. Note that 1 does not map to any letters.

    2 -> ['a', 'b', 'c']
    3 -> ['d', 'e', 'f']
    4 -> ['g', 'h', 'i']
    5 -> ['j', 'k', 'l']
    6 -> ['m', 'n', 'o']
    7 -> ['p', 'q', 'r', 's']
    8 -> ['t', 'u', 'v']
    9 -> ['w', 'x', 'y', 'z']

-----------------------------------------------------------------------------------------------------------------------
Use Depth First Search to include or exclude the alphabets corresponding to the digit and form the strings
'''


def letterCombinations(digits: str) -> List[str]:
    if len(digits) == 0: return []
    
    res = []
    digitToChar = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    def dfs(i: int, cur: str) -> None:
        if i == len(digits):
            res.append(cur)
            return
        
        for c in digitToChar[digits[i]]:
            dfs(i + 1, cur + c)
    
    dfs(0, "")

    return res
'''
10. Regular Expression Matching | Hard
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
    '.' Matches any single character.
    '*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).
-------------------------------------------------------------------------------------------------------------------
Top - down dynamic programming solution
'''

def regularExpressionMatching(s: str, p: str) -> bool:
    cache = {}

    def backtracking(i: int, j: int) -> bool:
        if (i, j) in cache:
            return cache[(i, j)]
        
        if i >= len(s) and j >= len(p):
            return True
        
        if i >= len(s):
            return False
        
        match = i < len(s) and (s[i] == p[j] or p[j] == '.')

        if j + 1 < len(p) and p[j + 1] == '*':
            cache[(i, j)] = (
                (match and backtracking(i + 1, j)) or   # Use the *
                (backtracking(i, j + 1))                # Do not use the *
            )

            return cache[(i, j)]
        
        if match:
            cache[(i, j)] = backtracking(i + 1, j + 1)
            return cache[(i, j)]
        
        cache[(i, j)] = False
        return False
    
    return backtracking(0, 0)
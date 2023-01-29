from typing import List

'''
38. Count and Say | Medium
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
    countAndSay(1) = "1"
    countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1),
    which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of substrings such
that each substring contains exactly one unique digit. Then for each substring, say the number
of digits, then say the digit. Finally, concatenate every said digit.

For example, the saying and conversion for digit string "3322251":
    3322251 => two 3s, three 2s, one 5, one 1 => 23321511
-----------------------------------------------------------------------------------------------
Seeing this problem for the first time in an interview can be tough, try to write the next sequences
and find a pattern. To begin write a function that gives us the counts of each element in the string,
next write a function to turn the counts into the next term of the sequence.
    n0 => count() => [count, num] in n => say() => n1

This can also be done iteratively by running a loop n - 2 times and generating the ith term in each loop
'''


def countAndSay(n: int) -> str:
    def count(s: str) -> List[List[object]]:
        l, r = 0, 0
        counts = []

        while l < len(s):
            while r < len(s) - 1 and s[l] == s[r]:
                r += 1
            
            counts.append([r - l, s[l]])
            l = r
        
        return counts
    
    def say(counts: List[List[object]]) -> str:
        res = ''

        for count, char in counts:
            res += (char * count) # type: ignore
        
        return res
    

    res = '1'
    for _ in range(n - 1):
        res = say(count(res))
    
    return res


def countAndSayIterative(n: int) -> str:
    # Covering the base cases
    if n == 1:
        return '1'
    
    if n == 2:
        return '11'
    
    res = '11'

    for i in range(3, n + 1):
        temp = ''
        res += '#'
        c = 1

        for j in range(1, len(res)):
            if res[j] == res[j - 1]:
                c += 1
                continue
            temp +=  str(c) + res[j]
            c = 1
        
        res = temp
    
    return res

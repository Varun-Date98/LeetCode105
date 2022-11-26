from typing import List

'''
14. Longest Common Prefix | Easy
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
----------------------------------------------------------------------------------------
There are many ways to solve this problem, one can scan through each string horizontally or
vertically. We can also use Trie data structure to accomplish this, if the question is ask 
such that new strings will be added and inbetween we need to find LCP then Trie apprach is best
'''


def lcsVerticalScan(words: List[str]) -> str:
    """
    Iterate through the characters of first string in the words list, comparing each index to
    particular character of all other strings
    """
    if len(words) == 0: return ''

    prefix = words[0]

    for i in range(len(prefix)):
        c = prefix[i]

        for j in range(1, len(words)):
            if i >= len(words[j]) or words[j][i] != c:
                return prefix[:i]
    
    return prefix


def lcsHorizontalScan(words: List[str]) -> str:
    if len(words) == 0: return ""

    prefix = words[0]

    for i in range(1, len(words)):
        j = 0

        while j < len(prefix) and j < len(words[i]) and prefix[j] == words[i][j]:
            j += 1
        
        if j == 0:
            return ""
        
        prefix = prefix[:j]
    
    return prefix

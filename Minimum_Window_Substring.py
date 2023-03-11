from collections import defaultdict


'''
76. Minimum Window Substring | Hard
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s 
such that every character in t (including duplicates) is included in the window. If there is no such
substring, return the empty string "".
----------------------------------------------------------------------------------------------------

'''


def minWindow(s: str, t: str) -> str:
    if len(t) > len(s):
        return ""

    i, left, right = 0, 0, 0    
    needs, missing = defaultdict(int), len(t)

    for c in t:
        needs[c] += 1
    
    for j, c in enumerate(s, 1):
        missing -= needs[c] > 0
        needs[c] -= 1

        if not missing:
            while i < j and needs[s[i]] < 0:
                needs[s[i]] += 1
                i += 1
            
            if not right or j - i < right - left:
                right, left = i, j
    
    return s[left:right]

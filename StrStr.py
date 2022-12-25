'''
28. Find the Index of the First Occurrence in a String | Medium
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack
or -1 if needle is not part of haystack.
-----------------------------------------------------------------------------------------------------

'''


def strStr(haystack: str, needle: str) -> int:
    i = 0

    if needle == '':
        return 0
    
    while i < len(haystack) - len(needle) + 1:
        j = 0

        while j < len(needle):
            if haystack[i + j] != needle[j]:
                break

            j += 1
        
        if j == len(needle):
            return i
        
        i += 1
    
    return -1


def strStrKMP(haystack: str, needle: str) -> int:
    if needle == '':
        return 0
    
    i, previousLPS = 1, 0
    lps = [0] * (len(needle))

    while i < len(needle):
        if needle[i] == needle[previousLPS]:
            lps[i] = previousLPS + 1
            previousLPS += 1
            i += 1
        elif previousLPS == 0:
            lps[i] = 0
            i += 1
        else:
            previousLPS = lps[previousLPS - 1]
    
    i, j = 0, 0

    while i < len(haystack):
        if haystack[i] == needle[j]:
            i += 1
            j += 1
        else:
            if j == 0:
                i += 1
            else:
                j = lps[j - 1]
        
        if j == len(needle):
            return i - j
    
    return -1

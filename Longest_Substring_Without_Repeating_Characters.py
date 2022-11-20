'''
3. Longest Substring Without Repeating Characters | Medium

Given a string s, find the length of the longest substring without repeating characters.

----------------------------------------------------------------------------------------

Use sliding window algorithm, with left and right pointers and a set to keep
track of unique characters.

In the optimized approach instead of going through all characters between left and
the repeated characte, we directly skip to the position of repeated character + 1
'''

def slidingWindow(s: str) -> int:
    res = 0
    chars = set()
    left, right = 0, 0

    while right < len(s):
        while s[right] in chars:
            chars.remove(s[left])
            left += 1
        
        chars.add(s[right])
        res = max(res, right - left + 1)
        right += 1
    
    return res

def optimised(s: str) -> int:
    res = 0
    dp = {}
    currentStart = 0

    for i, c in enumerate(s):
        if c in dp and dp[c] >= currentStart:
            currentStart = dp[c] + 1
        
        dp[c] = i
        res = max(res, i - currentStart + 1)
    
    return res
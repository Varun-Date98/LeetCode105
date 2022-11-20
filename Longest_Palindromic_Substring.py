'''
5. Longest Palindromic Substring | Medium
Given a string s, return the longest palindromic substring in s.

------------------------------------------------------------------------------------------------------

Can be solved in many ways longest common substring between s and reverse s that is a palindrome
Can be solved with DP as well where dp[i][j] = True if s[i:j] is palindrome then
    dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
Most efficient way would be to use expanding around the center approach where we try and find
the longest palindrome with center at current index
'''

def longestPalindrome(s: str) -> str:
    res = ''

    def palindromeCenteredAtIdx(l: int, r: int) -> str:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        
        return s[l+1:r]
    
    for i in range(len(s)):
        odd = palindromeCenteredAtIdx(i, i)
        even = palindromeCenteredAtIdx(i, i + 1)
        res = max(res, odd, even, key=len)
    
    return res

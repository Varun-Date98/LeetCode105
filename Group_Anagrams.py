import collections
from typing import List


'''
49. Group Anagrams | Medium
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
----------------------------------------------------------------------------------------------------
Sort the word and use that as keys in dict to keep track of the anagrams.
'''


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    res = collections.defaultdict(list)

    for word in strs:
        res[''.join(sorted(word))].append(word)
    
    return list(res.values())

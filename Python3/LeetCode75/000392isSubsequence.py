# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false
 

# Constraints:

# 0 <= s.length <= 100
# 0 <= t.length <= 104
# s and t consist only of lowercase English letters.

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        slist = list(s)
        tlist = list(t)
        substr = True
        i=0
        pos = [-1]
        post = 0
        if (len(slist) == len(tlist) and s != t):
            substr = False
        while (i<len(slist) and substr == True):
            if slist[i] not in tlist:
                substr = False
            else:
                post = tlist.index(slist[i])
                if post in pos:
                    indici = [j for j, char in enumerate(t) if char == slist[i]]
                    indici.remove(post)
                    if len(indici)>0:
                        post = min(indici)
                    else:
                        substr = False
                    if post == 0:
                        substr = False
                    else:
                        pos.append(post)
                else:
                    pos.append(post)
                    if (post < max(pos)):
                        substr = False
            i+=1
        return substr
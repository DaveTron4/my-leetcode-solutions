class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(t)
        m = len(s)
        i, k = 0, 0

        while k < n and i < m:
            if s[i] == t[k]:
                i += 1
            k += 1
        
        return i == m
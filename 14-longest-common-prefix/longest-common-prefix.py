class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min(len(s) for s in strs)
        prefix = ""

        for i in range(min_len):
            chars = set(s[i] for s in strs)
            if len(chars) == 1:
                prefix += chars.pop()
            else:
                break
        return prefix
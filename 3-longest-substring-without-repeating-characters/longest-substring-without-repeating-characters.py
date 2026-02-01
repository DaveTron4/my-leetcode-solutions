class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}

        left = result = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.pop(s[left])
                left += 1
            seen[s[right]] = right
            result = max(right - left + 1, result)

        return result
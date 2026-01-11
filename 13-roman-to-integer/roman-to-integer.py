class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {   "I" : 1, 
                "V" : 5, 
                "X" : 10, 
                "L" : 50,
                "C" : 100,
                "D" : 500,
                "M" : 1000
            }
        total = 0
        for r in range(len(s)):
            if r + 1 < len(s) and roman[s[r]] < roman[s[r + 1]]:
                total -= roman[s[r]]
            else:
                total += roman[s[r]]
        return total
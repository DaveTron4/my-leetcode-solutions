from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineHash = Counter(magazine)
        ransomHash = Counter(ransomNote)

        for char, freq in ransomHash.items():
            if char in magazineHash and freq <= magazineHash[char]:
                continue
            else:
                return False

        return True
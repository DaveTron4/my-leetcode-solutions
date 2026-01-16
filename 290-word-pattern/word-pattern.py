class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        patternList = s.split()

        if len(pattern) != len(patternList):
            return False

        return len(set(zip(patternList, pattern))) == len(set(patternList)) == len(set(pattern))


        
                

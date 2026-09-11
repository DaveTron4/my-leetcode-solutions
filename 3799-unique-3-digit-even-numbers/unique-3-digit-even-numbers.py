class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        result = set()

        for i, j, k in permutations(digits, 3):
            if i != 0 and k % 2 == 0:
                result.add((i, j, k))
            
        return len(result)
        
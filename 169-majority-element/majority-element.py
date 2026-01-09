from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(i for i in nums)

        return max(counter, key=counter.get)
        
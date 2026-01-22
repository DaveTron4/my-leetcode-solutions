class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        result = 0

        for i in nums:
            result = result ^ i

        return result
        
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_to_i = {}
        for i in range(len(nums)):
            if nums[i] in num_to_i:
                if abs(num_to_i[nums[i]] - i) <= k:
                    return True
            num_to_i[nums[i]] = i

        return False
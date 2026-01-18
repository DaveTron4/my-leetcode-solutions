class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums)  == 0:
            return nums

        if len(nums) == 1:
            return [f"{nums[0]}"]


        result = []

        i, j = 0, 1
        
        for k in range(len(nums) - 1):
            if nums[j] == nums[k] + 1:
                j += 1
            else:
                if i == k:
                    result.append(f"{nums[i]}")
                    i = j
                    j += 1
                else:
                    result.append(f"{nums[i]}->{nums[k]}")
                    i = j
                    j += 1

        if i == j-1:
            result.append(f"{nums[i]}")
        else:
            result.append(f"{nums[i]}->{nums[j-1]}")

        return result
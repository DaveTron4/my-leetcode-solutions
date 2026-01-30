class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        maxAmount = 0

        left, right = 0, len(height) - 1

        while left <= right:
            h = min(height[left], height[right])
            w = right - left
            area = w * h

            if area > maxAmount:
                maxAmount = area

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxAmount


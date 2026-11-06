class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_water = 0

        left = 0
        right = len(height) - 1

        while left < right:

            width = right - left
            water = width * min(height[left],height[right])

            max_water = max(max_water,water)

            if height[left] < height[right]:
                left += 1

            else: # even when both walls are of same height
                right -= 1

        return max_water


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        left = []
        right = []

        left_max = 0
        right_max = 0

        for l in height:
            left_max = max(left_max,l)
            left.append(left_max)

        for r in height[::-1]:
            right_max = max(right_max,r)
            right.append(right_max)

        right = right[::-1]

        water = 0

        for i in range(n):
            water += min(left[i],right[i]) - height[i]

        return water






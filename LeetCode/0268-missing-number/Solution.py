class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)

        for i in range(n + 1):
            if i not in nums:
                return i 

        
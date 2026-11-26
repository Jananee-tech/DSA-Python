class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        t_s = sum(nums)
        l_s = 0

        for i in range(len(nums)):
            r_s = t_s - l_s - nums[i]
            if r_s == l_s:
                return i
            l_s += nums[i]

        return -1
        
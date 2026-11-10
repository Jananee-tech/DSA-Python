class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        total_sum = 0
        left = 0
        minimum = len(nums) + 1

        for right in range(len(nums)):
            total_sum += nums[right]

            while total_sum >= target:
                window_length = right - left + 1
                minimum = min(minimum , window_length)

                total_sum = total_sum - nums[left]
                left += 1

        if minimum == len(nums) + 1:
                return 0

        return minimum

            
        
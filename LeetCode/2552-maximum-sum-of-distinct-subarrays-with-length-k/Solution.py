class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        window = set()
        cur_sum = 0
        max_sum = 0
        left = 0

        for right in range(len(nums)):

            while nums[right] in window:
                window.remove(nums[left])
                cur_sum -= nums[left]
                left += 1

            window.add(nums[right])
            cur_sum += nums[right]

            if right - left + 1 > k:
                window.remove(nums[left])
                cur_sum -= nums[left]
                left += 1

            if right - left + 1 == k:
                max_sum = max(max_sum,cur_sum)

        return max_sum

        
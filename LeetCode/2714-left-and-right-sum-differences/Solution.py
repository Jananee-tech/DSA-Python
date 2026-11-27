class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_sum = 0
        total_sum = sum(nums)
        answer = []

        for i in range(len(nums)):
            right_sum = total_sum - left_sum - nums[i]

            diff = abs(left_sum - right_sum)

            answer.append(diff)

            left_sum += nums[i]

        return answer

        
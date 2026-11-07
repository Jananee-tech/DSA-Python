class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        hash_map = {}

        for i in range(len(nums)):
            num = nums[i]

            if num in hash_map:
                prevIndex = hash_map[num]

                if abs(i - prevIndex) <= k:
                    return True

            hash_map[num] = i

        return False


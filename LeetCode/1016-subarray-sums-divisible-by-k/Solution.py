class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        prefix_sum = 0
        count = 0
        hash_map = {0:1}

        for num in nums:
            prefix_sum += num

            remainder = prefix_sum % k

            if remainder in hash_map:
                count += hash_map[remainder]

            hash_map[remainder] = hash_map.get(remainder,0) + 1

        return count 

        
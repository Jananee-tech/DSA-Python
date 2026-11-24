class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        maximum = 0

        for num in num_set:
            prev = num - 1

            if prev not in num_set:
                start = num
                res = []
                length = 1
                next_el = num + 1
                
                while next_el in num_set:
                    length += 1
                    next_el = next_el + 1

                maximum = max(length,maximum)


        return maximum 



        
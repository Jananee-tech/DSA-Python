class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0

        for right in range(len(s)):
            substring = s[right:right + 3]

            if len(set(substring)) == 3:
                count += 1


        return count 
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sort = sorted(s1)
        n = len(s1)

        for right in range(len(s2) - n + 1):
            substring = s2[right : right + n]

            if sorted(substring) == sort:
                return True

        return False
        
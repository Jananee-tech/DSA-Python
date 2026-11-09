class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        res = []
        cur = []
        sorted_p = sorted(p)

        for right in range(0, len(s) - len(p) + 1):
            cur = s[right : right + len(p)]

            if sorted(cur) == sorted_p:
                res.append(right)

        return res
        
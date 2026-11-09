class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        freq_p ={}
        freq_s = {}

        for i in range(len(p)):
            freq_p[p[i]] = freq_p.get(p[i],0) + 1

        res = []
        k = len(p)
        left = 0

        for right in range(len(s)):
            freq_s[s[right]] = freq_s.get(s[right] , 0) + 1

            if right - left + 1 > k:
                freq_s[s[left]] -= 1
                
                if freq_s[s[left]] == 0:
                    del freq_s[s[left]]

                left += 1

            if freq_s == freq_p:
                res.append(left)

        return res




        
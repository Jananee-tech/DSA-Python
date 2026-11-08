class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}

        for ch in t:
            need[ch] = need.get(ch,0) + 1

        window = {}
        formed = 0
        required = len(need)
        
        left = 0
        min_length = float('inf')
        start = 0

        for right in range(len(s)):
            ch = s[right]
            window[ch] = window.get(ch,0) + 1

            if ch in need and window[ch] == need[ch]:
                formed += 1

            while formed == required:
                window_length = right - left + 1 

                if window_length < min_length:
                    min_length = window_length
                    start = left

                left_ch = s[left]

                if left_ch in need and window[left_ch] == need[left_ch]:
                    formed -= 1

                window[left_ch] -= 1
                left += 1

        if min_length == float("inf"):
            return ""

        return s[start : start + min_length]

                






        
class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        count = 0

        cur = sum(arr[:k])
        avg = cur / k

        if avg >= threshold:
            count += 1

        for i in range(k,len(arr)):
            cur = cur + arr[i] - arr[i - k]
            avg = cur / k

            if avg >= threshold:
                count += 1

        return count
        
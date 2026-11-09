class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])
        total_length = word_len * len(words)

        required = {}

        for w in words:
            required[w] = required.get(w,0) + 1

        res = []

        for i in range(len(s) - total_length + 1):

            substring = s[i:i+total_length]

            current = {}

            for j in range(0,total_length,word_len):

                chunk = substring[j:j+word_len]

                if chunk not in required:
                    break

                current[chunk] = current.get(chunk,0) + 1

            if current == required:
                res.append(i)

        return res

        
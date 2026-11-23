class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups= {} #hashmap
 
        for word in strs:
            key = " ".join(sorted(word))

            groups.setdefault(key,[])

            groups[key].append(word)

        return list(groups.values())
        
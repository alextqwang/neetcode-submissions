class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char) - 97] += 1
            frozen = tuple(count)
            if frozen in d:
                d[frozen].append(string)
            else:
                d[frozen] = [string]

        return list(d.values())
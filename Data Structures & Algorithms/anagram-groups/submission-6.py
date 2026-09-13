class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for string in strs:
            ds = {}
            for char in string:
                if char in ds:
                    ds[char] += 1
                else:
                    ds[char] = 1
            frozen = frozenset(ds.items())
            if frozen in d:
                d[frozen].append(string)
            else:
                d[frozen] = [string]

        return list(d.values())
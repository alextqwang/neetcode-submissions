class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            counts = [0] * 26
            for c in s:
                counts[ord(c) - ord('a')] += 1
            key = tuple(counts)
            if key in d:
                d[key].append(s)
            else:
                d[key] = [s]
        return list(d.values())
        

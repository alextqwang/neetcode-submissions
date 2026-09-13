class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            anagram = ''.join(sorted(s))
            if anagram in d:
                d[anagram].append(s)
            else:
                d[anagram] = [s]
            
        return list(d.values())
        

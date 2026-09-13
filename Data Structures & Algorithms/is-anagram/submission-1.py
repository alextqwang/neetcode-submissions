class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d1 = {}
        for c in s:
            if c in d1:
                d1[c] += 1
            else:
                d1[c] = 1
        d2 = {}
        for char in t:
            if char in d2:
                d2[char] += 1
            else:
                d2[char] = 1
        return d1 == d2
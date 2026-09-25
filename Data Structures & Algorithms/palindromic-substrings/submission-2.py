class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) == 1:
            return 1
        palindromes = 0
        for i in range(len(s)):
            palindromes += 1
            p0, p1 = i, i
            valid = True
            while valid and p0 > 0 and p1 < len(s) - 1:
                if s[p0 - 1] == s[p1 + 1]:
                    p0 -= 1
                    p1 += 1
                    palindromes += 1
                else:
                    valid = False

        for j in range(len(s) - 1):
            p0, p1 = j, j + 1
            valid = False
            if s[p0] == s[p1]:
                valid = True
                palindromes += 1
            while valid and p0 > 0 and p1 < len(s) - 1:
                if s[p0 - 1] == s[p1 + 1]:
                    p0 -= 1
                    p1 += 1
                    palindromes += 1
                else:
                    valid = False

        return palindromes
                
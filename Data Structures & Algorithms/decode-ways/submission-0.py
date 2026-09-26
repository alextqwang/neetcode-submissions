class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        f0 = 1
        curr = int(s[0:2])
        zero = False
        if s[1] == '0':
            if int(s[0]) > 2:
                return 0
            else:
                f1 = 1
                zero = True
        else:
            f1 = 2 if curr <= 26 else 1
        valid = True
        for i in range(1, len(s) - 1):
            temp = f0
            f0 = f1
            if s[i + 1] == '0':
                if zero or int(s[i]) > 2:
                    return 0
                else:
                    f1 = temp
                    zero = True
            else:
                if not zero:
                    curr = int(s[i:i + 2])
                    f1 = temp + f1 if curr <= 26 else f1
                zero = False
        return f1
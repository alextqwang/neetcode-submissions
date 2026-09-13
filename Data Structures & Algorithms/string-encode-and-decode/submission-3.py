class Solution:

    def encode(self, strs: List[str]) -> str:
        # Write all the lengths first, separated by any one character, then have a separate     
        # unique character define the 'start' of the strings. 
        if not strs:
            return ''
        encoded = ''
        lengths = []
        for s in strs:
            lengths.append(len(s))
            encoded += s
        string = ''
        for i in lengths:
            string += (str(i) + 'x')
        string += 'y'
        string += encoded
        return string


    def decode(self, s: str) -> List[str]:
        decoded = []
        if not s:
            return decoded
        stop = False
        i = 0
        while not stop:
            if s[i] == 'y':
                stop = True
            i += 1
        key = s[:(i - 1)]
        encoded = s[i:]
        lengths = []
        integer = ''
        for char in key:
            if char != 'x':
                integer += char
            else:
                lengths.append(int(integer))
                integer = ''
        for j in lengths:
            decoded.append(encoded[:j])
            encoded = encoded[j:]
        return decoded


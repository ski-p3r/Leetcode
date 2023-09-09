class Solution:
    def replaceDigits(self, s: str) -> str:
        r=""
        for i in range(len(s)):
            k=''
            if s[i].isdigit():
                k=chr(ord(s[i-1]) + int(s[i]))
                r+=k
            else:
                r+=s[i]
        return r
            
        
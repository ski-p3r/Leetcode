class Solution:
    def greatestLetter(self, s: str) -> str:
        d = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        sk=[]
        for i in d:
            if i in s and i.lower() in s:
                sk.append(i)
        if len(sk) > 0:
            return max(sk)
        return ""
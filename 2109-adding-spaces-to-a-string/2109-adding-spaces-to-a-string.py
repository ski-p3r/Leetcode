class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        kk = 0
        for i in spaces:
            result.append(s[kk:i])
            kk = i
        result.append(s[kk:])
        return ' '.join(result)

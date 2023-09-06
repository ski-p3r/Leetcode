class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        l=[]
        for i in accounts:
            l.append(sum(i))
        return max(l)
        
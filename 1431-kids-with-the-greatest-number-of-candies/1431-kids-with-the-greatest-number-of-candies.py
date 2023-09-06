class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        l=[]
        for i in candies:
            if extraCandies + i < max(candies):
                l.append(False)
            else:
                l.append(True)
        return l
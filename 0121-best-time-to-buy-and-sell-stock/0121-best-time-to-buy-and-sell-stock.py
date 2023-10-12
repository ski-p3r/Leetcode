class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0,1
        maxVal = 0
        while right <= len(prices)-1:
            if prices[left] > prices[right-1]:
                left = right
                right += 1
            elif prices[right] > prices[left]:
                maxVal = max(prices[right]-prices[left], maxVal)
                right += 1
            else:
                left = right
                right += 1
        return maxVal
        
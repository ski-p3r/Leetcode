class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currSum = maxSum = sum(nums[:k])
        for i in range(k, len(nums)):
            currSum += nums[i] - nums[i - k]
            maxSum = max(maxSum, currSum)
        return maxSum / k
        
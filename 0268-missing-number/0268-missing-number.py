class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(0, max(nums)+2):
            if not i in nums:
                return i
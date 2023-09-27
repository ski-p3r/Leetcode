class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        m=0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] + nums[j] < target and i<j:
                    m+=1
        return m
        
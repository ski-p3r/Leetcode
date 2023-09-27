class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        m=0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[i] == nums[j] and i<j:
                    m+=1
        return m
        
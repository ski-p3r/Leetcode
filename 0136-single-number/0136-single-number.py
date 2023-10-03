class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d=0
        for i in nums:
            if nums.count(i) == 1:
                d=i
                
        return d
        
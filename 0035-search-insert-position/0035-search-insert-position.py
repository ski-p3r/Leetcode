class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        try:
            x=nums.index(target)
            return x
        except:
            g=0
            for i in nums:
                if i < target:
                    g+=1
            return g
        
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        d=[]
        for _ in range(len(nums)):
            d.insert(index[_], nums[_])
            
        return d
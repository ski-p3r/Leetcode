class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        l=[]
        for i in range(0, len(nums), 2):
            for _ in range(nums[i]):
                l.append(nums[i+1])
        return l
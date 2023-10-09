class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        k=[]
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                k.append((nums[i]-1)*(nums[j]-1))
        return max(k)
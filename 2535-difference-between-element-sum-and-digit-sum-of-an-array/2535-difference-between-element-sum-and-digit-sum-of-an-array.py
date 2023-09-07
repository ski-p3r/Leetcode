class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        n=sum(nums)
        j=0
        for i in nums:
            if len(str(i))>1:
                for k in str(i):
                    j+=int(k)
            else:
                j+=i
        return n-j
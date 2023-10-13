class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n=len(nums)
        target=sum(nums)-x
        dp=[0]
        res=0
        for num in nums:
            res+=num
            dp.append(res)
        seen={v:i for i,v in enumerate(dp)}
        ans=-1
        for l_val,l_idx in seen.items():
            if l_val+target in seen:
                ans=max(seen[l_val+target]-l_idx,ans)
        if ans==-1:
            return ans
        else:
            return n-ans  
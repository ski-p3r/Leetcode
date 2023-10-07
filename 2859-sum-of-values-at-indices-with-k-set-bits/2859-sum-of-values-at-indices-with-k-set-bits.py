class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        s=[bin(i)[2:] for i in range(len(nums))]
        l=[]
        for i in s:
            if i.count(str('1')) == k:
                l.append(nums[s.index(i)])
        return sum(l)
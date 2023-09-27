class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        m=[0]
        n=[]
        for i in range(1,len(nums)):
            m.append(sum(nums[:i]))
            n.append(sum(nums[i:]))
        n.append(0)
        k=[]
        for _ in range(len(m)):
            k.append(abs(m[_]-n[_]))
        return k
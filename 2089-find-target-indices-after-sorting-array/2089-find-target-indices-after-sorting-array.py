class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        l=[]
        n=0
        for i in range(nums.count(target)):
            l.append(nums.index(target)+n)
            n+=1
        return l
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        d=int(nums.count(val))
        for i in range(d):
            nums.remove(val)
        return len(nums)
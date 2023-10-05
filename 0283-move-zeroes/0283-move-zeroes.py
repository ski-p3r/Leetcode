class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if nums.count(0) == 0:
            return nums
        for i in range(nums.count(0)):
            nums.remove(0)
            nums.append(0)
        return nums
        
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in nums:
            if nums.count(i) > 1:
                for j in range(nums.count(i)-1):
                    nums.remove(i)
        return len(nums)
            
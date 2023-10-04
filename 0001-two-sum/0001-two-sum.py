class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            try:
                for j in range(1,len(nums)):
                    if i==j:
                        pass
                    else:
                        if target==nums[i]+nums[j]:
                            return ([i,j])
            except:
                None
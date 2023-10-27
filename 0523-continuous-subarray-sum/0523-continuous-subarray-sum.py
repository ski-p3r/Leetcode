class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d , s = {0:-1} , 0
        for i, n in enumerate(nums):
            if k != 0:
                s = (s + n) % k
            else:
                s += n
            if s not in d:
                d[s] = i
            else:
                if i - d[s] >= 2:
                    return True
        return False
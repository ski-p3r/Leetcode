class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x, y):
            return int(str(y) + str(x)) - int(str(x) + str(y))
        
        sorted_numbers = sorted(nums, key=cmp_to_key(compare))
        ans = ''.join(str(i) for i in sorted_numbers)
        return ans if ans[0] != '0' else '0'


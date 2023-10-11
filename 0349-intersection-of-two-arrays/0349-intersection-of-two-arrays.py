class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l=[]
        for i in nums1:
            if (i in nums2) and (not i in l):
                l.append(i)
        return l
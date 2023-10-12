class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        buckets = {} #store values for diapason (i-indexDiff:i]
        valueDiff +=1 #if valueDiff = zero it's simplify proces edge-cases
        
        for idx, curVal in enumerate(nums):
            bucketId = curVal // valueDiff #bucket for new element
            if bucketId in buckets: return True # have 'duplicate value' in current bucket
            #check neighboring buckets if they are exists
            for i in (bucketId - 1, bucketId + 1):
                if i in buckets: # bucket exist
                    if abs(buckets[i] - curVal) < valueDiff: # because valueDiff+1 then check only strict <
                        return True
            
            #add current value to bucket
            buckets[bucketId] = curVal
            
            # remove value out of available window
            if idx >= indexDiff:
                removeVal = nums[idx - indexDiff]
                del buckets[removeVal//valueDiff]

        return False
class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        value_to_index = {num: i for i, num in enumerate(nums)}
        for operation in operations:
            old_value, new_value = operation
            index = value_to_index[old_value]
            nums[index] = new_value
            value_to_index[new_value] = index
            del value_to_index[old_value]

        return nums
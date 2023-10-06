class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if x == 0:
            return 0

        if x > 0:
            reversed_x = int(str(x)[::-1])
        else:
            reversed_x = -int(str(-x)[::-1])

        if reversed_x > INT_MAX or reversed_x < INT_MIN:
            return 0

        return reversed_x
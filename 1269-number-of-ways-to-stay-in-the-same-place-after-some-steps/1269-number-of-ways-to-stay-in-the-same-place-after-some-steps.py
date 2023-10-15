class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        modulo = 1000000007
        max_len = min(arrLen, 1 + steps // 2)
        ways = [0] * (max_len + 1)
        ways[0] = 1
        for i in range(steps):
            left = 0
            for j in range(min(max_len, i + 2, steps - i + 3)):
                left, ways[j] = ways[j], (ways[j] + left + ways[j + 1]) % modulo
        return ways[0]
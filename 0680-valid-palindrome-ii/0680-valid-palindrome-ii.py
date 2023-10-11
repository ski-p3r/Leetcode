class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(substring):
            return substring == substring[::-1]

        p1 = 0
        p2 = len(s) - 1

        while p1 <= p2:
            if s[p1] != s[p2]:
                return is_palindrome(s[p1:p2]) or is_palindrome(s[p1+1:p2+1])
            p1 += 1
            p2 -= 1

        return True

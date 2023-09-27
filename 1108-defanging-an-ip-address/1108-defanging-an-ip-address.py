class Solution:
    def defangIPaddr(self, address: str) -> str:
        s=address.split('.')
        return '[.]'.join(s)
        
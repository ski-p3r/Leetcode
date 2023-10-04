class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        x=num1+'*'+num2
        return str(eval(x))
class Solution:
    def backspaceCompare(self, s, t):
        backspace1=[]
        backspace2=[]
        backspace="#"
        for item in range(len(s)):
            if backspace1 and s[item]==backspace:
                backspace1.pop()
            else:
                if s[item]!=backspace:
                    backspace1.append(s[item])
        for item in range(len(t)):
            if backspace2 and t[item]==backspace:
                backspace2.pop()
            else:
                if t[item]!=backspace:
                    backspace2.append(t[item])
        if backspace1==backspace2:
            return True
        return False
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0;
        
        l = set();
        m = 0;
        i = 0;
        j = 0;
        
        while(i<len(s)):
            if(s[i] not in l):
                l.add(s[i])
                i+=1
            else:
                m = max(m,len(l));
                l.remove(s[j])
                j+=1
                
        m = max(m,len(l));
        return m;
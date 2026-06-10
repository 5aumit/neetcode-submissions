class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if not len(s)==len(t):
            return False
        
        s_chars , t_chars = {},{}

        for i in range(len(s)):

            try:
                s_chars[s[i]]+=1
            except:
                s_chars[s[i]]=0

            try:
                t_chars[t[i]]+=1
            except:
                t_chars[t[i]]=0

            
        return s_chars==t_chars
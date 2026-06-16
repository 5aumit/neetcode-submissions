class Solution:
    def isValid(self, s: str) -> bool:

        if len(s)<2:
            return False
        
        brackets = {
            '}':'{', ']':'[', ')':'('
        }

        st = []

        for b in s:
            
            # if not a closing bracket, append it
            if b not in brackets:
                st.append(b)

            else:  #If closing bracket
                if len(st)>0 and brackets[b] == st[-1]: #If stack is not empty, and correct bracket
                    st.pop()
                else:
                    return False
            
        return len(st)==0

            
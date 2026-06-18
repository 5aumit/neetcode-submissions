class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = []

        for i,t in enumerate(temperatures):
            j=i+1
            found = False
            while j<len(temperatures):
                if temperatures[j]>t:
                    out.append(j-i)
                    found = True
                    break
                j+=1
            if not found:
                out.append(0)

        return out
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l,r = 1,max(piles)
        
        mink=r
        c = 0

        while l<r:

            k = (l+r)//2
            t = self.findTime(piles,k)

            if t>h: 
                l=k+1

            elif t<=h:
                r=k
                mink = min(k,mink)            

        return mink


    def findTime(self,piles,k):
        
        t = 0

        for pile in piles:
            t += pile//k + (1 if pile%k>0 else 0)
        
        return t

    
        
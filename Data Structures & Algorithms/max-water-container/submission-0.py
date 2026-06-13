class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l,r = 0, len(heights)-1
        areamax = 0

        while l<r:
            a = min(heights[l],heights[r])*(r-l)

            if a>=areamax:
                areamax=a
            
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        
        return areamax
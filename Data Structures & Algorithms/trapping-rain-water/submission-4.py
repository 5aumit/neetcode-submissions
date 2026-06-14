class Solution:
    def trap(self, height: List[int]) -> int:

        maxheight = 0
        for i in range(len(height)):
            if height[i] >= height[maxheight]:
                maxheight = i
        
        return self.maxarea(height[:maxheight+1]) + self.maxarea(height[::-1][:len(height)-maxheight])

    def findarea(self,height: List[int]) -> int:
        a = min(height[0],height[-1])*(len(height)-2) - sum(height[1:-1])
        return a

    def maxarea(self,height):

        l,r = 0,1

        amax = 0

        while (r<len(height)) and (l<r):

            if height[r] < height[l]:
                open = True
                r+=1

            elif height[r] >= height[l]:
                open = False

            if not open:
                
                amax += self.findarea(height[l:r+1])
                print(l,r,height[l:r+1],self.findarea(height[l:r+1]))
                l=r
                r+=1

        return amax

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        areas = [0]*len(heights)

        for i,h1 in enumerate(heights):
            
            j=i+1
            k=i-1
            counts=0

            while j<len(heights) and heights[j]>=h1:
                counts+=1
                j+=1

            while k>-1 and heights[k]>=h1:
                counts+=1
                k-=1

            areas[i] = h1*(counts+1)

        return max(areas)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        hstack = []
        lstack = []

        maxArea=0

        for i,height in enumerate(heights):
            popped = False

            while hstack and hstack[-1]>height:

                leftheight = hstack.pop()
                left = lstack.pop()
                area = leftheight*(i-left)
                
                popped = True

                if area>=maxArea:
                    maxArea=area

            if popped:
                lstack.append(left)
            else:
                lstack.append(i)

            hstack.append(height)

        for i,v in enumerate(hstack):
            area = v*(len(heights)-lstack[i])
            if area>=maxArea:
                maxArea=area

        return maxArea


                



            
            
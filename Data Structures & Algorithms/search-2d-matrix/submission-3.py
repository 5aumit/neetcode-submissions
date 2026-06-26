class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m , n = len(matrix)-1, len(matrix[0])-1
        
        lrow,rrow = 0, m

        while lrow<=rrow:

            if target>=matrix[lrow][0] and target<=matrix[lrow][n]:
                return self.searchRow(matrix[lrow],target)

            elif target>=matrix[rrow][0] and target<=matrix[rrow][n]:
                return self.searchRow(matrix[rrow],target)
            
            if target>matrix[lrow][n]:
                lrow+=1
            elif target<matrix[rrow][0]:
                rrow-=1

 
        return False

        
    def searchRow(self,row,target):

        l,r = 0,len(row)-1

        while l<=r:

            mid = (l+r)//2

            if target > row[mid]:
                l=mid+1
            elif target < row[mid]:
                r=mid-1
            elif target==row[mid]:
                return True

        return False

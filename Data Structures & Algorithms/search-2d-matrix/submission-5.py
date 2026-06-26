class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m , n = len(matrix)-1, len(matrix[0])-1
        
        lrow,rrow = 0, m

        while lrow<=rrow:

            midRow = (lrow+rrow)//2

            if target>matrix[midRow][n]:
                lrow=midRow+1
            elif target<matrix[midRow][0]:
                rrow=midRow-1
            else:
                return self.searchRow(matrix[midRow],target)

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
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # make sure matrix exists !
        m=len(matrix) #len of col
        n=len(matrix[0]) #len of row
        l=0
        r=m*n-1
        
        while (r>=l):
            i=(r+l)//2
            row= i//n
            col=i%n
            if matrix[row][col]> target:
                r=i-1
            elif matrix[row][col]< target:
                l=i+1
            else:
                return True
        return False

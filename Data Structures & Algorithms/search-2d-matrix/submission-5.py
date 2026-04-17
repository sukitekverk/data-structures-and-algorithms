class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols= len(matrix[0])

        i = 0
        j = rows*cols-1

        while i <=j:
            mid = i+(j-i)//2
            r = mid//cols
            c= mid %cols

            if matrix[r][c]== target:
                return True
            elif  matrix[r][c]<target:
                i= mid+1
            else:
                j= mid-1
        return False
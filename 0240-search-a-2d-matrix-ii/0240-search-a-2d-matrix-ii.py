class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        row=len(matrix)
        cols=len(matrix[0])
        r=0
        c=cols-1
        while r<row and c>=0:
            if target==matrix[r][c]:
                return True
            elif target<matrix[r][c]:
                c-=1
            else:
                r+=1
        return False
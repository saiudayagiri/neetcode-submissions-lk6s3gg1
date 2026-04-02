class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t=0
        b=len(matrix)-1
        l=0
        r=len(matrix[0])-1
        while t<=b:
            m=(t+b) //2
            if target>matrix[m][-1]:
                t=m+1
            elif target<matrix[m][0]:
                b=m-1
            else:
                break
        if t > b:
            return False

        row = (t + b) // 2        

        while l<=r:
            m=(l+r) //2
            if matrix[row][m]==target:
                return True
            elif target >matrix[row][m]:
                l=m+1
            else:
                r=m-1
        return False                

        
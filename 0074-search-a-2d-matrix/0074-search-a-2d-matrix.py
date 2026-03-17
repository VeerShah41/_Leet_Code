
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = len(matrix)
        col = len(matrix[0])
        left = 0
        right = row*col-1
        while left<=right:
            mid = (left+right)//2
            r = mid // col
            c = mid % col
            if matrix[r][c]==target:
                return True
            elif matrix[r][c]<target:
                left = mid+1
            else:
                right = mid-1
        return False

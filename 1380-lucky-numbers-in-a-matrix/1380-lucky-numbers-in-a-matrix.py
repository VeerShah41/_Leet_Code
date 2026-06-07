class Solution(object):
    def luckyNumbers(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        for i in range(len(matrix)):
            mi = matrix[i].index(min(matrix[i]))
            ma = float("-inf")
            for j in range(len(matrix)):
                if ma<matrix[j][mi]:
                    ma = matrix[j][mi]
            if matrix[i][mi]==ma:
                return [ma]
        
        return []


        
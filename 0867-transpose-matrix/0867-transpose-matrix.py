import numpy as np
class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        matrix = np.array(matrix)
        trans = matrix.T
        return trans.tolist()
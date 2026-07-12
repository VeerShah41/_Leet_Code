class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        temp = sorted(set(arr))
        d = {v:i+1 for i,v in enumerate(temp)}
        res = [d[x] for x in arr]
        return res
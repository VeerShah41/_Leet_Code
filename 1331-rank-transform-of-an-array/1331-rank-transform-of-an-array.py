class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        d = {v:i+1 for i,v in enumerate(sorted(set(arr)))}
        return [d[x] for x in arr]
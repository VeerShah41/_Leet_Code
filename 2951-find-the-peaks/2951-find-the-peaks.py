class Solution(object):
    def findPeaks(self, mountain):
        """
        :type mountain: List[int]
        :rtype: List[int]
        """
        ans =[]
        for i in range(2,len(mountain)):
            if mountain[i-2] < mountain[i-1] >mountain[i]:
                ans.append(i-1)
        return ans
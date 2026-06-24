class Solution(object):
    def findLonely(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = {}

        for n in nums:
            d[n] = d.get(n, 0) + 1

        ans = []
        for i in d:
            if (d[i]==1 and i+1 not in d and i-1 not in d):
                ans .append(i)
        return ans                 
                 
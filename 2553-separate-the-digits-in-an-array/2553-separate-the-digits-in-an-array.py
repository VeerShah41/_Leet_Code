class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = []
        for i in nums :
            for j in str(i):
                l.append(int(j))
        return l
        
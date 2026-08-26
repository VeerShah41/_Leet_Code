class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=sorted(set(nums))
        if 3>len(l):
            return l[-1]
        return l[-3]
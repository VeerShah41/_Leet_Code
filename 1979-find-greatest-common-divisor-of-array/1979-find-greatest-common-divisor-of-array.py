from math import gcd
class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mi,ma = nums[0],nums[0]
        for i in nums:
            if i>ma:
                ma=i
            elif i<mi:
                mi=i
        
        return gcd(mi,ma)
        
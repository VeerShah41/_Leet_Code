class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            ans = 0
            x = nums[i]
            while x:
                ans+=x%10
                x//=10
            if ans == i:
                return i
            
        return -1
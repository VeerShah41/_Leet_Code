class Solution(object):
    def alternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = nums[0]
        for i in range(1,len(nums),2):
            s-=nums[i]
        for i in range(2,len(nums),2):
            s+=nums[i]
        return s
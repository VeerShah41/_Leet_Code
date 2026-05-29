class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = [0]*len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j and nums[i]>nums[j]:

                    l[i]+=1
        return l
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lis = [-1,-1]
        for i in range(len(nums)):
            
            if nums[i]==target:
                lis[0]=i
                j=i+1
                while len(nums)>j and nums[j]==target:
                    j+=1
                lis[1]=j-1
                break
        return lis

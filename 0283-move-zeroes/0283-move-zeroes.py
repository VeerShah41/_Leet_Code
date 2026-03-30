from collections import deque
class Solution(object):
    def moveZeroes(self, nums):
        """

        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l,r=0,1
        while r<len(nums):
            if nums[l]==0:
                if nums[r]==0:
                    r+=1
                
                elif r<len(nums):

                    nums[l],nums[r]=nums[r],nums[l]
                    l+=1
                    r+=1
            else:
                l+=1
                r+=1
        return nums
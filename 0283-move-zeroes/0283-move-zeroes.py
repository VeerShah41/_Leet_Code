from collections import deque
class Solution(object):
    def moveZeroes(self, nums):
        """

        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        d=deque()
        zero=0
        for i in nums:
            if i!=0:
                d.append(i)
            else:
                zero+=1
        d.extend([0] * zero)
        for j in range(len(nums)):
            nums[j]=d[j]

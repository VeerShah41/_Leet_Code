class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = [0]*len(nums)
        s=0
        for i in range(len(nums)-1):
            s+=nums[i]
            l[i+1]=s
        t=0
        for j in range(len(nums)-1,0,-1):
            t+=nums[j]
            l[j-1]=abs(l[j-1]-t)
        return l 
        


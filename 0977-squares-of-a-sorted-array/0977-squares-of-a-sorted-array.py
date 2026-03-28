class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l,r=0,len(nums)-1
        
        lis=[0]*len(nums)
        i=1
        while l<=r and i<=len(nums)+1:
            if abs(nums[l])>abs(nums[r]):

                lis[-1*i]=nums[l]**2
                i+=1
                
                l+=1
                
            elif abs(nums[l])<=abs(nums[r]):
                lis[-1*i]=nums[r]**2
                i+=1
                
                r-=1
            
        return lis
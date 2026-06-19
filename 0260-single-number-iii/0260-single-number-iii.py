class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        ans = []
        i=0
        
        while i<len(nums):
            if i==len(nums)-1 or nums[i]!=nums[i+1]:
                ans.append(nums[i])
                i+=1
                
            
            else:
       
                i+=2
                
        return ans

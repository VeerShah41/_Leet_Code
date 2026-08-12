class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                a,b = str(nums[i]),str(nums[j])

                if a+b < b+a:
                    nums[i],nums[j] = nums[j],nums[i]
            
        x = "".join(map(str,nums))
        if int(x)==0:
            return "0"
        return x
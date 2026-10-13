class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums.sort(key = abs)
        l,r = 0,n-1
        ans = 0
        while l<r:
            ans+=((nums[r]**2)-(nums[l]**2))
            l+=1
            r-=1
        if n%2!=0:
            ans+=(nums[r])**2
        return ans
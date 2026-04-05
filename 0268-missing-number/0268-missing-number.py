class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        n=len(nums)
        while i<n:
            pos = nums[i]
            if nums[i]<n and nums[i]!=nums[pos]:
                nums[i],nums[pos]=nums[pos],nums[i]
            else:
                i+=1
        j = 0
        while j < n:
            if nums[j]!=j:
                return j
            j+=1

        return j
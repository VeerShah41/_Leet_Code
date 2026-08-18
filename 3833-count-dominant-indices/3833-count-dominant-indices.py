
class Solution(object):
    def dominantIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)-1
        ans = 0
        for i in range(n):

            avg = (sum(nums[i+1:])/n)
            if nums[i] > avg:
                ans+=1
            n-=1
        return ans

            
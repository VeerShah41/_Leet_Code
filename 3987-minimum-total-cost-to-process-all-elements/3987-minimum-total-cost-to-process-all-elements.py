class Solution(object):
    def minimumCost(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        s = sum(nums)
        if s%k==0:
            l = s//k - 1
        else:
            l = s//k
        if s==k:
            return 0

        return (l*(l+1)//2)%((10**9)+7)

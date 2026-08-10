class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        f = {}
        n = len(nums)//3
        for i in nums:
            if i in f:
                f[i]+=1
            else:
                f[i]=1
        ans = []
        for i,j in f.items():
            if j>n:
                ans.append(i)
        return ans
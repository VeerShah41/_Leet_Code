class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        ans = 0
        for i,j in d.items():
            if j==1:
                ans+=i
        return ans

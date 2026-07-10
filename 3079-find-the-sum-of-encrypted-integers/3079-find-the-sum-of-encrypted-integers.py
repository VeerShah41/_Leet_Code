class Solution(object):
    def sumOfEncryptedInt(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        ans = 0
        for i in nums:
            ans+= int(max(str(i))*len(str(i)))
        return ans

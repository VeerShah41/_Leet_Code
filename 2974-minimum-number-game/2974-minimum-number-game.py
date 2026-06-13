class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        arr = sorted(nums)
        for i in range(0,len(nums),2):
            arr[i],arr[i+1]=arr[i+1],arr[i]
        return arr
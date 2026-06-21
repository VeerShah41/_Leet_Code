class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = 0
        for n in nums:
            s = str(n)
            if(len(s)%2 ==0):
                c+=1
        return c 
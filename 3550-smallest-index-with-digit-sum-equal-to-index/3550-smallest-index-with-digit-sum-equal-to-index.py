class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i]<10:
                if i==nums[i]:
                    return i
            else:
                n = str(nums[i])
                s = 0
                for j in n:
                    s+=int(j)
                if s==i:
                    return s
            
        return -1
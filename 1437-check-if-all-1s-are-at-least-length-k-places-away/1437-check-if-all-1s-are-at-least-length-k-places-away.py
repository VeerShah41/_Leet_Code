class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        i = 0
        place = 0
        while i < len(nums):
            
            if nums[i]==1:

                if nums[place]==1 and i!=place and i - place <= k:
                    return False
                place = i
            i+=1
            
        return True

                
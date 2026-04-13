class Solution(object):
    def transformArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        place = 0
        for i in range(len(nums)):
            val = nums[i]
            if val%2==0:
                if i==place:
                    nums[i]=0
                    place+=1
                else:
                    nums[place],nums[i]=0,nums[place]
                    place+=1
            else:
                nums[i] = 1
        return nums
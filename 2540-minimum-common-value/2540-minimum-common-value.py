class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        
        hashmap={}

        for i in nums1:
            hashmap[i]=1
        
        for i in nums2:
            if i in hashmap:
                return i
        return -1
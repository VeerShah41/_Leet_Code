class Solution(object):
    def minNumber(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        common = set(nums1) & set(nums2)

        if common:
            return min(common)

        a = min(nums1)
        b = min(nums2)

        return min(a * 10 + b, b * 10 + a)

        
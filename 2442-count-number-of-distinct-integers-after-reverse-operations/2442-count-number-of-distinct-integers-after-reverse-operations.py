class Solution(object):
    def countDistinctIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set()

        for n in nums:
            s.add(n)
            s.add(int(str(n)[::-1]))

        return len(s)
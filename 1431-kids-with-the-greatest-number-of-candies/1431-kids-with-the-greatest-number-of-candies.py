class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        cand = max(candies)
        l=[True]*len(candies)
        for i in range(len(candies)):
            if (candies[i]+extraCandies)<cand:
                l[i]=False
        return l

                
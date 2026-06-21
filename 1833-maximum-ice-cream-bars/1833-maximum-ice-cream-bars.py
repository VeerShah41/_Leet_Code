class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        c=0
        costs.sort()
        for i in costs:
            if coins>=i:
                coins-=i
                c+=1
        return c

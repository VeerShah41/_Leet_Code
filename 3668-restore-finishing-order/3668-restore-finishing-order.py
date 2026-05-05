class Solution(object):
    def recoverOrder(self, order, friends):
        """
        :type order: List[int]
        :type friends: List[int]
        :rtype: List[int]
        """
        fset = set(friends)
        l = [ ]
        for i in range(len(order)):
            if order[i] in fset :
                l.append(order[i])
        return l
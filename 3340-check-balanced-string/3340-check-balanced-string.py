class Solution(object):
    def isBalanced(self, num):
        """
        :type num: str
        :rtype: bool
        """
        o=0
        e=0
        flag =False
        for i in num:
            if flag:
                o+=int(i)
            else:
                e+=int(i)
            flag = not flag
        return e==o


        
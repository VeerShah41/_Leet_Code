class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        c=0
        for i in words:
            flag = True
            for j in i:
                if j not in allowed:
                    flag = False
            if flag:
                c+=1

            flag=True
        return c        
        
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l=[]
        op=["(","{","["]
        for i in s:
            if i in op:
                l.append(i)
            else:
                if l:
                    x=l.pop()
                    if x=="(" and i!=")":
                        return False
                    if x=="[" and i!="]":
                        return False
                    if x=="{" and i!="}":
                        return False
                else:
                    return False
        if len(l)==0:
            return True
        else:
            return False
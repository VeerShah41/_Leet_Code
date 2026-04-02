class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        l={'(':')','{':'}','[':']'}
        stack = []
        for i in s:
            if i in l.keys():
                stack.append(i)

            else:
                if stack:
                    x=stack.pop()
                    
                    if i!=l[x]:
                        return False
                else:
                    return False
            
        return len(stack)==0

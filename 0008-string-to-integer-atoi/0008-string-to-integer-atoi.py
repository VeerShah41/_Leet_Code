class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.lstrip()
       
        if not s:
            return 0
        
        sign = 1
        i = 0

        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1
        no = 0
        while i<len(s) and s[i].isdigit():
            no = no* 10 +int(s[i])
            i+=1
        no*=sign
        ma = 2**31-1
        mi = -2**31
        if no>ma:
            return ma
        if no<mi:
            return mi
        return no



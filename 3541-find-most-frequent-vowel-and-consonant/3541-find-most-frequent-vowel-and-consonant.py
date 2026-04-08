class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = { 'a' : 0 , 'e' : 0 , 'i' : 0 , 'o' : 0 , 'u' : 0 }
        con = {}
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]]+=1
            else:
                if s[i] in con:
                    con[s[i]]+=1
                else:
                    con[s[i]]=1
        max_vov = max(d.values())
        
        if con:
            max_con = max(con.values())
        else:
            max_con = 0
        return max_vov + max_con

class Solution(object):
    def vowelConsonantScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = ['a', 'e', 'i', 'o', 'u']
        n = [" ", "1","2","3","4","5","6","7","8","9","0"]
        v = 0
        c = 0
        for i in s:
            
            if i in l:
                v+=1
            elif i in n:
                continue
            else:
                c+=1
        if c==0:
            return 0
        return v//c
class Solution(object):
    def vowelConsonantScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = ['a', 'e', 'i', 'o', 'u']
        v = 0
        c = 0
        for i in s:
            if i.isalpha():
                if i in l:
                    v+=1
                else:
                    c+=1
        if c==0:
            return 0
        return v//c
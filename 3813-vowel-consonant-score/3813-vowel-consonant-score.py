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
            
            if i=='a' or i=='e'or i=='i'or i=='o'or i=='u':
                v+=1
            elif i==" " or i=="1"or i=="2"or i=="3"or i=="4"or i=="5"or i=="6"or i=="7"or i=="8"or i=="9"or i=="0":
                continue
            else:
                c+=1
        if c==0:
            return 0
        return v//c
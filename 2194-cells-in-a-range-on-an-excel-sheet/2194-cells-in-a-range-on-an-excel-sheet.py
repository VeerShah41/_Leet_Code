class Solution(object):
    def cellsInRange(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        l = []
        q = int(s[1])
        r = int(s[-1])+1
        start = ord(s[0])
        end = ord(s[3])
        for i in range(start,end+1):
            for j in range(q,r):
                l.append(chr(i)+str(j))
        return l

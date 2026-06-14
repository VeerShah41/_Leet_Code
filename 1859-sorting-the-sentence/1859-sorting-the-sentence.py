class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split(" ")
        ans = [""]*len(s)
        for i in s:
            j = int(i[-1])-1
            ans[j]=i[:-1]
        return  " ".join(ans)
            
            



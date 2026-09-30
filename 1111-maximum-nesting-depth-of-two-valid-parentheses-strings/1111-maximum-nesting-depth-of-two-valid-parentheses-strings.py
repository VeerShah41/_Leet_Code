class Solution(object):
    def maxDepthAfterSplit(self, seq):
        """
        :type seq: str
        :rtype: List[int]
        """
        n = len(seq)
        ans = [0]*n
        x = 0
        for i,j in enumerate(seq):
            if j=="(":
                x+=1
                ans[i]=x%2
            else:
                ans[i]=x%2
                x-=1
        return ans
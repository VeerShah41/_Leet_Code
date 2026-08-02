class Solution(object):
    def maxDifference(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = {}
        for i in s:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        e1,e2 = 0,len(s)
        o1,o2 = 0,len(s)
        for i,j in freq.items():
            if j%2==0:
                if e1<j:
                    e1 = j
                if e2>j:
                    e2 = j
            else:

                if o1<j:
                    o1 = j
                if o2>j:
                    o2 = j
        return max(o2-e1,o1-e2)
class Solution(object):
    def maxSumOfSquares(self, num, sum):
        if sum>9*num:
            return ""
        q = sum//9
        r = sum%9
        ans = "9"*q
        if r>0:
            ans+=str(r)
        return ans+"0"*(num-len(ans))


        
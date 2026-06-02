
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        if numRows==1:
            return [[1]]
        ans = [[1],[1,1]]
        flag = 3
        if numRows==2:
            return ans
        def help(flag,ans):
            l=[1]

            for i in range(flag-2):
                l.append(ans[i]+ans[i+1])
            l.append(1)
            
            return l
        for i in range(2,numRows):
            ans.append(help(flag,ans[-1]))
            flag+=1
        return ans

            


            



        
            
            


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = [ [1] , [1, 1] ]
        if numRows==1:
            return [ans[0]]
        if numRows==2:
            return ans
        
        def helper(row,arr):
            l = [1]
            for i in range(1,len(arr)):
                l.append(arr[i-1]+arr[i])
            l.append(1)
            return l

        for i in range(3,numRows+1):
            ans.append(helper(i,ans[i-2]))

        return ans
        
        

            


            



        
            
            

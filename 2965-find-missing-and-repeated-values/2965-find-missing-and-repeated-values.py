class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        n = len(grid)
        f = [0]*((n**2)+1)
        for i in range(n):
            for j in range(n):
                f[grid[i][j]]+=1
        ext = 0
        rep = 0
        for k in range(1,len(f)):
            if f[k]==2:
                ext = k
            if f[k]==0:
                rep = k
                
        return [ext,rep]

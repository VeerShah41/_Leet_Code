class Solution(object):
    def minOperations(self, grid, x):
        """
        :type grid: List[List[int]]
        :type x: int
        :rtype: int
        """
    
        arr = [j for i in grid for j in i]
        
    
        mod = arr[0] % x
        for num in arr:
            if num % x != mod:
                return -1
        

        arr.sort()
        median = arr[len(arr) // 2]
        

        ops = 0
        for num in arr:
            ops += abs(num - median) // x
        
        return ops
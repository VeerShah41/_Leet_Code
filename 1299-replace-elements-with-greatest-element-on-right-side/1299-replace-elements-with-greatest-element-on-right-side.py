class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        ma = max(arr)
        i = 0
        while i < len(arr):
            if arr[i]==ma:
                if i+1 < len(arr):
                    ma = max(arr[i+1:])
                else:
                    ma = -1
            arr[i]=ma
            i+=1
        return arr
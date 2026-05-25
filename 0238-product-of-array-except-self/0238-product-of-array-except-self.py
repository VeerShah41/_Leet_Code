class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p = 1
        flag = False
        pos = float('inf')
        l = [0]*len(nums)
        c=0
        for i in range(len(nums)):
            if nums[i] == 0:
                flag = True
                pos = i
                c+=1
            else:
                p*=nums[i]
        if flag:
            if c==1:
                l[pos] = p
            return l
        
        for j in range(len(nums)):
            
            l[j]=(p//nums[j])
        return l
        


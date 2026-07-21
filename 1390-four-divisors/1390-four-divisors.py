class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in nums:
            c = 2
            s = i+1
            for j in range(2,int(i**0.5)+1):
                if i%j==0:
                    if j == i/j:
                        c+=1
                        s+=j
                    else:
                        c+=2

                        s+=j+(i/j)
                if c>4:
                    break
            if c==4:
                ans+=s
        return ans



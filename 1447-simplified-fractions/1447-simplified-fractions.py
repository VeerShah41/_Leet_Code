class Solution:
    def simplifiedFractions(self, n: int) -> list[str]:
        ans = []
        for i in range(2,n+1):
            for j in range(1,n):
                if gcd(i,j)==1 and j < i :
                    ans.append(str(j)+"/"+str(i))
        return ans
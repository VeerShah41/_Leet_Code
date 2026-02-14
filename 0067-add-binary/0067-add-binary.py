class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        s=""
        n=len(a)-1
        m=len(b)-1
        carry=0
        while n>=0 and m>=0:
            no=int(a[n])+int(b[m])+carry
            carry=0
            
            if no==1:
                s+="1"
            elif no==0:
                s+="0"
            else:
                if no==2:
                    s+="0"
                    carry=1
                else:
                    s+="1"
                    carry=1
        
            n-=1
            m-=1
        while m>=0:
            x=int(b[m])
            if carry:
                if x+carry==1:
                    s+="1"
                    carry=0
                else:
                    s+="0"
                    carry=1
            

            else:

                s+=b[m]
            m-=1
        while n>=0:
            x=int(a[n])
            if carry:
                if x+carry==1:
                    s+="1"
                    carry=0
                else:
                    s+="0"
                    carry=1
            else:

                s+=a[n]
            n-=1
        if carry:
            s+="1"
            carry=0
        return s[::-1]        

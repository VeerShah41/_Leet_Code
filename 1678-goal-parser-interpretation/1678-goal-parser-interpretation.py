class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        ans = ""
        i = 0 
        while i<len(command):
            if command[i]=="G":
                ans+=command[i]
                i+=1
            elif command[i]+command[i+1]=="()":
                ans+="o"
                i+=2
            elif command[i:i+4]=="(al)":
                ans+="al"
                i+=4
        return ans

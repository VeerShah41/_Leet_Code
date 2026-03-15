class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        d = {'2':['a','b','c'],
        '3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],
        '7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        
        final = []
        def help(i,path):
            if i == len(digits):
                final.append(path)
                return
            for ch in d[digits[i]]:
                help(i+1,path+ch)
        help(0,'')
        return final
                



            
            
                


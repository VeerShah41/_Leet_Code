class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        d = {'2':['a','b','c'],
        '3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],
        '7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        
        if len(digits)==1:
            return d[digits]
        elif len(digits)==2:
            i=digits[0]
            j=digits[1]
            combo = []
            for a in d[i]:
                for b in d[j]:
                    combo.append(a+b)
            return combo
        elif len(digits)==3:
            i=digits[0]
            j=digits[1]
            k=digits[2]
            combo = []
            for a in d[i]:
                for b in d[j]:
                    for c in d[k]:
                        combo.append(a+b+c)
            return combo
        else:
            i=digits[0]
            j=digits[1]
            k=digits[2]
            l=digits[3]
            combo = []
            for a in d[i]:
                for b in d[j]:
                    for c in d[k]:
                        for e in d[l]:
                            combo.append(a+b+c+e)
            return combo
            
            
                


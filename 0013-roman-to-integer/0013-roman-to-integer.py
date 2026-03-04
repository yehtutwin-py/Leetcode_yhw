class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        total=0;i=0
        while i<len(s):
            if s[i]=='M':
                if i!=0 and s[i-1]=='C':
                    total+=800
                else:
                    total+=1000
            elif s[i]=='D':
                if i!=0 and s[i-1]=='C':
                    total+=300
                else:
                    total+=500
            elif s[i]=='C':
                if i!=0 and s[i-1]=='X':
                    total+=80
                else:
                    total+=100
            elif s[i]=='L':
                if i!=0 and s[i-1]=='X':
                    total+=30
                else:
                    total+=50
            elif s[i]=='X':
                if i!=0 and s[i-1]=='I':
                    total+=8
                else:
                    total+=10
            elif s[i]=='V':
                if i!=0 and s[i-1]=='I':
                    total+=3
                else:
                    total+=5
            elif s[i]=='I':
                if i!=0 and s[i-1]=='I':
                    if i!=1 and s[i-2]=='I':
                        if i!=2 and s[i-3]=='I':
                            break
                        else: total+=1
                    else: total+=1
                else: total+=1
            i+=1
        return total
        
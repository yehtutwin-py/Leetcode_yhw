class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        x,y=len(a)-1,len(b)-1
        carry_over=0
        result=""
        while x>=0 or y>=0 or carry_over:
            total=carry_over
            if x>=0:
                total+=int(a[x])
                x-=1
            if y>=0:
                total+=int(b[y])
                y-=1
            result=str(total%2)+result
            carry_over=total//2
        return result




                

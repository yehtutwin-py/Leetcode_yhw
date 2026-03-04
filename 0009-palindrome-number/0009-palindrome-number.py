class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        rev_x=0;y=x
        if x<0:
            return False
        while y!=0:
            rev_x = (rev_x*10) + (y%10)
            y=y//10
        if x!=rev_x:
            return False
        else: return True
            
        


        
        
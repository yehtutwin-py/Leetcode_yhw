class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        elif n==2:
            return 2
        else:
            stairs=[1,2]
            for i in range(n-2):
                temp=stairs[1]
                total=stairs[0]+stairs[1]
                stairs[0]=temp; stairs[1]=total
            return total
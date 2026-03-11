class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<2:
            return x
        else:
            left_index=2
            right_index=x/2
            turn=0
            while left_index<=right_index:
                mid = left_index + (right_index-left_index)//2
                num = mid * mid
                if num>x:
                    right_index=mid-1
                elif num<x:
                    left_index=mid+1
                else:
                    return mid
            return right_index

                    
                
                

            

            
        
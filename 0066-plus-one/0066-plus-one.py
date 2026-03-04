class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s=""; result=[]
        if digits[-1]+1<10:
            digits[-1]+=1
            return digits
        else:
            for i in range(len(digits)):
                s+=str(digits[i])
            new_digit=int(s)+1
            result = list(map(int, str(new_digit)))     
            return result
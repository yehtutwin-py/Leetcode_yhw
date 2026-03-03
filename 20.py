class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        box=[]
        for i in range(len(s)):
            if len(s)%2==1:
                return False
            size = len(box)
            if s[i]=='(':
                box.append(s[i])
            elif s[i]==')':
                if len(box)>0:
                    if box[size-1]=='(':
                        box.pop()
                    else: 
                        box.append(s[i])
                else:
                    return False
            elif s[i]=='[':
                box.append(s[i])
            elif s[i]==']':
                if len(box)>0:
                    if box[size-1]=='[':
                        box.pop()
                    else:
                        box.append(s[i])
                else:
                    return False
            elif s[i]=='{':
                box.append(s[i])
            elif s[i]=='}':
                if len(box)>0:
                    if box[size-1]=='{':
                        box.pop()
                    else:
                        box.append(s[i])
                else:
                    return False
        if len(box) == 0:
            return True
        else:
            return False
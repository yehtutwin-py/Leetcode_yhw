class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        cm_prefix = ""; condition = True
        if len(strs) > 1:
            for i in range(len(strs)):
                if i == 0:
                    cm_prefix = strs[i]
                else:
                    for j in range(len(cm_prefix)):
                        if j < len(strs[i]) and cm_prefix[j] == strs[i][j]:
                            continue
                        else:
                            cm_prefix = cm_prefix[:j]
                            break   
        else:
            return strs[0]
        return cm_prefix 
                
                    
        
def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    dummy = []
    for i in range(len(nums)):
        temp=nums[i]
        if dummy.index(temp)==True:
            dummy.append[temp]
    return len(dummy)

s=[0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(s))
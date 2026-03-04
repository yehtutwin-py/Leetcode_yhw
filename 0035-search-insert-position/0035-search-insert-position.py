class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        else:
            for i in range(len(nums)):
                temp=0
                if nums[i]>target:
                    if i==0:
                        return 0
                    else:
                        temp=nums.index(nums[i])
                        break
                else:
                    temp=nums.index(nums[i])+1
            return temp


        
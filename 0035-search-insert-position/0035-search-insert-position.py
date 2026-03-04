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

                if nums[i]<=target:
                    if i==len(nums)-1:
                        return len(nums)
                else:
                    if i==0:
                        return 0
                    else:
                        return nums.index(nums[i])


        
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        nums_copy = nums[:]
        dummy = []
        for i in range(len(nums)):
            if nums_copy[i]==val:
                nums.remove(nums_copy[i])
            else:
                dummy.append(nums_copy[i])
        return len(dummy)
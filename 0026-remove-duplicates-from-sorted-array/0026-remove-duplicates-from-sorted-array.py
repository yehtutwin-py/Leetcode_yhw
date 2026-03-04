class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dummy = []
        nums_copy = nums[:]
        for i in range(len(nums_copy)):
            temp=nums_copy[i]
            if not temp in dummy:
                dummy.append(temp)
            else:
                nums.remove(nums_copy[i])
        return len(dummy)

            
            
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        
        for i in range(len(nums)):
            next_num = target - nums[i]
            
            if next_num in seen:
                return [seen[next_num], i]
            
            seen[nums[i]] = i
        
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in seen:
                return [seen[dif], i]
            else:
                seen[nums[i]] = i
        

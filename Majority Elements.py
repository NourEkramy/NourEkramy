class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        sol=set([ nums[i] for i in range(len(nums)) if nums.count(nums[i])>(len(nums)/3)])
        return sol

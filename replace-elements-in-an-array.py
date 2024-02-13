class Solution(object):
    def arrayChange(self, nums, operations):
        """
        :type nums: List[int]
        :type operations: List[List[int]]
        :rtype: List[int]
        """

        sol={}
        for i in range(len(nums)):
            sol[nums[i]]=i

        for i, j in operations:
            nums[sol[i]]=j
            sol[j]=sol.pop(i)
        
        return nums
        

class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(1,len(nums)):
            if nums[i-1]==nums[i]:
                nums[i-1]=nums[i-1]*2
                nums[i]=0
            
        sol=[ nums[i] for i in range(len(nums)) if nums[i]!=0]
        x=0
        sol2=[x for i in range(nums.count(0))]
        return (sol+sol2)

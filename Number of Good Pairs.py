class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result=0
        i=0

        while i<len(nums):
            j=i+1
            while j<len(nums):
                if nums[i]==nums[j]:
                    result+=1
                j+=1
            i+=1
        return result

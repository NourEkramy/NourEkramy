class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cnt=0

        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                if cnt==1:
                    return False
                cnt+=1
                if i>=2 and nums[i-2]>nums[i]:
                    nums[i]=nums[i-1]
                    
        return True

       
        

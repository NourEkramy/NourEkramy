class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt=0
        mxcnt=0
        for i in nums:
            if i:
                cnt+=1
            else:
                mxcnt=max(mxcnt,cnt)
                cnt=0
        
        return max(mxcnt,cnt)

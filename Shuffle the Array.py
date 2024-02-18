class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        xlist=[nums[i] for i in range(n)]

        ylist=[nums[i] for i in range(n,2*n)]
        sol=[]

        for i in range(n):
                sol.append(xlist[i])
                sol.append(ylist[i])
        
        return sol

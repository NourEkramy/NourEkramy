class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        sol=[]
        if num%3==0:
            sol=[(num/3)-1,(num/3),(num/3)+1]
            return(sol)
        else:
            return(sol)

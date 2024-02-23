class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """

        lst=[i for i in range(1,n+1)]
        rem=0

        while len(lst)!=1:
            x=(rem+k-1)%len(lst)
            lst.pop(x)
            rem=x

        return lst[0]
            

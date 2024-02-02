class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp=x
        sum=0
        num=0
        while temp>0:
            num=temp%10
            sum=(sum*10)+num
            temp=temp/10

        if x is sum:
            return True
        else:
            return False

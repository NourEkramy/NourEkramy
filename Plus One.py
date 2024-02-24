class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num=0
        for i in range(len(digits)-1,-1,-1):
            num+=digits[i]*(10**(len(digits)-1-i))
        
        num+=1
        res = [int(x) for x in str(num)]
        return res

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        list_chk=[]

        for i in range(len(candies)):
            if candies[i]+extraCandies>=max(candies):
                list_chk.append(True) 
            else:
                list_chk.append(False)
        
        return list_chk

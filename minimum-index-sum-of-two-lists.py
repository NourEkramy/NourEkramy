class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        tmp=set(list1)&set(list2)
        sol={}
        for i,r in enumerate(list1):
            if r in tmp:
                sol[r]=i
        
        for i,r in enumerate(list2):
            if r in tmp:
                sol[r]+=i
        
        min_sol=min(sol.values())

        return [i for i,r in sol.items() if r==min_sol]

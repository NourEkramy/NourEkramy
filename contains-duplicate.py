class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        chk=False
        occ=set()
        for i in nums:
            if i in occ:
               chk=True
               break
            else:
                occ.add(i)

        return chk
        

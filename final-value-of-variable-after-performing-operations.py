class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        x=0
        
        for op in operations:
            if op=="X++" or op=="++X":
                x=x+1
            else:
                x=x-1
        
        return x

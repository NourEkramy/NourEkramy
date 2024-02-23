class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        rows, cols = len(strs), len(strs[0])
        arr = [[0] * rows for _ in range(cols)]  
        
        for i in range(rows):
            for j in range(cols):
                arr[j][i] = strs[i][j]
        
        sol=len(arr)

        for i in arr:
            if i != sorted(i):
                sol += 1
        
        return sol-len(arr)

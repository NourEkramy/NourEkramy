class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        rows, cols = len(matrix), len(matrix[0])
        arr = [[0] * rows for _ in range(cols)]  
        for i in range(rows):
            for j in range(cols):
                arr[j][i] = matrix[i][j]
        return arr

# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 15:17:04 2020

@author: 15025
"""

class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        rows = len(matrix)
        # print(rows)
        cols = len(matrix[0])
        # print(f"The value of clos is: {cols}")
        if target < matrix[0][-1]:
            for col in range(cols):
                    if matrix[0][col] == target:
                        return True
                    else:
                        return False
        else:    
            for row in range(rows - 1):
                # print(matrix[row][-1])
                # print(matrix[row + 1][-1])
                # print(f"The value of target is: {target}")
                if target == matrix[row][-1] or target == matrix[row + 1][-1]:
                    return True
                if target > matrix[row][-1] and target < matrix[row + 1][-1]:
                    print(f"If sentence has been executed.")
                    for col in range(cols):
                        # print(col)
                        print(matrix[row][col])
                        if matrix[row + 1][col] == target:
                            return True
            return False
                        
main = Solution()
# test
# result = main.searchMatrix([[5]], 2)
result = main.searchMatrix([[1,4,5],[6,7,8]], 8)
print(result)
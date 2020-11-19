# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 08:20:42 2020

@author: 15025
# 您的提交打败了 100.00% 的提交!
"""

class Solution:
    """
    @param n: An integer
    @return: A list of strings.
    """
    def fizzBuzz(self, n):
        # write your code here
        list1 = []
        for i in range(1, n+1):
            if i % 3 == 0:
                if i % 5 == 0:
                    list1.append("fizz buzz")
                else:
                    list1.append("fizz")
            elif i % 5 == 0:
                list1.append("buzz")
            else:
                list1.append(f"{i}")
            
        return list1
    
main = Solution()
result = main.fizzBuzz(15)
print(result)
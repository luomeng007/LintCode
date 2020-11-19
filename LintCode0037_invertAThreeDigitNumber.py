# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 08:31:32 2020

@author: 15025
反转一个三位数
"""

class Solution:
    """
    @param number: A 3-digit number.
    @return: Reversed number.
    """
    def reverseInteger(self, number):
        # write your code here
        self.a = number // 100
        self.b = number // 10 - self.a * 10
        self.c = number % 10
        if self.c != 0:
            return self.c * 100 + self.b * 10 + self.a
        elif self.b != 0:
            return self.b * 10 + self.a
        else:
            return self.a

main = Solution()
result = main.reverseInteger(123)
result = main.reverseInteger(900)
print(result)
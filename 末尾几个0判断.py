# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 09:02:57 2020

@author: 15025
虽然可以得到结果，但是当阶乘数字较大时，可能会溢出，时间复杂度太复杂，
可以进一步优化算法，尝试
"""

class Solution:
    """
    @param: n: An integer
    @return: An integer, denote the number of trailing zeros in n!
    """
    def trailingZeros(self, n):
        # write your code here, try to do it without arithmetic operators.
        result = 1
        for i in range(1, n+1):
            result *= i
        # print(result)
        count = 0
        while result % 10 == 0:
            count += 1
            result //= 10   # 这里一定要使用整除！！！！！！！！！！！！！！！！！！！！！！！！！
            # print(result)
            
        return count

main = Solution()
num = main.trailingZeros(105)
print(num)
# =============================================================================
# 科学计数法对10取余结果是否为0

# result = 1.23423523525e+63
# if result % 10 == 0:
#     print("余数为0")
# 用科学计数法显示的时候，末尾不视为以0结尾
# =============================================================================
#

# result = 1.23423523525e+63
# print("%d" % result)
# 也就是说在以科学计数法表示后，其他位上的数字已经出现了偏差，虽然很小，尽量避免
# =============================================================================
# 看是否可以关闭科学计数法

# import numpy as np
# np.set_printoptions(suppress=True)  # 感觉不是很好用

# result = np.array([12342352352500000000000000000000000000000000000000000000000])
# # print(result)

# =============================================================================
# result = 12342352352500000000000000000000000000000000000000000000000
# count = 0
# while result % 10 == 0:
    
#     count += 1
#     result //= 10   # 这里一定不要使用result /= 10，结果会不正确，选择整出代替
#     print(count)
#     print(result)
    
# print(count)    
# 1000的时候输出为3 代码没毛病
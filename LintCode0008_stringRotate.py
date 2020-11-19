# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:15:37 2020

@author: 15025
8. 旋转字符串
中文English
给定一个字符串（以字符数组的形式给出）和一个偏移量，根据偏移量原地旋转字符串(从左向右旋转)。

样例
样例 1:

输入:  str="abcdefg", offset = 3
输出:  str = "efgabcd"	
样例解释:  注意是原地旋转，即str旋转后为"efgabcd"
样例 2:

输入: str="abcdefg", offset = 0
输出: str = "abcdefg"	
样例解释: 注意是原地旋转，即str旋转后为"abcdefg"
样例 3:

输入: str="abcdefg", offset = 1
输出: str = "gabcdef"	
样例解释: 注意是原地旋转，即str旋转后为"gabcdef"
样例 4:

输入: str="abcdefg", offset =2
输出: str = "fgabcde"	
样例解释: 注意是原地旋转，即str旋转后为"fgabcde"
样例 5:

输入: str="abcdefg", offset = 10
输出: str = "efgabcd"	
样例解释: 注意是原地旋转，即str旋转后为"efgabcd"
挑战
在数组上原地旋转，使用O(1)的额外空间
NB:
    return 函数不能够返回表达式
"""
# %% 类似于字符串旋转，但是并不是原地旋转
class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotateString(self, s, offset):
        # write your code here
        new_string = s[-offset::] + s[0:-offset]
        return new_string
        # we could use s[offset:] or s[offset::]    

main = Solution()
result = main.rotateString("abcdefg", 3)
print(result)

# %% 字符串原地旋转， 原地旋转意味着你要在s本身进行修改。你不需要返回任何东西。
class Solution:
    """
    先转换为list，进行pop，insert操作，最后用join将list各个元素连接起来
    """
    def rotateString(self, s, offset):
        # write your code here
        s = list(s)
        for i in range(offset):
            ele = s.pop(-1)
            s.insert(0, ele)
        print(("").join(s))
        
            
main = Solution()
# main.rotateString("abcdefg", 3)
main.rotateString("''", 10)
# %%
s = "abcdefg"
# print(s[-3:-1]) # 只能输出ef
# print(s[-3::])  # efg
# print(s[-3:])  # efg
list_s = list(s)
print(list_s.pop())     # g
print(list_s.pop(-1))   # f
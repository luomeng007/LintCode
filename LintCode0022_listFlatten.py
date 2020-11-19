# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 10:25:06 2020

@author: 15025
"""
# %%
list1 = [[1,1],2,[1,1]]
print(len(list1))   # 3

# %%
# 需要递归调用！！！！
class Solution(object):

    # @param nestedList a list, each element in the list 
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList):
        # Write your code here
        list_result = []
        list_1D = []
        list_2D = []
        print(len(nestedList))
        if len(nestedList) == 1:
            return nestedList
        elif len(nestedList) == 2:
            for list_1D in nestedList:
                list_result = list_result + list(list_1D)
            return list_result
        # elif len(nestedList) == 3:
        #     for list_2D in nestedList:
        #         for list_1D in list_2D:
        #             list_result = list_result + list(list_1D)
        #     return list_result
        else:
            return "The input list is wrong!"
        
main = Solution()
result = main.flatten([[1,1],2,[1,1]])
print(result)
# %% 递归法，来源于网络大神
class Solution(object):
 
    # @param nestedList a list, each element in the list 
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def __init__(self) :
        self.flat_list = [] # Defined in the method will be looped to initialize
    def flatten(self, nestedList):
        # Write your code here
        for sublist in nestedList:
            if isinstance(sublist, int):
                self.flat_list.append(sublist)
            else:
                self.flatten(sublist)
        return self.flat_list
    
main = Solution()
result = main.flatten([[1,1],2,[1,1]])
print(result)
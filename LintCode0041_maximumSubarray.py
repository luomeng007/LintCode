# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 08:27:00 2020

@author: 15025
最大子数组：
Comment:
    思路清奇，并不难以理解，尝试有没有别的方法
"""

class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    # 注意题目并不需要你返回数组
    """
    def maxSubArray(self, nums):
        # write your code here
        # 先找出所有正值的index
        index1 = []
        for i in range(len(nums)):
            if nums[i] > 0:
                index1.append(i)
        # 两端的负值自动pass
        sum1 = 0
        final = 0
        for i in range(index1[0], index1[-1] + 1):
            sum1 += nums[i]
            final = max(final, sum1)
            if sum1 < 0:
                sum1 = 0
        return final
                
        
        
main = Solution()
result = main.maxSubArray([-2, 2, -3, 4, -1, 2, 1, -5, 3])
print(result)
# 潜在存在问题，若该数组仅有一个值，且为负值，程序将会报错，推荐使用第三个程序
# %%
# x = [-2,2,-3,4,-1,2,1,-5,3]
# print(x)
# %% 来源于网络
# def max_child(arr):
# 	result = arr[0]
# 	sum = arr[0]
# 	x = 0
# 	for i in range(1, len(arr)):
# 		if sum > 0:
# 			sum += arr[i]
# 		else:
# 			sum = arr[i]
# 			x = i
# 		if sum > result:
# 			result = sum
# 			y = i
# 	print("最大子数组的起始-结束下标", x, y)
# 	return result
 
# arr = [1, 2, -3, 4, 5]
# print("最大子数组的和：",max_child(arr)) 
# 该程序存在瑕疵
# %%
class Solution:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return 0
        sum = -2**31 - 1
        ans = 0
        for i in nums:
            ans += i
            sum = max(ans, sum)
            if ans < 0:
                ans = 0
        return sum

main = Solution()
result = main.maxSubArray([-2, 2, -3, 4, -1, 2, 1, -5, 3])
print(result)
# nice job， 您的提交打败了 87.00% 的提交!

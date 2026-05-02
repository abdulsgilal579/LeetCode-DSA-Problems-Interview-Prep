"""Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.



Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]


Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.


Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""

# --------------------------------------
# Brute Force Approach
# --------------------------------------

# intArray = [1,2,3,4]
#
# def productOfArrayExceptItself(array):
#     new_array = [0]*len(array)
#
#     for i in range(0,len(array)):
#         product = 1
#         for j in range(0, len(array)):
#             if j != i:
#                 product *= array[j]
#         new_array[i] = product
#     return new_array
#
# print(productOfArrayExceptItself(intArray))

# ----------------------------------------
# Optimal Solution The Most Efficient One
# ----------------------------------------

# Time Complexity of O(n)

array = [1, 2, 3, 4]
prefixArray = [1] * len(array)
for i in range(1, len(array)):
    prefixArray[i] = prefixArray[i - 1] * array[i - 1]

suffixArray = [1] * len(array)
for i in range(len(array) - 2, -1, -1):
    suffixArray[i] = suffixArray[i + 1] * array[i + 1]

finalArray = [1] * len(array)
for i in range(0, len(array)):
    finalArray[i] = prefixArray[i] * suffixArray[i]

print(finalArray)

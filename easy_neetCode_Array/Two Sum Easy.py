#Solution

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, number in enumerate(nums):
            compliment = target - number
            if compliment in seen:
                return [seen[compliment], index]
            else:
                seen[number] = index































#
# #
# # class Solution:
# #     def twoSum(self, nums: List[int], target: int) -> List[int]:
# #         for i in range(len(nums)):
# #             for j in range(i + 1, len(nums)):
# #                 if nums[i] + nums[j] == target:
# #                     return [i, j]
#
# array = [1, 7, 11, 2]
# target = 9
# def twoSum(array, target):
#     seen = {}
#     for i, number in enumerate(array):
#         compliment = target - number
#         if compliment in seen:
#             return [seen[compliment], i]
#         else:
#             print(f"Before addition {seen}")
#             seen[number] = i
#             print(f"After addition {seen}")
#
# print(twoSum(array, target))







from asyncio import current_task
from os.path import curdir

array = [-1, 0]


def twoSum(array, target):
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == target:
            return left + 1, right + 1
        elif currentSum > target:
            right -= 1
        else:
            left += 1
    return "Indexes not found"


print(twoSum(array, target=-1))

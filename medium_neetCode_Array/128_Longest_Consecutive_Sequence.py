#Brute_Force_Approach

# nums = [100,4,200,1,3,2]

# def longestConsecutiveSequence(nums):
#     sortedArray = sorted(nums)
#     currentStreak = 1
#     bestStreak = 1
#     if len(nums) == 0:
#         return 0
#     for i in range(0, len(sortedArray) - 1):
#         if sortedArray[i + 1] - sortedArray[i] == 1:
#             currentStreak += 1
#             bestStreak = max(currentStreak, bestStreak)
#         elif sortedArray[i + 1] - sortedArray[i] == 0:
#             continue
#         else:
#             currentStreak = 1
#     return bestStreak

# print(longestConsecutiveSequence(nums=nums))


#----------------------------------------------
#OPTIMAL SOLUTION
#----------------------------------------------

nums = [100,4,200,1,3,2]

def longestStreak(nums):
    numSet = set(nums)
    result = 0
    for number in nums:
        if number - 1 not in numSet:
            current_Streak = 1
            while number + current_Streak in numSet:
                current_Streak +=1
            result = max(result, current_Streak)
    return result

print(longestStreak(nums))
        


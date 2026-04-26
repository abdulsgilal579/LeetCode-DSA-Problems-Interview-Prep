#Brute_Force_Approach
from http.cookiejar import cut_port_re

nums = [100,4,200,1,3,2]

def longestConsecutiveSequence(nums):
    sortedArray = sorted(nums)
    currentStreak = 1
    bestStreak = 1
    for i in range(0,len(sortedArray)-1):
        if sortedArray[i+1] - sortedArray[i] == 1:
            currentStreak +=1
            bestStreak = max(currentStreak, bestStreak)
        elif sortedArray[i+1] - sortedArray[i] == 0:
            continue
        else:
            currentStreak =1
    return bestStreak





print(longestConsecutiveSequence(nums=nums))    

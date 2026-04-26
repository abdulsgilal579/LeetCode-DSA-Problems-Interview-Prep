#BruteForce Approach

nums = [100,4,200,1,3,2]

def longestConsecutiveSequence(nums):
    sortedArray = sorted(nums)
    difference = nums[1] - nums[0]
    for i in range(0, len(nums)):
        if nums[i+1] - nums[i] != 




print(longestConsecutiveSequence(nums=nums))

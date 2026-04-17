import math

unsortedArray = [8, 5, 65, 1234, 665, 3434,8, 5, 65, 1234, 665, 3434.8, 5, 65, 1234, 7]

min_value = min(unsortedArray)
max_value = max(unsortedArray)

numberOfBuckets = int((math.sqrt(len(unsortedArray))))

bucketList = [ [] for _ in range (numberOfBuckets)]

print(bucketList)

for element in unsortedArray:
    index = math.floor(((element - min_value)/(max_value - min_value + 1)) * numberOfBuckets)
    bucketList[index].append(element)
    
print(bucketList)
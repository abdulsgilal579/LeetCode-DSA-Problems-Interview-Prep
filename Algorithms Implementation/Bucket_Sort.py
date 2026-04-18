import math
from insertion_Sort import insertionSortAlgorithm

unsortedArray = [8, 5, 65, 1234, 665, 3434,8, 5, 65, 1234, 665, 3434.8, 5, 65, 1234, 7]

min_value = min(unsortedArray)
max_value = max(unsortedArray)

numberOfBuckets = int((math.sqrt(len(unsortedArray))))

bucketList = [ [] for _ in range (numberOfBuckets)]

for element in unsortedArray:
    ##normalize distribution formula
    index = math.floor(((element - min_value)/(max_value - min_value + 1)) * numberOfBuckets)
    bucketList[index].append(element)

final_sorted_list = []

for list in bucketList:
    sortedList = insertionSortAlgorithm(list)
    final_sorted_list.append(sortedList)

print(final_sorted_list)



array = [-1, 0, 1, 2, -1, -4]


def ThreeSum(array):
    sortedArray = sorted(array)
    tripletList = []
    for i in range(0, len(array) - 2):
        if i > 0 and sortedArray[i] == sortedArray[i - 1]:
            continue
        left = i + 1
        right = len(array) - 1
        while left < right:
            total = sortedArray[left] + sortedArray[right] + sortedArray[i]
            if total > 0:
                right -= 1
            elif total < 0:
                left += 1
            else:
                subList = [sortedArray[i], sortedArray[left], sortedArray[right]]
                tripletList.append(subList)
                left += 1
                right -= 1
                while left < right and sortedArray[left] == sortedArray[left - 1]:
                    left += 1
                while left < right and sortedArray[right] == sortedArray[right + 1]:
                    right -= 1
    return tripletList


print(ThreeSum(array=array))

inputHeight = [1, 1]


def containerWithMostWater(inputHeight):
    computedArea = 0
    leftPointer = 0
    rightPointer = len(inputHeight) - 1
    while leftPointer < rightPointer:
        areaAtThisPoint = (rightPointer - leftPointer) * min(
            inputHeight[leftPointer], inputHeight[rightPointer]
        )
        computedArea = max(computedArea, areaAtThisPoint)
        if inputHeight[leftPointer] < inputHeight[rightPointer]:
            leftPointer += 1
        else:
            rightPointer -= 1
    return computedArea


print(containerWithMostWater(inputHeight=inputHeight))


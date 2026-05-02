inputHeight = [4,2,0,3,2,5]


def tappingRainWater(inputHeight):
    totalTappingWater = 0
    leftPointer = 0
    rightPointer = len(inputHeight) - 1
    maxLeft = 0
    maxRight = 0
    while leftPointer < rightPointer:
        if maxLeft <= maxRight:
            maxLeft = max(maxLeft, inputHeight[leftPointer])
            totalTappingWater += maxLeft - inputHeight[leftPointer]
            leftPointer += 1
        else:
            maxRight = max(maxRight, inputHeight[rightPointer])
            totalTappingWater += maxRight - inputHeight[rightPointer]
            rightPointer -= 1
    return totalTappingWater

print(tappingRainWater(inputHeight=inputHeight))



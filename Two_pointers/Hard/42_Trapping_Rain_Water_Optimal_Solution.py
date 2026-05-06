inputHeight = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
inputHeight2 = [1, 2, 3, 4, 5, 6]

# def trappingRainWater(inputHeight):
# leftMax = 0
# rightMax = 0
# leftPointer = 0
# rightPointer = len(inputHeight) - 1
# sum = 0

# while leftPointer < rightPointer:
#     if leftMax <= rightMax:
#         leftMax = max(leftMax, inputHeight[leftPointer])
#         sum += leftMax - inputHeight[leftPointer]
#         leftPointer += 1
#     else:
#         rightMax = max(rightMax, inputHeight[rightPointer])
#         sum += rightMax - inputHeight[rightPointer]
#         rightPointer -= 1
# return sum

# print(trappingRainWater(inputHeight=inputHeight))


def trappingRainWaterFreeStyle(inputHeight):
    sum = 0
    arrayLength = len(inputHeight)
    leftMax = 0
    rightMax = 0
    leftPointer = 0
    rightPointer = arrayLength - 1

    while leftPointer <= rightPointer:
        if leftMax < rightMax:
            leftMax = max(leftMax, inputHeight[leftPointer])
            sum += max(0, min(leftMax, rightMax) - inputHeight[leftPointer])
            leftPointer += 1
        else:
            rightMax = max(rightMax, inputHeight[rightPointer])
            sum += max(0, min(leftMax, rightMax) - inputHeight[rightPointer])
            rightPointer -= 1
    return sum


print(trappingRainWaterFreeStyle(inputHeight=inputHeight))

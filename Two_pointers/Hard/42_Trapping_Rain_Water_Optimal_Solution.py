inputHeight = [0,1,0,2,1,0,1,3,2,1,2,1]

def trappingRainWater(inputHeight):
    leftMax = 0
    rightMax = 0
    leftPointer = 0
    rightPointer = len(inputHeight) - 1 
    sum = 0

    while leftPointer < rightPointer:
        if leftMax <= rightMax:
            leftMax = max(leftMax, inputHeight[leftPointer])
            sum += leftMax - inputHeight[leftPointer]
            leftPointer += 1
        else:
            rightMax = max(rightMax, inputHeight[rightPointer])
            sum += rightMax - inputHeight[rightPointer]
            rightPointer -= 1 
    return sum

print(trappingRainWater(inputHeight=inputHeight))
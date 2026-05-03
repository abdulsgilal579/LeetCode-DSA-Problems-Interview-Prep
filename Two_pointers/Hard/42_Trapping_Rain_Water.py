inputHeight = [1, 1]

# Better_Solution


def containerWithMostWater(inputHeight):
    arrayLength = len(inputHeight)
    maxLeft = [0] * arrayLength
    maxRight = [0] * arrayLength
    maxRight[arrayLength-1] = inputHeight[arrayLength-1]
    maxLeft[0] = inputHeight[0]
    sum = 0

    # filling_maxLeft_Array
    # The goal of maxLeft[i] is to answer: "What is the tallest bar to the LEFT of index i?"
    # So at any index i, you need to know the highest bar seen so far in all previous positions. That's why:
    
    for i in range(0, arrayLength - 1):
        maxLeft[i] = max(maxLeft[i - 1], inputHeight[i])

    for i in range(arrayLength - 2, -1, -1):
        maxRight[i] = max(maxRight[i + 1], inputHeight[i])

    for i in range(0, arrayLength - 1):
        sum += min(maxLeft[i], maxRight[i]) - inputHeight[i]
    
    return sum




print(containerWithMostWater(inputHeight=inputHeight))

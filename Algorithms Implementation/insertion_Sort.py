#Implementation of the insertion sort algorithm important for the bucket sort
#Work left to the right
#Examine each item and compare it to the items on it's left
#Insert the item in the correct position in the array

def insertionSortAlgorithm(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

if __name__ == "__main__":
    unsortedArray = [2, 8, 5, 3, 9, 4]
    print(insertionSortAlgorithm(unsortedArray))
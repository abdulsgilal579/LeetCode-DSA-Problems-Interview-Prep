stringArray = ["Hello", "World"]

def encode(array):
    string = ""
    for i in array:
        string += str(len(i)) + "#" + i
    return string

def decode(encodeString):
    decodedList = []
    pointer = 0
    while pointer < len(encodeString):
        j = pointer
        while encodeString[j] != "#":
            j += 1
        length = int(encodeString[pointer:j])
        decodedList.append(encodeString[j+1 : j + 1 + length])
        pointer = j+1+length
    return decodedList

print(decode(encode(stringArray)))


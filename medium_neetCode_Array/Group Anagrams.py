from collections import defaultdict

input_string = [""]

def groupAnagram(stringList):
    result = defaultdict(list)
    for word in stringList:
        key = tuple(sorted(word))
        result[key].append(word)
    return list(result.values())

print(groupAnagram(input_string))
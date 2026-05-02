string = "A man, a plan, a canal: Panama"


def valid_palindrome(string):
    cleanedString = "".join([c.lower() for c in string if c.isalnum()])
    left = 0
    right = len(cleanedString) - 1
    while left < right:
        if cleanedString[left] != cleanedString[right]:
            return False
        else:
            left += 1
            right -= 1

    return True


print(valid_palindrome(string))

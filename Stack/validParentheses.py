string = "()[]{}"


def validParentheses(string):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for character in string:
        if character in mapping:
            if not stack or stack[-1] != mapping[character]:
                return False
            stack.pop()
        else:
            stack.append(character)
    return len(stack) == 0


print(validParentheses(string=string))

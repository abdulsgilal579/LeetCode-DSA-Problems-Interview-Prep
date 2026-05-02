if len(s) != len(t):
    return False

frequency_dict_s = {}
for char in s:
    if char in frequency:
        frequency_dict_s[char] = +1
    else:
        frequency_dict_s[char] = 1

frequency_dict_t = {}
for char in t:
    if char in frequency:
        frequency_dict_t[char] = +1
    else:
        frequency_dict_t[char] = 1
for key, value in frequency_dict_s.items():
    if key not in frequency_dict_t:
        return False
    elif frequency_dict_s[key] != frequency_dick_t[key]:
        return False
return True

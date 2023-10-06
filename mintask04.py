d = {"a": 3, (1, 2): "a", (1, 3): "a", (1, 4): "a", "c": 1}
unique_keys = {}
reversed_dict = {}
for key, value in d.items():
    if value in unique_keys:
        reversed_dict[value] = unique_keys[value], key
        unique_keys.pop(value)
    elif value in reversed_dict:
        reversed_dict[value] += key,
    else:
        unique_keys[value] = key
for key, value in unique_keys.items():
    reversed_dict[key] = value
print(reversed_dict)
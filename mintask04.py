d = {"a": 3, (1, 2): "a", (1, 3): "a", (1, 4): "a", "c": 1}
unique_keys = set()
reversed_dict = {}
for key, value in d.items():
    if value in unique_keys:
        reversed_dict[value] = (reversed_dict[value], key)
        unique_keys.remove(value)
    elif value in reversed_dict:
        reversed_dict[value] += key,
    else:
        reversed_dict[value] = key
        unique_keys.add(value)

print(reversed_dict)

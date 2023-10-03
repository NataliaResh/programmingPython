d = {"a": 3, (1, 2): "a", (1, 3): "a", (1, 4): "a", "c": 1}
repetitive_keys = {}
unique_keys = {}
reversed_dict = {}
for key, value in d.items():
    if value in unique_keys:
        repetitive_keys[value] = unique_keys[value], key
        unique_keys.pop(value)
    elif value in repetitive_keys:
        repetitive_keys[value] += key,
    else:
        unique_keys[value] = key
reversed_dict = repetitive_keys
for key, value in unique_keys.items():
    repetitive_keys[key] = value
print(reversed_dict)

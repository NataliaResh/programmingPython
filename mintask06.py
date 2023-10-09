def flatten(arr):
    if not isinstance(arr, list):
        return arr
    new_arr = []
    for i in arr:
        if isinstance(i, list):
            new_arr.extend(flatten(i))
        else:
            new_arr.append(i)
    return new_arr


a = [1, 2, [4, 5], [6, [7]], 8]
print(flatten(a))

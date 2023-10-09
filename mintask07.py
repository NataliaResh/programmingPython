def flatten(arr, depth=-1):
    if depth == 0:
        return arr
    if not isinstance(arr, list):
        return arr
    new_arr = []
    for el in arr:
        if isinstance(el, list):
            new_arr.extend(flatten(el, depth - 1))
        else:
            new_arr.append(el)
    return new_arr


a = [1, 2, [4, 5], [6, [7]], 8]
print(flatten(a, 1))

def my_zip(array1, array2):
    zip_len = min(len(array1), len(array2))
    zip_array = []
    for i in range(zip_len):
        zip_array.append((array1[i], array2[i]))
    return zip_array


a = [1, 2, 3]
b = ['a', 'b']
print(my_zip(a, b))
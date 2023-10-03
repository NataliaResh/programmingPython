def matrix_array(array_str):
    return [[float(i) for i in line.split()] for line in array_str.split('|')]


s = input()
array = matrix_array(s)
print(array)
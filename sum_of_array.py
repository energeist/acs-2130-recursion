import math

arr = [1,2,3,4,5]

def sum_arr(arr):
    if len(arr) == 1:
        return arr[0]
    return arr[0] + sum_arr(arr[1:])

print(sum_arr(arr))


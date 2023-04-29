import math

arr = [20, 15, 89, 65, 23, 43]

def find_max_num(arr, maxnum = arr[0]):
    if len(arr) == 0:
        return maxnum
    elif arr[0] > maxnum:
        maxnum = arr[0]
    return find_max_num(arr[1:], maxnum)

print(find_max_num(arr))

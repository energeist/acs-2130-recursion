import math

arr = [20, 15, 89, 65, 23, 43]
arr = sorted(arr)

def recursive_binary_search(arr, item):
    if len(arr) == 1:
        if arr[0] == item:
            return f"found {item} in list"
        else:
            return f"{item} not found in list"
    else:
        if arr[0] == item:
            return f"found {item} in list"
        else:
            if arr[len(arr)//2] <= item:
                return recursive_binary_search(arr[(len(arr)//2):], item)
            else:
                return recursive_binary_search(arr[:(len(arr)//2)], item)
                
print(recursive_binary_search(arr, 89))
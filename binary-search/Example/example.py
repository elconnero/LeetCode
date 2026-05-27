def BinarySearch(arr, target):
    left = 0
    right = len(arr)  - 1


    if right < 0: return -1
    
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target: return mid
        if arr[mid] < target: left = mid + 1
        else: right = mid - 1
    return -1

test = BinarySearch([1,2,3,4,5,6,7,8,9], 8)
print(test)
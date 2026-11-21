# Find the position where a target should be inserted in a sorted list.

arr = [10, 20, 30, 40, 50]
target = 35

low = 0
high = len(arr) - 1
position = len(arr)

while low <= high:
    mid = (low + high) // 2

    if arr[mid] >= target:
        position = mid
        high = mid - 1
    else:
        low = mid + 1

print("Insert position:", position)
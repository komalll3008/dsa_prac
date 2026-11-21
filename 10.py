# Find the first and last occurrence of an element in a sorted list.

arr = [10, 20, 20, 20, 30, 40, 50]
target = 20

first = -1
last = -1

low = 0
high = len(arr) - 1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == target:
        first = mid
        high = mid - 1
    elif arr[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

low = 0
high = len(arr) - 1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == target:
        last = mid
        low = mid + 1
    elif arr[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

print("First:", first)
print("Last:", last)
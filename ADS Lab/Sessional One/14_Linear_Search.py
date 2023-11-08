def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i 
    return -1


def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1 


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 6


linear_result = linear_search(arr, target)
if linear_result != -1:
    print(f"Linear Search: Element {target} found at index {linear_result}")
else:
    print(f"Linear Search: Element {target} not found")


binary_result = binary_search(arr, target)
if binary_result != -1:
    print(f"Binary Search: Element {target} found at index {binary_result}")
else:
    print(f"Binary Search: Element {target} not found")

def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    low_index = 0
    high_index = len(arr) - 1

    mid_index = int( (low_index + high_index) / 2 )

    if high_index == -1:
        return -1

    while arr[low_index:high_index+1]:
        # print("List:", str(arr[low_index:high_index+1]))
        # print("Low index:", low_index)
        # print("Mid index:", mid_index)
        # print("High index:", high_index)

        if arr[mid_index] == target:
            return mid_index
        elif arr[mid_index] > target:
            high_index = mid_index - 1
            mid_index = int( (low_index + high_index) / 2 )
        elif arr[mid_index] < target:
            low_index = mid_index + 1
            mid_index = int( (low_index + high_index) / 2 )

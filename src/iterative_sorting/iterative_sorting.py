# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(i+1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j

        # TO-DO: swap
        # Your code here
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    for i in range(len(arr)):  # For each index in the array...
        for j in range(0, len(arr)-i-1):  # Check every index after it...
            if arr[j] > arr[j+1]:  # If the biggest value is before the smallest value...
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap!


    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here
    # Find max and check for negatives:
    max_val = 0
    for n in arr:
        if n > max_val:
            max_val = n
        elif n < 0:
            return "Error, negative numbers not allowed in Count Sort"

    # Create buckets
    buckets = [0] * (max_val + 1)

    # Add values to buckets
    for n in arr:
        buckets[n] += 1

    # Reconstruct sorted list from buckets
    arr = []
    for i in range(0, len(buckets)):
        arr = arr + [i] * buckets[i]

    return arr

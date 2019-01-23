import sys 
from random import randrange


def partition(x, pivot_index):
    i = 0
    if pivot_index !=0: x[0],x[pivot_index] = x[pivot_index],x[0]
    for j in range(len(x)-1):
        if x[j+1] < x[0]:
            x[j+1],x[i+1] = x[i+1], x[j+1]
            i += 1
    x[0],x[i] = x[i],x[0]
    return x, i


def quickSelect(arr,k):
    if len(arr) == 1:
        return arr[0]
    else:
        partitioned_arr = partition(arr,randrange(len(arr)))
        arr = partitioned_arr[0] # partitioned array
        j = partitioned_arr[1] # pivot index
        if j == k:
            return arr[j]
        elif j > k:
            return quickSelect(arr[:j], k)
        else:
            k = k - j - 1
            return quickSelect(arr[(j+1):], k)

# Read input
test_values = [4, 2, 8, 0, 1]
n = test_values[0]
k = test_values[1] 
numbers = [5]

kSmallest = quickSelect(numbers,k)

print kSmallest
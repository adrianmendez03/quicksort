def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp 

def partition(arr, start, end):
    pivotIndex = start
    pivotValue = arr[end]
    while start <= end:
        if arr[start] < pivotValue:
            swap(arr, start, pivotIndex)
            pivotIndex += 1
        start += 1
    swap(arr, pivotIndex, end)
    return pivotIndex

def quickSort(arr, start, end):    
    if start >= end: 
        return
    index = partition(arr, start, end)
    
    quickSort(arr, start, index - 1)
    quickSort(arr, index + 1, end)
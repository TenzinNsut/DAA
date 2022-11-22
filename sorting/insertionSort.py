
def insertionSort(arr):
    for i in range (1,len(arr)):
        pos = i
        while (pos>0 and arr[pos]<arr[pos-1]):
            (arr[pos],arr[pos-1]) = (arr[pos-1],arr[pos])
            pos = pos-1
    return (arr)

arr = [31,56,3,-2,12,54,6]
print("list: ", arr)
print("Sorted list:",insertionSort(arr))
    
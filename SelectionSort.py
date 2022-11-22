
def SelectionSort(arr):
    # Traverse all the elements in the array
    for i in range(len(arr)):
        min_ind = i;
        #traverse through second array to find the mininmum element and swap
        for j in range(i+1,len(arr)):
            if arr[min_ind]> arr[j]:
                min_ind = j

        #swap the values
        arr[i], arr[min_ind] = arr[min_ind], arr[i]





arr =  [2,1,5,3,4,6]
SelectionSort(arr)
print(arr)
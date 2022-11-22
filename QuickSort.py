def partion(arr,low,high):
    pivot = arr[low]
    leftwall = low
    
    for i=low+1 in range(len(arr)):
        if(arr[i]<pivot):
            arr[i], arr[leftwall] = arr[leftwall],arr[i]





def QucikSort(arr,low,high):
    if (low<high):
        piv_loc = partion(arr,low,high)

    





arr = []
low =  0
high = 9

QucikSort(arr,low,high)

print(arr)
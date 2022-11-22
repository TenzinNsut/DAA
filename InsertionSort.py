
def InsertionSort(arr):
    for i in range(1,len(arr)): # iterates from second element in the list
        j = i #initially j = 1
        while  arr[j-1] > arr[i] and j>0: # j>0 to let use know the we are not at -1 index
            arr[j-1], arr[j] = arr [j], arr[j-1] #swap
            j -= 1; #for comparing the left side of the sorted array




# arr = [1,3,2,4,8,6,7]
# InsertionSort(arr)
# print(arr)

# n = int(input("Enter the number of elements: "))
# data = list(map(int(input("\n Enter numbers: ").strip.split()))) [:n]
# print(data)

# arr = (data)
# InsertionSort(arr)
# print(arr)

#=========================================================
# Input form the unser
arr = []
n = int(input("Enter the number of elements: "))

for t  in range(n):
    item = int(input())
    arr.append(item)
print(arr)



#===========================================================
InsertionSort(arr)
print(arr)

def LinearSearch(arr, key):
    for i in range (len(arr)):
        if (arr[i] == key):
            return f"item found at position: {i}"
    return f"'{key}' is not in the list."
    

arr = [24,56,32,13,24,64,34]
key = 32

x = LinearSearch(arr,key)
print(x)







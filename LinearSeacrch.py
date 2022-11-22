# Linear Search => sequential search



List1 = [23,43,234,432,234,32]
key = 32


def LinearSearch(List1,key):
    for i in range(len(List1)):
        if(List1[i]==key):
            print(i)
            break;
    else:
        print("Element not found")
        
LinearSearch(List1, key)

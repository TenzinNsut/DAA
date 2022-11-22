def bsearch(akey,left,right):
    if(right-left<0):
        return(False)
    mid=(left+right)//2
    if (arr[mid]==key):
        return arr[mid]
    if key<arr[mid]:
        return(bsearch(arr,key,left,mid-1))
    else:
        return(bsearch(arr,key,mid+1,right))



arr = [3,5,8,12,15,20,22,28]
key = 12
left = 0
right = len(arr) - 1


bsearch(arr,key,left,right)
#print(bsearch([1,2,3,4],5,0,3))
# print(bsearch(,3,0,3))
#print(bsearch([1,2,3,4],2,0,3))
#print(bsearch([1,2,3,4],3,0,3))
#print(bsearch([1,2,3,4],4
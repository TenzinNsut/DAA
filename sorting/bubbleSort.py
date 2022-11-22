def bubblesort(LA):
    for i in range(len(LA)-1,0,-1):
        for j in range(0,i):
            if LA[j]>LA[j+1]:
                (LA[j],LA[j+1])=(LA[j+1],LA[j])
    print("sorted list is",LA)


bubblesort([2,-1,6,1,5,3])
bubblesort([5,4,3,2,1])
bubblesort([10,-2,78,32,50,-8,100,200,150])
bubblesort([-1,30,45,100,200,50])
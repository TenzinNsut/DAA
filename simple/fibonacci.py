
def fib(n):
    if(n<0):
        return "invalid input, enter a +ve value instead"
    else:
        fibtable = {}
        fibtable[0] = 0
        fibtable[1] = 1
        for i in range (2,n+1):
            fibtable[i] = fibtable[i-1]+fibtable[i-2]
        return(fibtable[n])

print(fib(8))
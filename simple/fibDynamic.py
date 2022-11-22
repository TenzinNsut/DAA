
fibArray = [0,1]

def fib(n):
    if(n<0):
        print("invalid input")
    #initiallay fibArray[size = 2]
    elif(n < len(fibArray)):
        return fibArray[n]
    else:
        fibArray.append(fib(n-1)+fib(n-2))
        return fibArray[n]
    

print(fib(6))
            
             
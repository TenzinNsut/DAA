def factor(n):
    f=[1,n]
    for i in range(2,n):
        if n%i==0:
            f=f+[i]
    return(f)

def isprime(n):
    return(factor(n)==[1,n])

def primeuptonumber(n):
    (count,i,plist)=(0,2,[])
    while i<=n:
        if isprime(i):
            (count,plist)=(count+1,plist+[i])
        i=i+1
    print("total number of prime numbers",count)
    return(plist)

print(primeuptonumber(14))

import math

def isPrime(n):
    if(n==1):
        return False
    k=int(math.sqrt(n))
    for j in range(2,k+1):
        if(n%j==0):
            return False
    return True

def isMonisn(M,P):
    if(M<P):
        return False
    if(isPrime(M)==False or isPrime(P)==False):
        return False
    if(M==2**P-1):
        return True
    return False

print(isMonisn(31,5))

print("%s%10s" %("P","M"))
found=0;
for m in range(1,100):
    for p in range(1,100):
        if(isMonisn(m,p)==True):
            found=found+1
            print("%s%10s" %(m,p))
            if(found>6):
                break


def numberOfPrime(n):
    result = 0
    for i in range(1,n+1):
        num = 0
        for j in range(1, i+1 ):
            if i%j==0:
                num += 1
        if num ==2:
                result +=1
    return result

A = numberOfPrime(10000)
B = numberOfPrime(20000)
C = numberOfPrime(100000)
print(A+B+C)

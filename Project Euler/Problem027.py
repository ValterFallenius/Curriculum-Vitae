def erestat(n): #finds primenumbers less than n:
    num = list(range(n))
    for i in range(2,n):
        if num[i]!=0:
            for j in range(2*i,n,i):
                num[j]=0
    return num

primes=erestat(10**6)
nmax=0
amax=0
bmax=0
for a in range(-1000,1000):
    for b in range(-1000,1000):
        end=False
        n=0
        while not end:
            q=n**2+a*n+b
            if q==primes[q]:
                n+=1
            else:
                end=True
                if n>nmax:
                    amax=a
                    bmax=b
                    nmax=n
print(amax,bmax,nmax)
print("product =", amax*bmax)

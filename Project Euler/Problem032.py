import itertools
def erestat(n): #finds primenumbers less than n:
    num = list(range(2,n))
    for i in range(n-2):
        if num[i]!=0:
            for j in range(2*num[i],n-2,num[i]):
                num[j]=0
    num=list(filter(lambda a: a != 0, num))
    return num

def primefactors(n):
    m=n
    i=0
    primes=erestat(int(n/2)+1)
    primefactors=[]
    while m!=1:
        if m%primes[i]==0:
            primefactors.append(primes[i])
            m/=primes[i]
            m=int(m)
        else:
            i+=1
    return primefactors
N=3*7*13*91
p=primefactors(N)
print(list(itertools.combinations("0123", len(p))))
for i in itertools.combinations("0123", 3):
    prod=1
    print(i)
    for j in i:
        prod*=p[int(j)]
    print(prod)

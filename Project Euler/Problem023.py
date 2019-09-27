def product(array):
    prod=1
    for i in array:
        prod*=i
    return prod
N=28124
#finding all proper divisors
divisorlist=[]
numbers=list(range(1,N))
for i in numbers:
    divisors=[1]
    for j in range(2,(i)):
        if i%j==0:
            divisors.append(j)
    divisorlist.append(divisors)
print(divisorlist[-1])
#finding abundant numbers
trueabundants=[]
abundantnumbers=[]
for i in numbers:
    shortcut=False
    for j in trueabundants:
        if i%j==0:
            abundantnumbers.append(i)
            shortcut=True
            break
    if i<sum(divisorlist[i-1]) and not shortcut:
        trueabundants.append(i)
        abundantnumbers.append(i)
print(abundantnumbers)
doubles=[]
allints=list(range(N))
for i in abundantnumbers:
    for j in abundantnumbers:
        if j>i or i+j>N-1:
            break
        else:
            allints[i+j]=0
summation=sum(allints)
print(allints)
print(summation)

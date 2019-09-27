def product(lista,power):
    n=0
    for i in lista:
        n+=i**power
    return n

powernums=0
for i in range(2,1000000):
    string=str(i)
    integers=[]
    prod=0
    for j in string:
        integers.append(int(j))
    if i==product(integers,5):
        powernums+=i
        print(powernums)

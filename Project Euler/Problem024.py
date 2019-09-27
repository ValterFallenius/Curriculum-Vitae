index=0
integers=list(range(10))
number=""
N=10**6
import math
while index<N:
    remaining=len(integers)
    added=False
    for i in range(remaining):
        print(index+(i+1)*math.factorial(remaining-1))
        if index+(i+1)*math.factorial(remaining-1)>=N and not added:
            print("index", index)
            number+=str(integers.pop(i))
            index+=(i)*math.factorial(remaining-1)
            print("index", index, " number ", number)
            added=True


print(number)
